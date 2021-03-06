﻿using System.Collections.Generic;
using Ginkgo.IOC;
using UniRx;
#if UNITY_EDITOR
using UnityEditor;
#endif

namespace Ginkgo.UI
{
    /// <summary>
    /// 不同layer上的UI可以同时显示，相同layer总是显示最后一个而隐藏前一个ui
    /// traceback=true,不会删除前一个push的view，pop时候会重新显示。
    /// </summary>
    public sealed class GUIManager : MLSingleton<GUIManager>
    {
        class ViewContext
        {
            public UIView uiView;
            public bool traceback;
        }

        [Inject]
        IUIManagerService m_manipulator = null;
        IUIAssetCtrl m_assetCtrl = null;
        //list top always visible.
        List<List<UIView>> m_layerToViews;
        //用于缓存
        Dictionary<int, ViewContext> m_idToViews;

        Queue<int> m_pushQueue;
        HashSet<int> m_readySet;

        /// <summary>
        /// 不可弹出的层的最小值，小于该值的层不会被POP，同时MinUnpoppableLayer+1层为默认的Push层，
        /// 比如 当0层作为背景层，如果还需要到Push到0层，需要 MinUnpoppableLayer = GUIManager.POP_ALL，
        /// 主要是使用方便上的考虑
        /// </summary>
        public int MinUnpoppableLayer { get; set; }
        public const int POP_ALL = -1;

        protected override void onInitialize()
        {
            m_layerToViews = new List<List<UIView>>(3);
            m_idToViews = new Dictionary<int, ViewContext>();
            m_pushQueue = new Queue<int>();
            m_readySet = new HashSet<int>();
            m_assetCtrl = m_manipulator.InitManager();
            m_manipulator.InitLoadAssets(m_assetCtrl);
            //work on main thread?
            Observable.EveryEndOfFrame().Subscribe((_) =>
            {
                if(m_pushQueue.Count > 0)
                {
                    int id = m_pushQueue.Peek();
                    if (m_readySet.Remove(id))
                    {
                        m_pushQueue.Dequeue();
                        innerPush(id);
                    }
                }
            });
        }

#if UNITY_EDITOR
        public List<List<UIView>> GetLayerViews()
        {
            return m_layerToViews;
        }
#endif

        public bool Check()
        {
            return m_manipulator != null && m_assetCtrl != null;
        }

        public void Clean()
        {
            m_layerToViews.Clear();
            m_pushQueue.Clear();
            m_readySet.Clear();
            foreach(var di in m_idToViews)
            {
                di.Value.uiView.DestroyWhenHide = true;
                di.Value.uiView.Hide(false);
                di.Value.uiView.DestroyWhenHide = false;
            }
        }

        public int LayerNumber
        {
            get
            {
                return m_layerToViews.Count;
            }
        }
        /// <summary>
        /// Push and show a UI.
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="traceback">是否回退</param>
        /// <param name="onNewLayer">是否增到新一层上.</param>
        /// <returns></returns>
        public T Push<T>(bool traceback = false, bool onNewLayer = false) where T : UIView
        {
            var view = UIView.CreateView<T>();
            if (view != null)
            {
                view.OnNewLayer = onNewLayer;
                Push(view, traceback);
            }

            return view;
        }

        public void BringViewToLayer(int viewId, int layer)
        {
            int targetLayer = layer >= 0 ? layer : m_layerToViews.Count + layer;

            if (targetLayer >= 0 && targetLayer < m_layerToViews.Count)
            {
                ViewContext viewContext = getViewContext(viewId);
                if(viewContext != null)
                {
                    int sublayer;
                    int currentViewLayer = findLayerForView(viewContext.uiView, out sublayer);
                    if(currentViewLayer != -1 && currentViewLayer != targetLayer)
                    {
                        var currentViews = m_layerToViews[currentViewLayer];
                        //TODO: use swap.
                        m_layerToViews.RemoveAt(currentViewLayer);
                        m_layerToViews.Insert(targetLayer, currentViews);
                        UIView.adjustOrder(viewContext.uiView, targetLayer);
#if UNITY_EDITOR
                        EditorUtility.SetDirty(this);
#endif
                    }
                }
            }
        }
        public void BringViewToFront(int viewId)
        {
            BringViewToLayer(viewId, -1);
        }

        public void Pop(int layer = -1)
        {
            int targetLayer = layer >= 0 ? layer : m_layerToViews.Count + layer;
            
            if(m_layerToViews.Count > 0 
                && (targetLayer <= MinUnpoppableLayer))
            {
                Log.Common.Print("Pop Layer is bottom most, omit popping.");
                return;
            }

            if(targetLayer >=0 && targetLayer < m_layerToViews.Count)
            {
                var viewsOnLayer = m_layerToViews[targetLayer];
                if(viewsOnLayer.Count == 0)
                {
                    Log.Common.PrintWarning("Something wrong ? no view on Layer: " + targetLayer);
                    return;
                }
                var view = viewsOnLayer[viewsOnLayer.Count - 1];
                viewsOnLayer.RemoveAt(viewsOnLayer.Count - 1);

                int viewId = view.ViewId;
                m_readySet.Remove(viewId);
                if(m_pushQueue.Contains(viewId))
                {
                    var datas = m_pushQueue.ToArray();
                    m_pushQueue.Clear();
                    foreach (var d in datas)
                    {
                        if(d != viewId)
                        {
                            m_pushQueue.Enqueue(d);
                        }
                    }
                }
                if (view.DestroyWhenHide)
                {
                    m_idToViews.Remove(viewId);
                }
                view.Hide(view.HideAnimation);
                if(viewsOnLayer.Count > 0)
                {
                    view = viewsOnLayer[viewsOnLayer.Count - 1];
                    view.Show();
                }
                else
                {
                    m_layerToViews.RemoveAt(targetLayer);
                }
#if UNITY_EDITOR
                EditorUtility.SetDirty(this);
#endif
            }
        }

        int findLayerForView(UIView view, out int subLayer)
        {
            subLayer = -1;
            for (int i = 0; i < m_layerToViews.Count; i++)
            {
                subLayer = m_layerToViews[i].FindIndex((v) =>
                {
                    return v.ViewId == view.ViewId;
                });
                if(subLayer != -1)
                {
                    return i;
                }
            }
            return -1;
        }

        ViewContext getViewContext(int viewId)
        {
            ViewContext viewContext;
            if (!m_idToViews.TryGetValue(viewId, out viewContext))
            {
                Log.Common.PrintWarning("Get View null, view has been disposed after push ?");
                return null;
            }
            return viewContext;
        }

        void innerPush(int viewId)
        {
            var viewContext = getViewContext(viewId);
            if(viewContext == null)
            {
                return;
            }

            UIView view = viewContext.uiView;
            if(view.Processing)
            {
                Log.Common.Print("View {0}:{1} Is In process or Active in layer.", view.ViewId, view.Name);
                return;
            }
            int sublayer;
            int layer = findLayerForView(view, out sublayer);

            List<UIView> viewsOfLayer = null;
            int defaultPushLayer = MinUnpoppableLayer + 1;
            if (view.OnNewLayer
                || m_layerToViews.Count == 0 
                || defaultPushLayer > m_layerToViews.Count - 1)
            {
                if (layer != -1)
                {
                    Log.Common.Print(true, "View {0}:{1} already In Layer.", view.ViewId, view.Name);
                    return;
                }
                viewsOfLayer = new List<UIView>();
                m_layerToViews.Add(viewsOfLayer);
            }
            else
            {
                //find view already on layer?
                //var sv = from layers in m_layerToViews
                //from v in layers
                //where view == v
                //select v;

                if(layer != -1)
                {
                    viewsOfLayer = m_layerToViews[layer];
                    if(viewsOfLayer.Count - 1 == sublayer)
                    {
                        Log.Common.Print(true, "View {0}:{1} already on top.", view.ViewId, view.Name);
                        return;
                    }
                    else
                    {
                        viewsOfLayer.RemoveAt(sublayer);
                    }
                }

                //default push on last layer.
                int lastLayer = m_layerToViews.Count - 1;
                if (viewsOfLayer == null)
                {
                    viewsOfLayer = m_layerToViews[lastLayer];
                }
                int last = viewsOfLayer.Count - 1;
                if (last >= 0)
                {
                    UIView lastTopView = viewsOfLayer[last];
                    lastTopView.Hide(false);
                    if(!viewContext.traceback)
                    {
                        viewsOfLayer.RemoveAt(last);
                    }
                }
            }
            viewsOfLayer.Add(view);
            view.Show();
#if UNITY_EDITOR
            EditorUtility.SetDirty(this);
#endif
        }

        public void Push(UIView view, bool traceback=false)
        {
            if (view == null)
            {
                Log.Common.PrintWarning("?? Push null UIView...");
                return;
            }
            if (!m_idToViews.ContainsKey(view.ViewId))
            {
                m_idToViews.Add(view.ViewId, new ViewContext() {
                    uiView = view,
                    traceback = traceback
                });
            }
            
            if (!m_pushQueue.Contains(view.ViewId) && !m_readySet.Contains(view.ViewId))
            {
                m_pushQueue.Enqueue(view.ViewId);
                m_assetCtrl.PrepareAssets(view.PackageName, view.ComponentName, () =>
                {
                    m_readySet.Add(view.ViewId);
                });
            }
            else
            {
                Log.Common.Print("Multiple Push On view: " + view.Name);
            }
        }

        public T GetView<T>() where T : UIView
        {
            var type = typeof(T);
            foreach (var kv in m_idToViews)
            {
                if(kv.Value.GetType() == type)
                {
                    return kv.Value.uiView as T;
                }
            }
            return null;
        }

        public UIView GetView(int viewId)
        {
            ViewContext view;
            if (m_idToViews.TryGetValue(viewId, out view))
            {
                return view.uiView;
            }
            else
            {
                return null;
            }
        }

    }
}
