import zmq
import json
from json_csv import create_csv

environment = zmq.Context()
replySocket = environment.socket(zmq.REP)
replySocket.bind("tcp://*:5564") #confirm its available 
print("Listening for messages ...")
#wait for message from program

while True:
    message = replySocket.recv_json()
    print("Request recieved")


    data = json.loads(message)
    
    plan = data['plan']
    plan_time = data['plan_time']
    plan_name = data['plan_name']
    allocated_time = data['allocated_time']

    if not plan or not plan_time or not plan_name or not allocated_time:
        response_message = {"Error": 'Missing variables'}

    else:
        response_data = create_csv(plan_name, plan, plan_time, allocated_time)
        response_message = {"Success": response_data}

        
        
    
    replySocket.send_json(response_message)