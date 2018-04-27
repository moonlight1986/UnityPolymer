# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='version.proto',
  package='version',
  syntax='proto3',
  serialized_pb=_b('\n\rversion.proto\x12\x07version\"\xb2\x01\n\x0bVersionItem\x12\x11\n\tchannelId\x18\x01 \x01(\x05\x12\x15\n\rappMinVersion\x18\x02 \x01(\x05\x12\x18\n\x10\x61ppTargetVersion\x18\x03 \x01(\x05\x12\x16\n\x0e\x61ppTestVersion\x18\x04 \x01(\x05\x12\x15\n\rresMinVersion\x18\x05 \x01(\x05\x12\x18\n\x10resTargetVersion\x18\x06 \x01(\x05\x12\x16\n\x0eresTestVersion\x18\x07 \x01(\x05\"X\n\nVersionCfg\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x10\n\x08gameType\x18\x02 \x01(\x05\x12\'\n\tstVerItem\x18\x03 \x03(\x0b\x32\x14.version.VersionItemB\x11\xaa\x02\x0eVersons.Commonb\x06proto3')
)




_VERSIONITEM = _descriptor.Descriptor(
  name='VersionItem',
  full_name='version.VersionItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelId', full_name='version.VersionItem.channelId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appMinVersion', full_name='version.VersionItem.appMinVersion', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appTargetVersion', full_name='version.VersionItem.appTargetVersion', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appTestVersion', full_name='version.VersionItem.appTestVersion', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resMinVersion', full_name='version.VersionItem.resMinVersion', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resTargetVersion', full_name='version.VersionItem.resTargetVersion', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resTestVersion', full_name='version.VersionItem.resTestVersion', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=205,
)


_VERSIONCFG = _descriptor.Descriptor(
  name='VersionCfg',
  full_name='version.VersionCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='version.VersionCfg.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gameType', full_name='version.VersionCfg.gameType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stVerItem', full_name='version.VersionCfg.stVerItem', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=295,
)

_VERSIONCFG.fields_by_name['stVerItem'].message_type = _VERSIONITEM
DESCRIPTOR.message_types_by_name['VersionItem'] = _VERSIONITEM
DESCRIPTOR.message_types_by_name['VersionCfg'] = _VERSIONCFG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersionItem = _reflection.GeneratedProtocolMessageType('VersionItem', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONITEM,
  __module__ = 'version_pb2'
  # @@protoc_insertion_point(class_scope:version.VersionItem)
  ))
_sym_db.RegisterMessage(VersionItem)

VersionCfg = _reflection.GeneratedProtocolMessageType('VersionCfg', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONCFG,
  __module__ = 'version_pb2'
  # @@protoc_insertion_point(class_scope:version.VersionCfg)
  ))
_sym_db.RegisterMessage(VersionCfg)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\016Versons.Common'))
# @@protoc_insertion_point(module_scope)
