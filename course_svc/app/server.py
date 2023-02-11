import asyncio
import logging
import sys
import grpc
from google.protobuf import json_format
from grpc import aio
from pydantic import ValidationError

from core.config import settings
from grpc_generated_files import course_pb2_grpc
from helpers import ProfessionHelper
from schemas import (
    CreateProfessionSchema, ListProfessionsSchema,
    UpdateProfessionSchema, GetProfessionSchema,
    DeleteProfessionSchema
)


class CourseServicer(course_pb2_grpc.CourseServiceServicer):
    async def ListProfessions(self, request, context):
        print("ListProfessions received request")
        data = json_format.MessageToDict(request, preserving_proto_field_name=True)
        try:
            valid_data = ListProfessionsSchema(**data)
        except ValidationError as exc:
            raise await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(exc))
        return await ProfessionHelper.list_professions(context, page_number=valid_data.page_number,
                                                       page_size=valid_data.page_size, order_by=valid_data.order_by,
                                                       desc=valid_data.desc)

    async def GetProfession(self, request, context):
        print("CourseServicer received request")
        data = json_format.MessageToDict(request, preserving_proto_field_name=True)
        data.update(extra_ctx={'context': context})
        try:
            valid_data = GetProfessionSchema(**data)
        except ValidationError as exc:
            raise await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(exc))
        return await ProfessionHelper.get_profession(context, valid_data.obj_id)

    async def CreateProfession(self, request, context):
        print("CourseServicer received request")
        data = json_format.MessageToDict(request, preserving_proto_field_name=True)
        data.update(extra_ctx={'context': context})
        try:
            validated_data = CreateProfessionSchema(**data)
        except ValidationError as exc:
            raise await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(exc))
        return await ProfessionHelper.create_profession(context, validated_data)

    async def UpdateProfession(self, request, context):
        print("CourseServicer received request")
        data = json_format.MessageToDict(request, preserving_proto_field_name=True)
        try:
            UpdateProfessionSchema(**data)
            return await ProfessionHelper.update_profession(context, obj_id=request.obj_id,
                                                            updated_obj=request.profession, mask=request.mask)
        except ValidationError as exc:
            raise await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(exc))

    async def DeleteProfession(self, request, context):
        print("CourseServicer received request")
        data = json_format.MessageToDict(request, preserving_proto_field_name=True)
        try:
            valid_data = DeleteProfessionSchema(**data)
            return await ProfessionHelper.delete_profession(context, obj_id=valid_data.obj_id)
        except ValidationError as exc:
            raise await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(exc))


async def serve():
    server = aio.server()
    listen_addr = f"[::]:{settings.SVC_PORT}"
    course_pb2_grpc.add_CourseServiceServicer_to_server(CourseServicer(), server)
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)

    await server.start()
    await server.wait_for_termination()


def write_log():
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('../debug.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)


if __name__ == '__main__':
    write_log()
    asyncio.run(serve())
