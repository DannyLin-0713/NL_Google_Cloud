#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64

while True:
    AuthoID=input("\033[1;33;40m Please input your autho ID \033[0m \n")
    f_open=input("\033[1;33;40m Please input the doc name with the content you want to analyze the emotion \033[0m \n")
    file_t=open('./'+f_open,'r+')
    file_tt=file_t.readline()

    url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + AuthoID
    headers = {'content-type': 'application/json'}
    requestData={
          "document":{
              "language":"en-US",
              "content":file_tt,
              "type":"PLAIN_TEXT"
              }
          }
    after_call = requests.post(url, json=requestData, headers=headers)
    text=json.loads(after_call.text)
    print ("\033[1;32;40m \nEmotion-Positivity of this text is \033[0m")

    if after_call.status_code == 200:
        print(text['documentSentiment']['score'])
    else:
        print("error, pls check the file or your autho id")
        print (text)
    print ("\n New Search")
