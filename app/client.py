"""
Example of client on Python.
"""

import grpc

import app.definitions.builds.service_pb2 as service_pb2
import app.definitions.builds.service_pb2_grpc as service_pb2_grpc
from app.utils.logger import logger as log


def main(task_count: int) -> service_pb2.TaskResponse:
    """
    main
        Execute functionality of client on Python.

    Args:
        task_count (int)

    Returns:
        service_pb2.TaskResponse
            task: str
            error: bool
    """

    with grpc.insecure_channel("localhost:8080") as channel:
        client = service_pb2_grpc.TaskStub(channel)

        log.debug("Client is ready...")

        request = service_pb2.TaskRequest(task_count=task_count)
        response = client.GetTask(request)

        log.debug("Get response from server...")

        return response


if __name__ == "__main__":
    log.debug(f"Get task: {main(2)}")
