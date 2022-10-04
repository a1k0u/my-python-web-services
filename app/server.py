"""

"""

import logging

from concurrent.futures import ThreadPoolExecutor
import grpc


from definitions.builds.service_pb2_grpc import TaskServicer
from definitions.builds.service_pb2_grpc import add_TaskServicer_to_server
import definitions.builds.service_pb2 as service_pb2
from questions.questions import questions


def __validate_data(task_count) -> bool:
    if not (0 <= task_count < len(questions)):
        return False
    return True


def __get_task(task_count: int) -> str:
    return questions[task_count // 2]


class Service(TaskServicer):
    def GetTask(self, request, context):
        response = service_pb2.TaskResponse()
        response.error = 1
        response.task = "abac"
        print(1)
        return response


def run_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TaskServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:8080")
    server.start()

    logging.debug("The server is up and running ...")

    server.wait_for_termination()


if __name__ == "__main__":
    run_server()
