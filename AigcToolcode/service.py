#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from loguru import logger
import grpc
from concurrent import futures
import chatgbt
import proto.aigc_tool_pb2_grpc as proto
from proto import aigc_tool_pb2


class Service(proto.AigcServiceServicer):

    def ChatApi(self, request, context):
        logger.info('ChatApi start to process request:{request}', request=request)
        usage, result = chatgbt.text_call(request.content, request.apiKey)
        return aigc_tool_pb2.ChatApiRes(code=0, message="success", content=result, usage=usage)

        # return api_pb2.UserReply(message='success', data=users)


def serve():
    logger.debug('start python grpc server====>')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto.add_AigcServiceServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:8100')
    server.start()
    logger.info('ai_prom server start :8100', type(server))
    server.wait_for_termination()


if __name__ == '__main__':
    logger.add("file.log", format="{time} {level} {message}", filter="")
    serve()
