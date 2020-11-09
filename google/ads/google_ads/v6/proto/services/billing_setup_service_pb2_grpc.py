# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import billing_setup_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_billing__setup__pb2
from google.ads.google_ads.v6.proto.services import billing_setup_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2


class BillingSetupServiceStub(object):
    """Proto file describing the BillingSetup service.

    A service for designating the business entity responsible for accrued costs.

    A billing setup is associated with a payments account.  Billing-related
    activity for all billing setups associated with a particular payments account
    will appear on a single invoice generated monthly.

    Mutates:
    The REMOVE operation cancels a pending billing setup.
    The CREATE operation creates a new billing setup.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBillingSetup = channel.unary_unary(
                '/google.ads.googleads.v6.services.BillingSetupService/GetBillingSetup',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.GetBillingSetupRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_billing__setup__pb2.BillingSetup.FromString,
                )
        self.MutateBillingSetup = channel.unary_unary(
                '/google.ads.googleads.v6.services.BillingSetupService/MutateBillingSetup',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.MutateBillingSetupRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.MutateBillingSetupResponse.FromString,
                )


class BillingSetupServiceServicer(object):
    """Proto file describing the BillingSetup service.

    A service for designating the business entity responsible for accrued costs.

    A billing setup is associated with a payments account.  Billing-related
    activity for all billing setups associated with a particular payments account
    will appear on a single invoice generated monthly.

    Mutates:
    The REMOVE operation cancels a pending billing setup.
    The CREATE operation creates a new billing setup.
    """

    def GetBillingSetup(self, request, context):
        """Returns a billing setup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateBillingSetup(self, request, context):
        """Creates a billing setup, or cancels an existing billing setup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BillingSetupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBillingSetup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBillingSetup,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.GetBillingSetupRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_billing__setup__pb2.BillingSetup.SerializeToString,
            ),
            'MutateBillingSetup': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateBillingSetup,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.MutateBillingSetupRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.MutateBillingSetupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.BillingSetupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BillingSetupService(object):
    """Proto file describing the BillingSetup service.

    A service for designating the business entity responsible for accrued costs.

    A billing setup is associated with a payments account.  Billing-related
    activity for all billing setups associated with a particular payments account
    will appear on a single invoice generated monthly.

    Mutates:
    The REMOVE operation cancels a pending billing setup.
    The CREATE operation creates a new billing setup.
    """

    @staticmethod
    def GetBillingSetup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.BillingSetupService/GetBillingSetup',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.GetBillingSetupRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_billing__setup__pb2.BillingSetup.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateBillingSetup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.BillingSetupService/MutateBillingSetup',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.MutateBillingSetupRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_billing__setup__service__pb2.MutateBillingSetupResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
