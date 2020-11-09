# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import asset_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_asset__pb2
from google.ads.google_ads.v6.proto.services import asset_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2


class AssetServiceStub(object):
    """Proto file describing the Asset service.

    Service to manage assets. Asset types can be created with AssetService are
    YoutubeVideoAsset, MediaBundleAsset and ImageAsset. TextAsset should be
    created with Ad inline.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAsset = channel.unary_unary(
                '/google.ads.googleads.v6.services.AssetService/GetAsset',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.GetAssetRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_asset__pb2.Asset.FromString,
                )
        self.MutateAssets = channel.unary_unary(
                '/google.ads.googleads.v6.services.AssetService/MutateAssets',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsResponse.FromString,
                )


class AssetServiceServicer(object):
    """Proto file describing the Asset service.

    Service to manage assets. Asset types can be created with AssetService are
    YoutubeVideoAsset, MediaBundleAsset and ImageAsset. TextAsset should be
    created with Ad inline.
    """

    def GetAsset(self, request, context):
        """Returns the requested asset in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateAssets(self, request, context):
        """Creates assets. Operation statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AssetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAsset': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAsset,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.GetAssetRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_asset__pb2.Asset.SerializeToString,
            ),
            'MutateAssets': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateAssets,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.AssetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AssetService(object):
    """Proto file describing the Asset service.

    Service to manage assets. Asset types can be created with AssetService are
    YoutubeVideoAsset, MediaBundleAsset and ImageAsset. TextAsset should be
    created with Ad inline.
    """

    @staticmethod
    def GetAsset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AssetService/GetAsset',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.GetAssetRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_asset__pb2.Asset.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateAssets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AssetService/MutateAssets',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
