import logging
import grpc

import definitions.builds.service_pb2 as service_pb2
import definitions.builds.service_pb2_grpc as service_pb2_grpc


def main(task_count: int):
    with grpc.insecure_channel("localhost:8080") as channel:
        client = service_pb2_grpc.TaskStub(channel)
        request = service_pb2.TaskRequest(task_count=task_count)
        response = client.GetTask(request)

        return response


if __name__ == "__main__":
    logging.debug(f"Get the task: {main(3)}")
