import grpc
import sys
import os
from concurrent import futures
proto_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../protobuf'))
sys.path.insert(0, proto_path)
import point_service_pb2 
import point_service_pb2_grpc

class PointServiceServicer(point_service_pb2_grpc.PointServiceServicer):
    def __init__(self):
        self.users = {}

    def AddPoints(self, request, context):
        user_id = request.user_id
        points = request.points
        if user_id in self.users:
            self.users[user_id] += points
        else:
            self.users[user_id] = points
        return point_service_pb2.PointResponse(user_id=user_id, total_points=self.users[user_id])

    def SubtractPoints(self, request, context):
        user_id = request.user_id
        points = request.points
        if user_id in self.users:
            self.users[user_id] -= points
        else:
            self.users[user_id] = -points
        return point_service_pb2.PointResponse(user_id=user_id, total_points=self.users[user_id])

    def GetUsers(self, request, context):
        user_list = [point_service_pb2.User(user_id=user_id, total_points=points) for user_id, points in self.users.items()]
        return point_service_pb2.UserList(users=user_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    point_service_pb2_grpc.add_PointServiceServicer_to_server(PointServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
