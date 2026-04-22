import grpc
from shared import user_pb2, user_pb2_grpc

class ChatService:

    def __init__(self):
        # connect to User Service
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    def handle_chat(self, user_id: int):
        print("Calling User Service...")

        response = self.stub.GetUser(
            user_pb2.UserRequest(user_id=user_id)
        )

        return f"Hello {response.name}, how can I help you?"


# simple test run
if __name__ == "__main__":
    chat = ChatService()

    result = chat.handle_chat(101)
    print(result)