# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: course.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import course_types_pb2 as course__types__pb2
from . import tag_types_pb2 as tag__types__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ourse.proto\x1a\x12\x63ourse_types.proto\x1a\x0ftag_types.proto\x1a\x1bgoogle/protobuf/empty.proto2\xa0\x06\n\rCourseService\x12^\n\x0fListProfessions\x12$.course_types.ListProfessionsRequest\x1a%.course_types.ListProfessionsResponse\x12T\n\rGetProfession\x12\".course_types.GetProfessionRequest\x1a\x1f.course_types.ProfessionMessage\x12`\n\x10\x43reateProfession\x12+.course_types.CreateUpdateProfessionRequest\x1a\x1f.course_types.ProfessionMessage\x12Z\n\x10UpdateProfession\x12%.course_types.UpdateProfessionRequest\x1a\x1f.course_types.ProfessionMessage\x12Q\n\x10\x44\x65leteProfession\x12%.course_types.DeleteProfessionRequest\x1a\x16.google.protobuf.Empty\x12\x43\n\x08ListTags\x12\x1a.tag_types.ListTagsRequest\x1a\x1b.tag_types.ListTagsResponse\x12\x39\n\x06GetTag\x12\x18.tag_types.GetTagRequest\x1a\x15.tag_types.TagMessage\x12\x45\n\tCreateTag\x12!.tag_types.CreateUpdateTagRequest\x1a\x15.tag_types.TagMessage\x12?\n\tUpdateTag\x12\x1b.tag_types.UpdateTagRequest\x1a\x15.tag_types.TagMessage\x12@\n\tDeleteTag\x12\x1b.tag_types.DeleteTagRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'course_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COURSESERVICE._serialized_start=83
  _COURSESERVICE._serialized_end=883
# @@protoc_insertion_point(module_scope)
