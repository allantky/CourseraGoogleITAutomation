#!/usr/bin/env python3
import os
import requests

external_ip = "34.72.142.92"
feedback_dir = r"/data/feedback"

for file in os.listdir(feedback_dir):
    if file.endswith(".txt"):
        #print(file)
        review_dict = {}
        #print(os.path.join(feedback_dir, file))
        with open(os.path.join(feedback_dir, file), 'r') as fh:
            review_dict["title"] = fh.readline().strip()
            review_dict["name"] = fh.readline().strip()
            review_dict["date"] = fh.readline().strip()
            review_dict["feedback"] = fh.readline().strip()
        #print(review_dict)
        response = requests.post('http://' + external_ip + '/feedback/', json=review_dict)
        response.raise_for_status()
        if response.status_code == 201:
            print("response: POST success")
            #print(response.request.url)
            #print(response.request.body)
        else:
            raise Exception("response: POST failed with status code {}".format(response.status_code))
            #print(response.request.body)
