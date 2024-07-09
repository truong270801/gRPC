import grpc
import point_service_pb2
import point_service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = point_service_pb2_grpc.PointServiceStub(channel)

    # Thêm điểm cho người dùng 1
    response = stub.AddPoints(point_service_pb2.PointRequest(user_id="user1", points=10))
    print(f"User: {response.user_id}, Total Points: {response.total_points}")

    # Thêm điểm cho người dùng 2
    response = stub.AddPoints(point_service_pb2.PointRequest(user_id="user2", points=20))
    print(f"User: {response.user_id}, Total Points: {response.total_points}")

  # Trừ điểm cho người dùng 2
    response = stub.SubtractPoints(point_service_pb2.PointRequest(user_id="user2", points=10))
    print(f"User: {response.user_id}, Total Points: {response.total_points}")
    
    # Trừ điểm cho người dùng 1
    response = stub.SubtractPoints(point_service_pb2.PointRequest(user_id="user1", points=5))
    print(f"User: {response.user_id}, Total Points: {response.total_points}")

    # Lấy danh sách người dùng
    response = stub.GetUsers(point_service_pb2.Empty())
    for user in response.users:
        print(f"User: {user.user_id}, Total Points: {user.total_points}")

if __name__ == '__main__':
    run()
