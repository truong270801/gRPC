import tkinter as tk
from tkinter import messagebox
import grpc
import sys
import os
proto_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../protobuf'))
sys.path.insert(0, proto_path)
from point_service_pb2 import PointRequest, Empty
import point_service_pb2_grpc
from dotenv import load_dotenv
import os

load_dotenv()

channel = grpc.insecure_channel('localhost:50051')
stub = point_service_pb2_grpc.PointServiceStub(channel)

def add_points():
    user_id = userIdAdd.get()
    points = int(pointsToAdd.get())
    try:
        response = stub.AddPoints(PointRequest(user_id=user_id, points=points))
        messagebox.showinfo("Success", f"Added {points} points to User {response.user_id}. Total Points: {response.total_points}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add points: {str(e)}")

def subtract_points():
    user_id = userIdAdd.get()
    points = int(pointsToAdd.get())
    try:
        response = stub.SubtractPoints(PointRequest(user_id=user_id, points=points))
        messagebox.showinfo("Success", f"Subtracted {points} points from User {response.user_id}. Total Points: {response.total_points}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to subtract points: {str(e)}")

def get_users():
    try:
        response = stub.GetUsers(Empty())
        user_list = "\n".join([f"User: {user.user_id}, Total Points: {user.total_points}" for user in response.users])
        messagebox.showinfo("User List", user_list)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch user list: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Point Management")

# Add Points Frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(side=tk.LEFT, padx=10)

label_add = tk.Label(frame, text="Point Management", font=("Helvetica", 16))
label_add.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(frame, text="User ID").grid(row=1, column=0, sticky='w')
userIdAdd = tk.Entry(frame)
userIdAdd.grid(row=1, column=1)

tk.Label(frame, text="Points").grid(row=2, column=0, sticky='w')
pointsToAdd = tk.Entry(frame)
pointsToAdd.grid(row=2, column=1)

addButton = tk.Button(frame, text="Add Points", command=add_points)
addButton.grid(row=3, column=0, columnspan=1, pady=3)

subtractButton = tk.Button(frame, text="Subtract Points", command=subtract_points)
subtractButton.grid(row=3, column=1, columnspan=1, pady=3)

listButton = tk.Button(frame, text="Get User List", command=get_users)
listButton.grid(row=3, column=2, columnspan=2, pady=3)

root.mainloop()