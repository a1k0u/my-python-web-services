"""
Server which returns tasks for users.
"""

import grpc
from concurrent.futures import ThreadPoolExecutor

import app.definitions.builds.service_pb2 as service_pb2
import app.definitions.builds.service_pb2_grpc as service_pb2_grpc
from app.utils.logger import logger as log
from app.questions.questions import get_task


class Service(service_pb2_grpc.TaskServicer):
    def GetTask(
        self, request: service_pb2.TaskRequest, context
    ) -> service_pb2.TaskResponse:
        """
        GetTask
            Each user from the chat have to send a message,
            after that thier task will change.

        Information about how many messages they
        was sent in session storage in another server.

        Args:
            request (service_pb2.TaskRequest)
            context (_type_)

        Returns:
            service_pb2.TaskResponse
                task: str
                error: bool
        """

        log.debug("Get a request...")

        response = service_pb2.TaskResponse()
        response.task, response.error = get_task(request.task_count)

        log.debug("Response is done...")

        return response


def run_server():
    """
    run_server
        Starts server at localhost:8080.
    """

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_TaskServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:8080")
    server.start()

    log.debug("The server is up and running ...")

    server.wait_for_termination()
