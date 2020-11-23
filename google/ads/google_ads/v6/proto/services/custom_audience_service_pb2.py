# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/services/custom_audience_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.resources import custom_audience_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_custom__audience__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/services/custom_audience_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\032CustomAudienceServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDgoogle/ads/googleads_v6/proto/services/custom_audience_service.proto\x12 google.ads.googleads.v6.services\x1a=google/ads/googleads_v6/proto/resources/custom_audience.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"b\n\x18GetCustomAudienceRequest\x12\x46\n\rresource_name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'googleads.googleapis.com/CustomAudience\"\xa3\x01\n\x1cMutateCustomAudiencesRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12R\n\noperations\x18\x02 \x03(\x0b\x32\x39.google.ads.googleads.v6.services.CustomAudienceOperationB\x03\xe0\x41\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\"\xf3\x01\n\x17\x43ustomAudienceOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x43\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x31.google.ads.googleads.v6.resources.CustomAudienceH\x00\x12\x43\n\x06update\x18\x02 \x01(\x0b\x32\x31.google.ads.googleads.v6.resources.CustomAudienceH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"n\n\x1dMutateCustomAudiencesResponse\x12M\n\x07results\x18\x01 \x03(\x0b\x32<.google.ads.googleads.v6.services.MutateCustomAudienceResult\"3\n\x1aMutateCustomAudienceResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xf9\x03\n\x15\x43ustomAudienceService\x12\xcd\x01\n\x11GetCustomAudience\x12:.google.ads.googleads.v6.services.GetCustomAudienceRequest\x1a\x31.google.ads.googleads.v6.resources.CustomAudience\"I\x82\xd3\xe4\x93\x02\x33\x12\x31/v6/{resource_name=customers/*/customAudiences/*}\xda\x41\rresource_name\x12\xf2\x01\n\x15MutateCustomAudiences\x12>.google.ads.googleads.v6.services.MutateCustomAudiencesRequest\x1a?.google.ads.googleads.v6.services.MutateCustomAudiencesResponse\"X\x82\xd3\xe4\x93\x02\x39\"4/v6/customers/{customer_id=*}/customAudiences:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x81\x02\n$com.google.ads.googleads.v6.servicesB\x1a\x43ustomAudienceServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_custom__audience__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETCUSTOMAUDIENCEREQUEST = _descriptor.Descriptor(
  name='GetCustomAudienceRequest',
  full_name='google.ads.googleads.v6.services.GetCustomAudienceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.GetCustomAudienceRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A)\n\'googleads.googleapis.com/CustomAudience', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=318,
  serialized_end=416,
)


_MUTATECUSTOMAUDIENCESREQUEST = _descriptor.Descriptor(
  name='MutateCustomAudiencesRequest',
  full_name='google.ads.googleads.v6.services.MutateCustomAudiencesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.MutateCustomAudiencesRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v6.services.MutateCustomAudiencesRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v6.services.MutateCustomAudiencesRequest.validate_only', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=419,
  serialized_end=582,
)


_CUSTOMAUDIENCEOPERATION = _descriptor.Descriptor(
  name='CustomAudienceOperation',
  full_name='google.ads.googleads.v6.services.CustomAudienceOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v6.services.CustomAudienceOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v6.services.CustomAudienceOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v6.services.CustomAudienceOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v6.services.CustomAudienceOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
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
      name='operation', full_name='google.ads.googleads.v6.services.CustomAudienceOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=585,
  serialized_end=828,
)


_MUTATECUSTOMAUDIENCESRESPONSE = _descriptor.Descriptor(
  name='MutateCustomAudiencesResponse',
  full_name='google.ads.googleads.v6.services.MutateCustomAudiencesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v6.services.MutateCustomAudiencesResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=830,
  serialized_end=940,
)


_MUTATECUSTOMAUDIENCERESULT = _descriptor.Descriptor(
  name='MutateCustomAudienceResult',
  full_name='google.ads.googleads.v6.services.MutateCustomAudienceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.MutateCustomAudienceResult.resource_name', index=0,
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
  serialized_start=942,
  serialized_end=993,
)

_MUTATECUSTOMAUDIENCESREQUEST.fields_by_name['operations'].message_type = _CUSTOMAUDIENCEOPERATION
_CUSTOMAUDIENCEOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CUSTOMAUDIENCEOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_custom__audience__pb2._CUSTOMAUDIENCE
_CUSTOMAUDIENCEOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_custom__audience__pb2._CUSTOMAUDIENCE
_CUSTOMAUDIENCEOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMAUDIENCEOPERATION.fields_by_name['create'])
_CUSTOMAUDIENCEOPERATION.fields_by_name['create'].containing_oneof = _CUSTOMAUDIENCEOPERATION.oneofs_by_name['operation']
_CUSTOMAUDIENCEOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMAUDIENCEOPERATION.fields_by_name['update'])
_CUSTOMAUDIENCEOPERATION.fields_by_name['update'].containing_oneof = _CUSTOMAUDIENCEOPERATION.oneofs_by_name['operation']
_CUSTOMAUDIENCEOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMAUDIENCEOPERATION.fields_by_name['remove'])
_CUSTOMAUDIENCEOPERATION.fields_by_name['remove'].containing_oneof = _CUSTOMAUDIENCEOPERATION.oneofs_by_name['operation']
_MUTATECUSTOMAUDIENCESRESPONSE.fields_by_name['results'].message_type = _MUTATECUSTOMAUDIENCERESULT
DESCRIPTOR.message_types_by_name['GetCustomAudienceRequest'] = _GETCUSTOMAUDIENCEREQUEST
DESCRIPTOR.message_types_by_name['MutateCustomAudiencesRequest'] = _MUTATECUSTOMAUDIENCESREQUEST
DESCRIPTOR.message_types_by_name['CustomAudienceOperation'] = _CUSTOMAUDIENCEOPERATION
DESCRIPTOR.message_types_by_name['MutateCustomAudiencesResponse'] = _MUTATECUSTOMAUDIENCESRESPONSE
DESCRIPTOR.message_types_by_name['MutateCustomAudienceResult'] = _MUTATECUSTOMAUDIENCERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomAudienceRequest = _reflection.GeneratedProtocolMessageType('GetCustomAudienceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMAUDIENCEREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.custom_audience_service_pb2'
  ,
  '__doc__': """Request message for [CustomAudienceService.GetCustomAudience][google.a
  ds.googleads.v6.services.CustomAudienceService.GetCustomAudience].
  
  Attributes:
      resource_name:
          Required. The resource name of the custom audience to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GetCustomAudienceRequest)
  })
_sym_db.RegisterMessage(GetCustomAudienceRequest)

MutateCustomAudiencesRequest = _reflection.GeneratedProtocolMessageType('MutateCustomAudiencesRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMAUDIENCESREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.custom_audience_service_pb2'
  ,
  '__doc__': """Request message for [CustomAudienceService.MutateCustomAudiences][goog
  le.ads.googleads.v6.services.CustomAudienceService.MutateCustomAudienc
  es].
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose custom audiences are
          being modified.
      operations:
          Required. The list of operations to perform on individual
          custom audiences.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomAudiencesRequest)
  })
_sym_db.RegisterMessage(MutateCustomAudiencesRequest)

CustomAudienceOperation = _reflection.GeneratedProtocolMessageType('CustomAudienceOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMAUDIENCEOPERATION,
  '__module__' : 'google.ads.googleads_v6.proto.services.custom_audience_service_pb2'
  ,
  '__doc__': """A single operation (create, update) on a custom audience.
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          custom audience.
      update:
          Update operation: The custom audience is expected to have a
          valid resource name.
      remove:
          Remove operation: A resource name for the removed custom
          audience is expected, in this format:  ``customers/{customer_i
          d}/customAudiences/{custom_audience_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CustomAudienceOperation)
  })
_sym_db.RegisterMessage(CustomAudienceOperation)

MutateCustomAudiencesResponse = _reflection.GeneratedProtocolMessageType('MutateCustomAudiencesResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMAUDIENCESRESPONSE,
  '__module__' : 'google.ads.googleads_v6.proto.services.custom_audience_service_pb2'
  ,
  '__doc__': """Response message for custom audience mutate.
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomAudiencesResponse)
  })
_sym_db.RegisterMessage(MutateCustomAudiencesResponse)

MutateCustomAudienceResult = _reflection.GeneratedProtocolMessageType('MutateCustomAudienceResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMAUDIENCERESULT,
  '__module__' : 'google.ads.googleads_v6.proto.services.custom_audience_service_pb2'
  ,
  '__doc__': """The result for the custom audience mutate.
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomAudienceResult)
  })
_sym_db.RegisterMessage(MutateCustomAudienceResult)


DESCRIPTOR._options = None
_GETCUSTOMAUDIENCEREQUEST.fields_by_name['resource_name']._options = None
_MUTATECUSTOMAUDIENCESREQUEST.fields_by_name['customer_id']._options = None
_MUTATECUSTOMAUDIENCESREQUEST.fields_by_name['operations']._options = None

_CUSTOMAUDIENCESERVICE = _descriptor.ServiceDescriptor(
  name='CustomAudienceService',
  full_name='google.ads.googleads.v6.services.CustomAudienceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=996,
  serialized_end=1501,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomAudience',
    full_name='google.ads.googleads.v6.services.CustomAudienceService.GetCustomAudience',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMAUDIENCEREQUEST,
    output_type=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_custom__audience__pb2._CUSTOMAUDIENCE,
    serialized_options=b'\202\323\344\223\0023\0221/v6/{resource_name=customers/*/customAudiences/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateCustomAudiences',
    full_name='google.ads.googleads.v6.services.CustomAudienceService.MutateCustomAudiences',
    index=1,
    containing_service=None,
    input_type=_MUTATECUSTOMAUDIENCESREQUEST,
    output_type=_MUTATECUSTOMAUDIENCESRESPONSE,
    serialized_options=b'\202\323\344\223\0029\"4/v6/customers/{customer_id=*}/customAudiences:mutate:\001*\332A\026customer_id,operations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMAUDIENCESERVICE)

DESCRIPTOR.services_by_name['CustomAudienceService'] = _CUSTOMAUDIENCESERVICE

# @@protoc_insertion_point(module_scope)