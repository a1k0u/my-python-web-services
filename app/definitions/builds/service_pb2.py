# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"!\n\x0bTaskRequest\x12\x12\n\ntask_count\x18\x01 \x01(\x05\"+\n\x0cTaskResponse\x12\x0c\n\x04task\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\x08\x32.\n\x04Task\x12&\n\x07GetTask\x12\x0c.TaskRequest\x1a\r.TaskResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TASKREQUEST._serialized_start=17
  _TASKREQUEST._serialized_end=50
  _TASKRESPONSE._serialized_start=52
  _TASKRESPONSE._serialized_end=95
  _TASK._serialized_start=97
  _TASK._serialized_end=143
# @@protoc_insertion_point(module_scope)
