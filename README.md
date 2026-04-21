# demo_microservice_project
demo micro service project which in we going to learn how a micro service project works.

project_root/
│
├── api_gateway/
├── chat_service/
├── user_service/
├── proto/
└── shared/

---------------------------------------------------------------------------------------------------

- python -m grpc_tools.protoc -I./proto --python_out=./shared --grpc_python_out=./shared ./proto/user.proto