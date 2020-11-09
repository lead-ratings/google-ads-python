# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/errors/date_range_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/errors/date_range_error.proto',
  package='google.ads.googleads.v6.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.errorsB\023DateRangeErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Errors\312\002\036Google\\Ads\\GoogleAds\\V6\\Errors\352\002\"Google::Ads::GoogleAds::V6::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads_v6/proto/errors/date_range_error.proto\x12\x1egoogle.ads.googleads.v6.errors\x1a\x1cgoogle/api/annotations.proto\"\xe6\x01\n\x12\x44\x61teRangeErrorEnum\"\xcf\x01\n\x0e\x44\x61teRangeError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0cINVALID_DATE\x10\x02\x12\x1d\n\x19START_DATE_AFTER_END_DATE\x10\x03\x12\x1b\n\x17\x43\x41NNOT_SET_DATE_TO_PAST\x10\x04\x12 \n\x1c\x41\x46TER_MAXIMUM_ALLOWABLE_DATE\x10\x05\x12/\n+CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED\x10\x06\x42\xee\x01\n\"com.google.ads.googleads.v6.errorsB\x13\x44\x61teRangeErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Errors\xea\x02\"Google::Ads::GoogleAds::V6::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_DATERANGEERRORENUM_DATERANGEERROR = _descriptor.EnumDescriptor(
  name='DateRangeError',
  full_name='google.ads.googleads.v6.errors.DateRangeErrorEnum.DateRangeError',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='START_DATE_AFTER_END_DATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_DATE_TO_PAST', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AFTER_MAXIMUM_ALLOWABLE_DATE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=149,
  serialized_end=356,
)
_sym_db.RegisterEnumDescriptor(_DATERANGEERRORENUM_DATERANGEERROR)


_DATERANGEERRORENUM = _descriptor.Descriptor(
  name='DateRangeErrorEnum',
  full_name='google.ads.googleads.v6.errors.DateRangeErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATERANGEERRORENUM_DATERANGEERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=356,
)

_DATERANGEERRORENUM_DATERANGEERROR.containing_type = _DATERANGEERRORENUM
DESCRIPTOR.message_types_by_name['DateRangeErrorEnum'] = _DATERANGEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DateRangeErrorEnum = _reflection.GeneratedProtocolMessageType('DateRangeErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _DATERANGEERRORENUM,
  '__module__' : 'google.ads.googleads_v6.proto.errors.date_range_error_pb2'
  ,
  '__doc__': """Container for enum describing possible date range errors.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.errors.DateRangeErrorEnum)
  })
_sym_db.RegisterMessage(DateRangeErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
