import grpc
from concurrent import futures

from shared import user_pb2, user_pb2_grpc


class UserService(user_pb2_grpc.UserServiceServicer):

    def GetUser(self, request, context):
        print("UserService hit:", request.user_id)

        # fake DB
        return user_pb2.UserResponse(
            name=f"User_{request.user_id}"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserService(), server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    print("User Service running on 50051")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()