import json
import logging

import grpc
from google.protobuf.empty_pb2 import (
    Empty
)

from app.crud import ProfessionCRUD
from app.grpc_generated_files.course_types_pb2 import (
    ProfessionMessage,
    ListProfessionsResponse
)
from .base_helper import BaseHelper


class ProfessionHelper(BaseHelper):

    @classmethod
    async def list_professions(cls, context, page_number, page_size, order_by, desc):
        try:
            professions, pagination = await ProfessionCRUD.get_paginated_list(context, page_number=page_number,
                                                                              page_size=page_size,
                                                                              order_by=order_by, desc=desc)
            professions_resp = [await cls.get_profession(context, profession.id) for profession in professions]
            return ListProfessionsResponse(page_number=pagination.page_number, page_size=pagination.page_size,
                                           num_pages=pagination.num_pages, total_results=pagination.total_results,
                                           results=professions_resp)
        except Exception as e:
            logging.error(e)
            await context.abort(grpc.StatusCode.INTERNAL, "Internal server error")

    @classmethod
    async def get_profession(cls, context, obj_id):
        try:
            profession = await ProfessionCRUD.get(context, obj_id=obj_id)
            profession_resp = ProfessionMessage(id=profession.id, title=json.dumps(profession.title),
                                                desc=json.dumps(profession.desc), is_active=profession.is_active,
                                                sort=profession.sort, slug=profession.slug,
                                                created_at=cls.get_timestamp_or_none(profession, 'created_at'),
                                                updated_at=cls.get_timestamp_or_none(profession, 'updated_at'))
            return profession_resp
        except Exception as e:
            logging.error(e)
            await context.abort(grpc.StatusCode.INTERNAL, "Internal server error")

    @classmethod
    async def create_profession(cls, context, valid_data):
        try:
            profession = await ProfessionCRUD.create(context, title=valid_data.title,
                                                     desc=valid_data.desc, slug=valid_data.slug)
            print(profession)
            profession_resp = ProfessionMessage(id=profession.id, title=json.dumps(profession.title),
                                                desc=json.dumps(profession.desc), sort=profession.sort,
                                                slug=profession.slug,
                                                created_at=cls.get_timestamp_or_none(profession, 'created_at'))
            return profession_resp
        except Exception as e:
            logging.error(e)
            await context.abort(grpc.StatusCode.INTERNAL, "Internal server error")

    @classmethod
    async def update_profession(cls, context, obj_id, updated_obj, mask):
        try:
            original_obj = await ProfessionCRUD.get(context, obj_id=obj_id)
            mask.MergeMessage(updated_obj, original_obj)
            profession = await ProfessionCRUD.update(context, original_obj)

            profession_resp = ProfessionMessage(id=profession.id, title=json.dumps(profession.title),
                                                desc=json.dumps(profession.desc), slug=profession.slug,
                                                sort=profession.sort, is_active=profession.is_active,
                                                created_at=cls.get_timestamp_or_none(profession, 'created_at'),
                                                updated_at=cls.get_timestamp_or_none(profession, 'updated_at'))
            return profession_resp
        except Exception as e:
            logging.error(e)
            await context.abort(grpc.StatusCode.INTERNAL, "Internal server error")

    @classmethod
    async def delete_profession(cls, context, obj_id):
        try:
            obj = await ProfessionCRUD.get(context, obj_id=obj_id)
            await ProfessionCRUD.delete(context, obj_id=obj.id)
            return Empty()
        except Exception as e:
            logging.error(e)
            await context.abort(grpc.StatusCode.INTERNAL, "Internal server error")
