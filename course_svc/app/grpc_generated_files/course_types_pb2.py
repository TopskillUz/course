# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: course_types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x63ourse_types.proto\x12\x0c\x63ourse_types\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/protobuf/field_mask.proto\"\xfb\x01\n\x11ProfessionMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x11\n\tis_active\x18\x04 \x01(\x08\x12\x0c\n\x04sort\x18\x05 \x01(\x05\x12\x0c\n\x04slug\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x16ProfessionShortMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"&\n\x14GetProfessionRequest\x12\x0e\n\x06obj_id\x18\x01 \x01(\x05\"k\n\x1d\x43reateUpdateProfessionRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\x12\x0c\n\x04sort\x18\x04 \x01(\x05\x12\x0c\n\x04slug\x18\x05 \x01(\t\"`\n\x16ListProfessionsRequest\x12\x13\n\x0bpage_number\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x10\n\x08order_by\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\x08\"\x94\x01\n\x17UpdateProfessionRequest\x12\x0e\n\x06obj_id\x18\x01 \x01(\x03\x12?\n\nprofession\x18\x02 \x01(\x0b\x32+.course_types.CreateUpdateProfessionRequest\x12(\n\x04mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x9d\x01\n\x17ListProfessionsResponse\x12\x13\n\x0bpage_number\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x11\n\tnum_pages\x18\x03 \x01(\x05\x12\x15\n\rtotal_results\x18\x04 \x01(\x05\x12\x30\n\x07results\x18\x05 \x03(\x0b\x32\x1f.course_types.ProfessionMessage\")\n\x17\x44\x65leteProfessionRequest\x12\x0e\n\x06obj_id\x18\x01 \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'course_types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROFESSIONMESSAGE._serialized_start=104
  _PROFESSIONMESSAGE._serialized_end=355
  _PROFESSIONSHORTMESSAGE._serialized_start=357
  _PROFESSIONSHORTMESSAGE._serialized_end=407
  _GETPROFESSIONREQUEST._serialized_start=409
  _GETPROFESSIONREQUEST._serialized_end=447
  _CREATEUPDATEPROFESSIONREQUEST._serialized_start=449
  _CREATEUPDATEPROFESSIONREQUEST._serialized_end=556
  _LISTPROFESSIONSREQUEST._serialized_start=558
  _LISTPROFESSIONSREQUEST._serialized_end=654
  _UPDATEPROFESSIONREQUEST._serialized_start=657
  _UPDATEPROFESSIONREQUEST._serialized_end=805
  _LISTPROFESSIONSRESPONSE._serialized_start=808
  _LISTPROFESSIONSRESPONSE._serialized_end=965
  _DELETEPROFESSIONREQUEST._serialized_start=967
  _DELETEPROFESSIONREQUEST._serialized_end=1008
# @@protoc_insertion_point(module_scope)