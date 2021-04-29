# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redhvid/flight_video_distributor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='redhvid/flight_video_distributor.proto',
  package='redhvid',
  syntax='proto3',
  serialized_options=b'\252\002\007redhvid',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&redhvid/flight_video_distributor.proto\x12\x07redhvid\"%\n\x12\x46lightVideoMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2Z\n\x16\x46lightVideoDistributor\x12@\n\x04\x45\x63ho\x12\x1b.redhvid.FlightVideoMessage\x1a\x1b.redhvid.FlightVideoMessageB\n\xaa\x02\x07redhvidb\x06proto3'
)




_FLIGHTVIDEOMESSAGE = _descriptor.Descriptor(
  name='FlightVideoMessage',
  full_name='redhvid.FlightVideoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='redhvid.FlightVideoMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['FlightVideoMessage'] = _FLIGHTVIDEOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlightVideoMessage = _reflection.GeneratedProtocolMessageType('FlightVideoMessage', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHTVIDEOMESSAGE,
  '__module__' : 'redhvid.flight_video_distributor_pb2'
  # @@protoc_insertion_point(class_scope:redhvid.FlightVideoMessage)
  })
_sym_db.RegisterMessage(FlightVideoMessage)


DESCRIPTOR._options = None

_FLIGHTVIDEODISTRIBUTOR = _descriptor.ServiceDescriptor(
  name='FlightVideoDistributor',
  full_name='redhvid.FlightVideoDistributor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=90,
  serialized_end=180,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='redhvid.FlightVideoDistributor.Echo',
    index=0,
    containing_service=None,
    input_type=_FLIGHTVIDEOMESSAGE,
    output_type=_FLIGHTVIDEOMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FLIGHTVIDEODISTRIBUTOR)

DESCRIPTOR.services_by_name['FlightVideoDistributor'] = _FLIGHTVIDEODISTRIBUTOR

# @@protoc_insertion_point(module_scope)