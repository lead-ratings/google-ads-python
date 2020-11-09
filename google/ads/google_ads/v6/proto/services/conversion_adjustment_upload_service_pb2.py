# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/services/conversion_adjustment_upload_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import conversion_adjustment_type_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_conversion__adjustment__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/services/conversion_adjustment_upload_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB&ConversionAdjustmentUploadServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nQgoogle/ads/googleads_v6/proto/services/conversion_adjustment_upload_service.proto\x12 google.ads.googleads.v6.services\x1a\x44google/ads/googleads_v6/proto/enums/conversion_adjustment_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/rpc/status.proto\"\xd0\x01\n\"UploadConversionAdjustmentsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12[\n\x16\x63onversion_adjustments\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v6.services.ConversionAdjustmentB\x03\xe0\x41\x02\x12\x1c\n\x0fpartial_failure\x18\x03 \x01(\x08\x42\x03\xe0\x41\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xa7\x01\n#UploadConversionAdjustmentsResponse\x12\x31\n\x15partial_failure_error\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12M\n\x07results\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v6.services.ConversionAdjustmentResult\"\xc8\x03\n\x14\x43onversionAdjustment\x12\x1e\n\x11\x63onversion_action\x18\x08 \x01(\tH\x01\x88\x01\x01\x12!\n\x14\x61\x64justment_date_time\x18\t \x01(\tH\x02\x88\x01\x01\x12m\n\x0f\x61\x64justment_type\x18\x05 \x01(\x0e\x32T.google.ads.googleads.v6.enums.ConversionAdjustmentTypeEnum.ConversionAdjustmentType\x12M\n\x11restatement_value\x18\x06 \x01(\x0b\x32\x32.google.ads.googleads.v6.services.RestatementValue\x12S\n\x14gclid_date_time_pair\x18\x01 \x01(\x0b\x32\x33.google.ads.googleads.v6.services.GclidDateTimePairH\x00\x12\x12\n\x08order_id\x18\x07 \x01(\tH\x00\x42\x17\n\x15\x63onversion_identifierB\x14\n\x12_conversion_actionB\x17\n\x15_adjustment_date_time\"p\n\x10RestatementValue\x12\x1b\n\x0e\x61\x64justed_value\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\x1a\n\rcurrency_code\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x11\n\x0f_adjusted_valueB\x10\n\x0e_currency_code\"m\n\x11GclidDateTimePair\x12\x12\n\x05gclid\x18\x03 \x01(\tH\x00\x88\x01\x01\x12!\n\x14\x63onversion_date_time\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_gclidB\x17\n\x15_conversion_date_time\"\xff\x02\n\x1a\x43onversionAdjustmentResult\x12\x1e\n\x11\x63onversion_action\x18\x07 \x01(\tH\x01\x88\x01\x01\x12!\n\x14\x61\x64justment_date_time\x18\x08 \x01(\tH\x02\x88\x01\x01\x12m\n\x0f\x61\x64justment_type\x18\x05 \x01(\x0e\x32T.google.ads.googleads.v6.enums.ConversionAdjustmentTypeEnum.ConversionAdjustmentType\x12S\n\x14gclid_date_time_pair\x18\x01 \x01(\x0b\x32\x33.google.ads.googleads.v6.services.GclidDateTimePairH\x00\x12\x12\n\x08order_id\x18\x06 \x01(\tH\x00\x42\x17\n\x15\x63onversion_identifierB\x14\n\x12_conversion_actionB\x17\n\x15_adjustment_date_time2\xe8\x02\n!ConversionAdjustmentUploadService\x12\xa5\x02\n\x1bUploadConversionAdjustments\x12\x44.google.ads.googleads.v6.services.UploadConversionAdjustmentsRequest\x1a\x45.google.ads.googleads.v6.services.UploadConversionAdjustmentsResponse\"y\x82\xd3\xe4\x93\x02>\"9/v6/customers/{customer_id=*}:uploadConversionAdjustments:\x01*\xda\x41\x32\x63ustomer_id,conversion_adjustments,partial_failure\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x8d\x02\n$com.google.ads.googleads.v6.servicesB&ConversionAdjustmentUploadServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_conversion__adjustment__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_UPLOADCONVERSIONADJUSTMENTSREQUEST = _descriptor.Descriptor(
  name='UploadConversionAdjustmentsRequest',
  full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conversion_adjustments', full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsRequest.conversion_adjustments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=303,
  serialized_end=511,
)


_UPLOADCONVERSIONADJUSTMENTSRESPONSE = _descriptor.Descriptor(
  name='UploadConversionAdjustmentsResponse',
  full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsResponse.partial_failure_error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v6.services.UploadConversionAdjustmentsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=514,
  serialized_end=681,
)


_CONVERSIONADJUSTMENT = _descriptor.Descriptor(
  name='ConversionAdjustment',
  full_name='google.ads.googleads.v6.services.ConversionAdjustment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversion_action', full_name='google.ads.googleads.v6.services.ConversionAdjustment.conversion_action', index=0,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment_date_time', full_name='google.ads.googleads.v6.services.ConversionAdjustment.adjustment_date_time', index=1,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment_type', full_name='google.ads.googleads.v6.services.ConversionAdjustment.adjustment_type', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='restatement_value', full_name='google.ads.googleads.v6.services.ConversionAdjustment.restatement_value', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gclid_date_time_pair', full_name='google.ads.googleads.v6.services.ConversionAdjustment.gclid_date_time_pair', index=4,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='google.ads.googleads.v6.services.ConversionAdjustment.order_id', index=5,
      number=7, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='conversion_identifier', full_name='google.ads.googleads.v6.services.ConversionAdjustment.conversion_identifier',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_conversion_action', full_name='google.ads.googleads.v6.services.ConversionAdjustment._conversion_action',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_adjustment_date_time', full_name='google.ads.googleads.v6.services.ConversionAdjustment._adjustment_date_time',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=684,
  serialized_end=1140,
)


_RESTATEMENTVALUE = _descriptor.Descriptor(
  name='RestatementValue',
  full_name='google.ads.googleads.v6.services.RestatementValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adjusted_value', full_name='google.ads.googleads.v6.services.RestatementValue.adjusted_value', index=0,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.ads.googleads.v6.services.RestatementValue.currency_code', index=1,
      number=4, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_adjusted_value', full_name='google.ads.googleads.v6.services.RestatementValue._adjusted_value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_currency_code', full_name='google.ads.googleads.v6.services.RestatementValue._currency_code',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1142,
  serialized_end=1254,
)


_GCLIDDATETIMEPAIR = _descriptor.Descriptor(
  name='GclidDateTimePair',
  full_name='google.ads.googleads.v6.services.GclidDateTimePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gclid', full_name='google.ads.googleads.v6.services.GclidDateTimePair.gclid', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conversion_date_time', full_name='google.ads.googleads.v6.services.GclidDateTimePair.conversion_date_time', index=1,
      number=4, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_gclid', full_name='google.ads.googleads.v6.services.GclidDateTimePair._gclid',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_conversion_date_time', full_name='google.ads.googleads.v6.services.GclidDateTimePair._conversion_date_time',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1256,
  serialized_end=1365,
)


_CONVERSIONADJUSTMENTRESULT = _descriptor.Descriptor(
  name='ConversionAdjustmentResult',
  full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversion_action', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult.conversion_action', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment_date_time', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult.adjustment_date_time', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment_type', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult.adjustment_type', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gclid_date_time_pair', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult.gclid_date_time_pair', index=3,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult.order_id', index=4,
      number=6, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='conversion_identifier', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult.conversion_identifier',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_conversion_action', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult._conversion_action',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_adjustment_date_time', full_name='google.ads.googleads.v6.services.ConversionAdjustmentResult._adjustment_date_time',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1368,
  serialized_end=1751,
)

_UPLOADCONVERSIONADJUSTMENTSREQUEST.fields_by_name['conversion_adjustments'].message_type = _CONVERSIONADJUSTMENT
_UPLOADCONVERSIONADJUSTMENTSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_UPLOADCONVERSIONADJUSTMENTSRESPONSE.fields_by_name['results'].message_type = _CONVERSIONADJUSTMENTRESULT
_CONVERSIONADJUSTMENT.fields_by_name['adjustment_type'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_conversion__adjustment__type__pb2._CONVERSIONADJUSTMENTTYPEENUM_CONVERSIONADJUSTMENTTYPE
_CONVERSIONADJUSTMENT.fields_by_name['restatement_value'].message_type = _RESTATEMENTVALUE
_CONVERSIONADJUSTMENT.fields_by_name['gclid_date_time_pair'].message_type = _GCLIDDATETIMEPAIR
_CONVERSIONADJUSTMENT.oneofs_by_name['conversion_identifier'].fields.append(
  _CONVERSIONADJUSTMENT.fields_by_name['gclid_date_time_pair'])
_CONVERSIONADJUSTMENT.fields_by_name['gclid_date_time_pair'].containing_oneof = _CONVERSIONADJUSTMENT.oneofs_by_name['conversion_identifier']
_CONVERSIONADJUSTMENT.oneofs_by_name['conversion_identifier'].fields.append(
  _CONVERSIONADJUSTMENT.fields_by_name['order_id'])
_CONVERSIONADJUSTMENT.fields_by_name['order_id'].containing_oneof = _CONVERSIONADJUSTMENT.oneofs_by_name['conversion_identifier']
_CONVERSIONADJUSTMENT.oneofs_by_name['_conversion_action'].fields.append(
  _CONVERSIONADJUSTMENT.fields_by_name['conversion_action'])
_CONVERSIONADJUSTMENT.fields_by_name['conversion_action'].containing_oneof = _CONVERSIONADJUSTMENT.oneofs_by_name['_conversion_action']
_CONVERSIONADJUSTMENT.oneofs_by_name['_adjustment_date_time'].fields.append(
  _CONVERSIONADJUSTMENT.fields_by_name['adjustment_date_time'])
_CONVERSIONADJUSTMENT.fields_by_name['adjustment_date_time'].containing_oneof = _CONVERSIONADJUSTMENT.oneofs_by_name['_adjustment_date_time']
_RESTATEMENTVALUE.oneofs_by_name['_adjusted_value'].fields.append(
  _RESTATEMENTVALUE.fields_by_name['adjusted_value'])
_RESTATEMENTVALUE.fields_by_name['adjusted_value'].containing_oneof = _RESTATEMENTVALUE.oneofs_by_name['_adjusted_value']
_RESTATEMENTVALUE.oneofs_by_name['_currency_code'].fields.append(
  _RESTATEMENTVALUE.fields_by_name['currency_code'])
_RESTATEMENTVALUE.fields_by_name['currency_code'].containing_oneof = _RESTATEMENTVALUE.oneofs_by_name['_currency_code']
_GCLIDDATETIMEPAIR.oneofs_by_name['_gclid'].fields.append(
  _GCLIDDATETIMEPAIR.fields_by_name['gclid'])
_GCLIDDATETIMEPAIR.fields_by_name['gclid'].containing_oneof = _GCLIDDATETIMEPAIR.oneofs_by_name['_gclid']
_GCLIDDATETIMEPAIR.oneofs_by_name['_conversion_date_time'].fields.append(
  _GCLIDDATETIMEPAIR.fields_by_name['conversion_date_time'])
_GCLIDDATETIMEPAIR.fields_by_name['conversion_date_time'].containing_oneof = _GCLIDDATETIMEPAIR.oneofs_by_name['_conversion_date_time']
_CONVERSIONADJUSTMENTRESULT.fields_by_name['adjustment_type'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_conversion__adjustment__type__pb2._CONVERSIONADJUSTMENTTYPEENUM_CONVERSIONADJUSTMENTTYPE
_CONVERSIONADJUSTMENTRESULT.fields_by_name['gclid_date_time_pair'].message_type = _GCLIDDATETIMEPAIR
_CONVERSIONADJUSTMENTRESULT.oneofs_by_name['conversion_identifier'].fields.append(
  _CONVERSIONADJUSTMENTRESULT.fields_by_name['gclid_date_time_pair'])
_CONVERSIONADJUSTMENTRESULT.fields_by_name['gclid_date_time_pair'].containing_oneof = _CONVERSIONADJUSTMENTRESULT.oneofs_by_name['conversion_identifier']
_CONVERSIONADJUSTMENTRESULT.oneofs_by_name['conversion_identifier'].fields.append(
  _CONVERSIONADJUSTMENTRESULT.fields_by_name['order_id'])
_CONVERSIONADJUSTMENTRESULT.fields_by_name['order_id'].containing_oneof = _CONVERSIONADJUSTMENTRESULT.oneofs_by_name['conversion_identifier']
_CONVERSIONADJUSTMENTRESULT.oneofs_by_name['_conversion_action'].fields.append(
  _CONVERSIONADJUSTMENTRESULT.fields_by_name['conversion_action'])
_CONVERSIONADJUSTMENTRESULT.fields_by_name['conversion_action'].containing_oneof = _CONVERSIONADJUSTMENTRESULT.oneofs_by_name['_conversion_action']
_CONVERSIONADJUSTMENTRESULT.oneofs_by_name['_adjustment_date_time'].fields.append(
  _CONVERSIONADJUSTMENTRESULT.fields_by_name['adjustment_date_time'])
_CONVERSIONADJUSTMENTRESULT.fields_by_name['adjustment_date_time'].containing_oneof = _CONVERSIONADJUSTMENTRESULT.oneofs_by_name['_adjustment_date_time']
DESCRIPTOR.message_types_by_name['UploadConversionAdjustmentsRequest'] = _UPLOADCONVERSIONADJUSTMENTSREQUEST
DESCRIPTOR.message_types_by_name['UploadConversionAdjustmentsResponse'] = _UPLOADCONVERSIONADJUSTMENTSRESPONSE
DESCRIPTOR.message_types_by_name['ConversionAdjustment'] = _CONVERSIONADJUSTMENT
DESCRIPTOR.message_types_by_name['RestatementValue'] = _RESTATEMENTVALUE
DESCRIPTOR.message_types_by_name['GclidDateTimePair'] = _GCLIDDATETIMEPAIR
DESCRIPTOR.message_types_by_name['ConversionAdjustmentResult'] = _CONVERSIONADJUSTMENTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadConversionAdjustmentsRequest = _reflection.GeneratedProtocolMessageType('UploadConversionAdjustmentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCONVERSIONADJUSTMENTSREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.conversion_adjustment_upload_service_pb2'
  ,
  '__doc__': """Request message for [ConversionAdjustmentUploadService.UploadConversio
  nAdjustments][google.ads.googleads.v6.services.ConversionAdjustmentUpl
  oadService.UploadConversionAdjustments].
  
  Attributes:
      customer_id:
          Required. The ID of the customer performing the upload.
      conversion_adjustments:
          Required. The conversion adjustments that are being uploaded.
      partial_failure:
          Required. If true, successful operations will be carried out
          and invalid operations will return errors. If false, all
          operations will be carried out in one transaction if and only
          if they are all valid. This should always be set to true. See
          https://developers.google.com/google-ads/api/docs/best-
          practices/partial-failures for more information about partial
          failure.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.UploadConversionAdjustmentsRequest)
  })
_sym_db.RegisterMessage(UploadConversionAdjustmentsRequest)

UploadConversionAdjustmentsResponse = _reflection.GeneratedProtocolMessageType('UploadConversionAdjustmentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCONVERSIONADJUSTMENTSRESPONSE,
  '__module__' : 'google.ads.googleads_v6.proto.services.conversion_adjustment_upload_service_pb2'
  ,
  '__doc__': """Response message for [ConversionAdjustmentUploadService.UploadConversi
  onAdjustments][google.ads.googleads.v6.services.ConversionAdjustmentUp
  loadService.UploadConversionAdjustments].
  
  Attributes:
      partial_failure_error:
          Errors that pertain to conversion adjustment failures in the
          partial failure mode. Returned when all errors occur inside
          the adjustments. If any errors occur outside the adjustments
          (e.g. auth errors), we return an RPC level error. See
          https://developers.google.com/google-ads/api/docs/best-
          practices/partial-failures for more information about partial
          failure.
      results:
          Returned for successfully processed conversion adjustments.
          Proto will be empty for rows that received an error. Results
          are not returned when validate\_only is true.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.UploadConversionAdjustmentsResponse)
  })
_sym_db.RegisterMessage(UploadConversionAdjustmentsResponse)

ConversionAdjustment = _reflection.GeneratedProtocolMessageType('ConversionAdjustment', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONADJUSTMENT,
  '__module__' : 'google.ads.googleads_v6.proto.services.conversion_adjustment_upload_service_pb2'
  ,
  '__doc__': """A conversion adjustment.
  
  Attributes:
      conversion_action:
          Resource name of the conversion action associated with this
          conversion adjustment. Note: Although this resource name
          consists of a customer id and a conversion action id,
          validation will ignore the customer id and use the conversion
          action id as the sole identifier of the conversion action.
      adjustment_date_time:
          The date time at which the adjustment occurred. Must be after
          the conversion\_date\_time. The timezone must be specified.
          The format is "yyyy-mm-dd hh:mm:ss+\|-hh:mm", e.g. "2019-01-01
          12:32:45-08:00".
      adjustment_type:
          The adjustment type.
      restatement_value:
          Information needed to restate the conversion's value. Required
          for restatements. Should not be supplied for retractions. An
          error will be returned if provided for a retraction. NOTE: If
          you want to upload a second restatement with a different
          adjusted value, it must have a new, more recent, adjustment
          occurrence time. Otherwise, it will be treated as a duplicate
          of the previous restatement and ignored.
      conversion_identifier:
          Identifies the conversion to be adjusted.
      gclid_date_time_pair:
          Uniquely identifies a conversion that was reported without an
          order ID specified.
      order_id:
          The order ID of the conversion to be adjusted. If the
          conversion was reported with an order ID specified, that order
          ID must be used as the identifier here.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.ConversionAdjustment)
  })
_sym_db.RegisterMessage(ConversionAdjustment)

RestatementValue = _reflection.GeneratedProtocolMessageType('RestatementValue', (_message.Message,), {
  'DESCRIPTOR' : _RESTATEMENTVALUE,
  '__module__' : 'google.ads.googleads_v6.proto.services.conversion_adjustment_upload_service_pb2'
  ,
  '__doc__': """Contains information needed to restate a conversion's value.
  
  Attributes:
      adjusted_value:
          The restated conversion value. This is the value of the
          conversion after restatement. For example, to change the value
          of a conversion from 100 to 70, an adjusted value of 70 should
          be reported. NOTE: If you want to upload a second restatement
          with a different adjusted value, it must have a new, more
          recent, adjustment occurrence time. Otherwise, it will be
          treated as a duplicate of the previous restatement and
          ignored.
      currency_code:
          The currency of the restated value. If not provided, then the
          default currency from the conversion action is used, and if
          that is not set then the account currency is used. This is the
          ISO 4217 3-character currency code e.g. USD or EUR.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.RestatementValue)
  })
_sym_db.RegisterMessage(RestatementValue)

GclidDateTimePair = _reflection.GeneratedProtocolMessageType('GclidDateTimePair', (_message.Message,), {
  'DESCRIPTOR' : _GCLIDDATETIMEPAIR,
  '__module__' : 'google.ads.googleads_v6.proto.services.conversion_adjustment_upload_service_pb2'
  ,
  '__doc__': """Uniquely identifies a conversion that was reported without an order ID
  specified.
  
  Attributes:
      gclid:
          Google click ID (gclid) associated with the original
          conversion for this adjustment.
      conversion_date_time:
          The date time at which the original conversion for this
          adjustment occurred. The timezone must be specified. The
          format is "yyyy-mm-dd hh:mm:ss+\|-hh:mm", e.g. "2019-01-01
          12:32:45-08:00".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GclidDateTimePair)
  })
_sym_db.RegisterMessage(GclidDateTimePair)

ConversionAdjustmentResult = _reflection.GeneratedProtocolMessageType('ConversionAdjustmentResult', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONADJUSTMENTRESULT,
  '__module__' : 'google.ads.googleads_v6.proto.services.conversion_adjustment_upload_service_pb2'
  ,
  '__doc__': """Information identifying a successfully processed ConversionAdjustment.
  
  Attributes:
      conversion_action:
          Resource name of the conversion action associated with this
          conversion adjustment.
      adjustment_date_time:
          The date time at which the adjustment occurred. The format is
          "yyyy-mm-dd hh:mm:ss+\|-hh:mm", e.g. "2019-01-01
          12:32:45-08:00".
      adjustment_type:
          The adjustment type.
      conversion_identifier:
          Identifies the conversion that was adjusted.
      gclid_date_time_pair:
          Uniquely identifies a conversion that was reported without an
          order ID specified.
      order_id:
          The order ID of the conversion that was adjusted.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.ConversionAdjustmentResult)
  })
_sym_db.RegisterMessage(ConversionAdjustmentResult)


DESCRIPTOR._options = None
_UPLOADCONVERSIONADJUSTMENTSREQUEST.fields_by_name['customer_id']._options = None
_UPLOADCONVERSIONADJUSTMENTSREQUEST.fields_by_name['conversion_adjustments']._options = None
_UPLOADCONVERSIONADJUSTMENTSREQUEST.fields_by_name['partial_failure']._options = None

_CONVERSIONADJUSTMENTUPLOADSERVICE = _descriptor.ServiceDescriptor(
  name='ConversionAdjustmentUploadService',
  full_name='google.ads.googleads.v6.services.ConversionAdjustmentUploadService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1754,
  serialized_end=2114,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadConversionAdjustments',
    full_name='google.ads.googleads.v6.services.ConversionAdjustmentUploadService.UploadConversionAdjustments',
    index=0,
    containing_service=None,
    input_type=_UPLOADCONVERSIONADJUSTMENTSREQUEST,
    output_type=_UPLOADCONVERSIONADJUSTMENTSRESPONSE,
    serialized_options=b'\202\323\344\223\002>\"9/v6/customers/{customer_id=*}:uploadConversionAdjustments:\001*\332A2customer_id,conversion_adjustments,partial_failure',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONVERSIONADJUSTMENTUPLOADSERVICE)

DESCRIPTOR.services_by_name['ConversionAdjustmentUploadService'] = _CONVERSIONADJUSTMENTUPLOADSERVICE

# @@protoc_insertion_point(module_scope)
