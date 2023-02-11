import inspect
from typing import Optional

from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    extra_ctx: Optional[dict]

    @classmethod
    def get_context(cls, values: dict):
        extra_ctx = values.get('extra_ctx', None)
        if extra_ctx:
            return extra_ctx.get('context', None)
        return None


def optional(*fields):
    def dec(_cls):
        for field in fields:
            _cls.__fields__[field].required = False
        return _cls

    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], BaseModel):
        cls = fields[0]
        fields = cls.__fields__
        return dec(cls)
    return dec


class GetProfessionSchema(BaseSchema):
    obj_id: int


class CreateProfessionSchema(BaseSchema):
    title: str
    desc: Optional[str]
    is_active: Optional[bool] = Field(default=True)
    slug: Optional[str]
    sort: Optional[int]


class ListProfessionsSchema(BaseSchema):
    page_number: Optional[int] = Field(default=1)
    page_size: Optional[int] = Field(default=10)
    order_by: Optional[str] = Field(default='id')
    desc: Optional[bool] = Field(default=False)


class UpdateProfessionSchema(BaseSchema):
    obj_id: int
    profession: dict
    mask: str


class DeleteProfessionSchema(BaseSchema):
    obj_id: int
