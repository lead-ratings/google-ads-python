# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import currency_constant_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_currency__constant__pb2
from google.ads.google_ads.v6.proto.services import currency_constant_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_currency__constant__service__pb2


class CurrencyConstantServiceStub(object):
    """Service to fetch currency constants.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCurrencyConstant = channel.unary_unary(
                '/google.ads.googleads.v6.services.CurrencyConstantService/GetCurrencyConstant',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_currency__constant__service__pb2.GetCurrencyConstantRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_currency__constant__pb2.CurrencyConstant.FromString,
                )


class CurrencyConstantServiceServicer(object):
    """Service to fetch currency constants.
    """

    def GetCurrencyConstant(self, request, context):
        """Returns the requested currency constant.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CurrencyConstantServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCurrencyConstant': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrencyConstant,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_currency__constant__service__pb2.GetCurrencyConstantRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_currency__constant__pb2.CurrencyConstant.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.CurrencyConstantService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CurrencyConstantService(object):
    """Service to fetch currency constants.
    """

    @staticmethod
    def GetCurrencyConstant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CurrencyConstantService/GetCurrencyConstant',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_currency__constant__service__pb2.GetCurrencyConstantRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_currency__constant__pb2.CurrencyConstant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
