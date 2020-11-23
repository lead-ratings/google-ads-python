# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/services/customer_feed_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import response_content_type_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_response__content__type__pb2
from google.ads.google_ads.v6.proto.resources import customer_feed_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_customer__feed__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/services/customer_feed_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\030CustomerFeedServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBgoogle/ads/googleads_v6/proto/services/customer_feed_service.proto\x12 google.ads.googleads.v6.services\x1a?google/ads/googleads_v6/proto/enums/response_content_type.proto\x1a;google/ads/googleads_v6/proto/resources/customer_feed.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"^\n\x16GetCustomerFeedRequest\x12\x44\n\rresource_name\x18\x01 \x01(\tB-\xe0\x41\x02\xfa\x41\'\n%googleads.googleapis.com/CustomerFeed\"\xa3\x02\n\x1aMutateCustomerFeedsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12P\n\noperations\x18\x02 \x03(\x0b\x32\x37.google.ads.googleads.v6.services.CustomerFeedOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12i\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v6.enums.ResponseContentTypeEnum.ResponseContentType\"\xed\x01\n\x15\x43ustomerFeedOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x41\n\x06\x63reate\x18\x01 \x01(\x0b\x32/.google.ads.googleads.v6.resources.CustomerFeedH\x00\x12\x41\n\x06update\x18\x02 \x01(\x0b\x32/.google.ads.googleads.v6.resources.CustomerFeedH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x9d\x01\n\x1bMutateCustomerFeedsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12K\n\x07results\x18\x02 \x03(\x0b\x32:.google.ads.googleads.v6.services.MutateCustomerFeedResult\"y\n\x18MutateCustomerFeedResult\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x46\n\rcustomer_feed\x18\x02 \x01(\x0b\x32/.google.ads.googleads.v6.resources.CustomerFeed2\xe7\x03\n\x13\x43ustomerFeedService\x12\xc5\x01\n\x0fGetCustomerFeed\x12\x38.google.ads.googleads.v6.services.GetCustomerFeedRequest\x1a/.google.ads.googleads.v6.resources.CustomerFeed\"G\x82\xd3\xe4\x93\x02\x31\x12//v6/{resource_name=customers/*/customerFeeds/*}\xda\x41\rresource_name\x12\xea\x01\n\x13MutateCustomerFeeds\x12<.google.ads.googleads.v6.services.MutateCustomerFeedsRequest\x1a=.google.ads.googleads.v6.services.MutateCustomerFeedsResponse\"V\x82\xd3\xe4\x93\x02\x37\"2/v6/customers/{customer_id=*}/customerFeeds:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xff\x01\n$com.google.ads.googleads.v6.servicesB\x18\x43ustomerFeedServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_response__content__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_customer__feed__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETCUSTOMERFEEDREQUEST = _descriptor.Descriptor(
  name='GetCustomerFeedRequest',
  full_name='google.ads.googleads.v6.services.GetCustomerFeedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.GetCustomerFeedRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\'\n%googleads.googleapis.com/CustomerFeed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=404,
  serialized_end=498,
)


_MUTATECUSTOMERFEEDSREQUEST = _descriptor.Descriptor(
  name='MutateCustomerFeedsRequest',
  full_name='google.ads.googleads.v6.services.MutateCustomerFeedsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.MutateCustomerFeedsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v6.services.MutateCustomerFeedsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v6.services.MutateCustomerFeedsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v6.services.MutateCustomerFeedsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_content_type', full_name='google.ads.googleads.v6.services.MutateCustomerFeedsRequest.response_content_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=501,
  serialized_end=792,
)


_CUSTOMERFEEDOPERATION = _descriptor.Descriptor(
  name='CustomerFeedOperation',
  full_name='google.ads.googleads.v6.services.CustomerFeedOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v6.services.CustomerFeedOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v6.services.CustomerFeedOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v6.services.CustomerFeedOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v6.services.CustomerFeedOperation.remove', index=3,
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
      name='operation', full_name='google.ads.googleads.v6.services.CustomerFeedOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=795,
  serialized_end=1032,
)


_MUTATECUSTOMERFEEDSRESPONSE = _descriptor.Descriptor(
  name='MutateCustomerFeedsResponse',
  full_name='google.ads.googleads.v6.services.MutateCustomerFeedsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v6.services.MutateCustomerFeedsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v6.services.MutateCustomerFeedsResponse.results', index=1,
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
  serialized_start=1035,
  serialized_end=1192,
)


_MUTATECUSTOMERFEEDRESULT = _descriptor.Descriptor(
  name='MutateCustomerFeedResult',
  full_name='google.ads.googleads.v6.services.MutateCustomerFeedResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.MutateCustomerFeedResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_feed', full_name='google.ads.googleads.v6.services.MutateCustomerFeedResult.customer_feed', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1194,
  serialized_end=1315,
)

_MUTATECUSTOMERFEEDSREQUEST.fields_by_name['operations'].message_type = _CUSTOMERFEEDOPERATION
_MUTATECUSTOMERFEEDSREQUEST.fields_by_name['response_content_type'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_response__content__type__pb2._RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE
_CUSTOMERFEEDOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CUSTOMERFEEDOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_customer__feed__pb2._CUSTOMERFEED
_CUSTOMERFEEDOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_customer__feed__pb2._CUSTOMERFEED
_CUSTOMERFEEDOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMERFEEDOPERATION.fields_by_name['create'])
_CUSTOMERFEEDOPERATION.fields_by_name['create'].containing_oneof = _CUSTOMERFEEDOPERATION.oneofs_by_name['operation']
_CUSTOMERFEEDOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMERFEEDOPERATION.fields_by_name['update'])
_CUSTOMERFEEDOPERATION.fields_by_name['update'].containing_oneof = _CUSTOMERFEEDOPERATION.oneofs_by_name['operation']
_CUSTOMERFEEDOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMERFEEDOPERATION.fields_by_name['remove'])
_CUSTOMERFEEDOPERATION.fields_by_name['remove'].containing_oneof = _CUSTOMERFEEDOPERATION.oneofs_by_name['operation']
_MUTATECUSTOMERFEEDSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATECUSTOMERFEEDSRESPONSE.fields_by_name['results'].message_type = _MUTATECUSTOMERFEEDRESULT
_MUTATECUSTOMERFEEDRESULT.fields_by_name['customer_feed'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_customer__feed__pb2._CUSTOMERFEED
DESCRIPTOR.message_types_by_name['GetCustomerFeedRequest'] = _GETCUSTOMERFEEDREQUEST
DESCRIPTOR.message_types_by_name['MutateCustomerFeedsRequest'] = _MUTATECUSTOMERFEEDSREQUEST
DESCRIPTOR.message_types_by_name['CustomerFeedOperation'] = _CUSTOMERFEEDOPERATION
DESCRIPTOR.message_types_by_name['MutateCustomerFeedsResponse'] = _MUTATECUSTOMERFEEDSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCustomerFeedResult'] = _MUTATECUSTOMERFEEDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomerFeedRequest = _reflection.GeneratedProtocolMessageType('GetCustomerFeedRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMERFEEDREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.customer_feed_service_pb2'
  ,
  '__doc__': """Request message for [CustomerFeedService.GetCustomerFeed][google.ads.g
  oogleads.v6.services.CustomerFeedService.GetCustomerFeed].
  
  Attributes:
      resource_name:
          Required. The resource name of the customer feed to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GetCustomerFeedRequest)
  })
_sym_db.RegisterMessage(GetCustomerFeedRequest)

MutateCustomerFeedsRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerFeedsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERFEEDSREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.customer_feed_service_pb2'
  ,
  '__doc__': """Request message for [CustomerFeedService.MutateCustomerFeeds][google.a
  ds.googleads.v6.services.CustomerFeedService.MutateCustomerFeeds].
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose customer feeds are
          being modified.
      operations:
          Required. The list of operations to perform on individual
          customer feeds.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
      response_content_type:
          The response content type setting. Determines whether the
          mutable resource or just the resource name should be returned
          post mutation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomerFeedsRequest)
  })
_sym_db.RegisterMessage(MutateCustomerFeedsRequest)

CustomerFeedOperation = _reflection.GeneratedProtocolMessageType('CustomerFeedOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERFEEDOPERATION,
  '__module__' : 'google.ads.googleads_v6.proto.services.customer_feed_service_pb2'
  ,
  '__doc__': """A single operation (create, update, remove) on a customer feed.
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          customer feed.
      update:
          Update operation: The customer feed is expected to have a
          valid resource name.
      remove:
          Remove operation: A resource name for the removed customer
          feed is expected, in this format:
          ``customers/{customer_id}/customerFeeds/{feed_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CustomerFeedOperation)
  })
_sym_db.RegisterMessage(CustomerFeedOperation)

MutateCustomerFeedsResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerFeedsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERFEEDSRESPONSE,
  '__module__' : 'google.ads.googleads_v6.proto.services.customer_feed_service_pb2'
  ,
  '__doc__': """Response message for a customer feed mutate.
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomerFeedsResponse)
  })
_sym_db.RegisterMessage(MutateCustomerFeedsResponse)

MutateCustomerFeedResult = _reflection.GeneratedProtocolMessageType('MutateCustomerFeedResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERFEEDRESULT,
  '__module__' : 'google.ads.googleads_v6.proto.services.customer_feed_service_pb2'
  ,
  '__doc__': """The result for the customer feed mutate.
  
  Attributes:
      resource_name:
          Returned for successful operations.
      customer_feed:
          The mutated customer feed with only mutable fields after
          mutate. The field will only be returned when
          response\_content\_type is set to "MUTABLE\_RESOURCE".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomerFeedResult)
  })
_sym_db.RegisterMessage(MutateCustomerFeedResult)


DESCRIPTOR._options = None
_GETCUSTOMERFEEDREQUEST.fields_by_name['resource_name']._options = None
_MUTATECUSTOMERFEEDSREQUEST.fields_by_name['customer_id']._options = None
_MUTATECUSTOMERFEEDSREQUEST.fields_by_name['operations']._options = None

_CUSTOMERFEEDSERVICE = _descriptor.ServiceDescriptor(
  name='CustomerFeedService',
  full_name='google.ads.googleads.v6.services.CustomerFeedService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1318,
  serialized_end=1805,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomerFeed',
    full_name='google.ads.googleads.v6.services.CustomerFeedService.GetCustomerFeed',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMERFEEDREQUEST,
    output_type=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_customer__feed__pb2._CUSTOMERFEED,
    serialized_options=b'\202\323\344\223\0021\022//v6/{resource_name=customers/*/customerFeeds/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateCustomerFeeds',
    full_name='google.ads.googleads.v6.services.CustomerFeedService.MutateCustomerFeeds',
    index=1,
    containing_service=None,
    input_type=_MUTATECUSTOMERFEEDSREQUEST,
    output_type=_MUTATECUSTOMERFEEDSRESPONSE,
    serialized_options=b'\202\323\344\223\0027\"2/v6/customers/{customer_id=*}/customerFeeds:mutate:\001*\332A\026customer_id,operations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMERFEEDSERVICE)

DESCRIPTOR.services_by_name['CustomerFeedService'] = _CUSTOMERFEEDSERVICE

# @@protoc_insertion_point(module_scope)