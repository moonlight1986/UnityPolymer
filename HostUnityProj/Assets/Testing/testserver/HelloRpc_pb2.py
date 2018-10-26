# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HelloRpc.proto

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
  name='HelloRpc.proto',
  package='hello',
  syntax='proto3',
  serialized_pb=_b('\n\x0eHelloRpc.proto\x12\x05hello\" \n\x0cHelloRequest\x12\x10\n\x08greeting\x18\x01 \x01(\t\".\n\rHelloResponse\x12\r\n\x05reply\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x04 \x03(\x05\" \n\x0cWorldRequest\x12\x10\n\x08greeting\x18\x01 \x01(\t\"\x1e\n\rWorldResponse\x12\r\n\x05reply\x18\x01 \x01(\t2E\n\x0cHelloService\x12\x35\n\x08SayHello\x12\x13.hello.HelloRequest\x1a\x14.hello.HelloResponse2|\n\x0cWorldService\x12\x35\n\x08SayHello\x12\x13.hello.HelloRequest\x1a\x14.hello.WorldResponse\x12\x35\n\x08SayWorld\x12\x13.hello.WorldRequest\x1a\x14.hello.WorldResponseb\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='hello.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='hello.HelloRequest.greeting', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=25,
  serialized_end=57,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='hello.HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='hello.HelloResponse.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number', full_name='hello.HelloResponse.number', index=1,
      number=4, type=5, cpp_type=1, label=3,
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
  serialized_start=59,
  serialized_end=105,
)


_WORLDREQUEST = _descriptor.Descriptor(
  name='WorldRequest',
  full_name='hello.WorldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='hello.WorldRequest.greeting', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=107,
  serialized_end=139,
)


_WORLDRESPONSE = _descriptor.Descriptor(
  name='WorldResponse',
  full_name='hello.WorldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='hello.WorldResponse.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=141,
  serialized_end=171,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE
DESCRIPTOR.message_types_by_name['WorldRequest'] = _WORLDREQUEST
DESCRIPTOR.message_types_by_name['WorldResponse'] = _WORLDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'HelloRpc_pb2'
  # @@protoc_insertion_point(class_scope:hello.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), dict(
  DESCRIPTOR = _HELLORESPONSE,
  __module__ = 'HelloRpc_pb2'
  # @@protoc_insertion_point(class_scope:hello.HelloResponse)
  ))
_sym_db.RegisterMessage(HelloResponse)

WorldRequest = _reflection.GeneratedProtocolMessageType('WorldRequest', (_message.Message,), dict(
  DESCRIPTOR = _WORLDREQUEST,
  __module__ = 'HelloRpc_pb2'
  # @@protoc_insertion_point(class_scope:hello.WorldRequest)
  ))
_sym_db.RegisterMessage(WorldRequest)

WorldResponse = _reflection.GeneratedProtocolMessageType('WorldResponse', (_message.Message,), dict(
  DESCRIPTOR = _WORLDRESPONSE,
  __module__ = 'HelloRpc_pb2'
  # @@protoc_insertion_point(class_scope:hello.WorldResponse)
  ))
_sym_db.RegisterMessage(WorldResponse)


# @@protoc_insertion_point(module_scope)
