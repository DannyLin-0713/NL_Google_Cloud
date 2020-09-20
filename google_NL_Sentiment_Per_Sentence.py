#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64

while True:
    AuthoID=input("\033[1;33;40m Please input your autho ID \033[0m \n")
    f_open=input("\033[1;33;40m Please input the doc name with the content you want to analysis the emotion \033[0m \n")
    file_t=open('./'+f_open,'r+')
    file_tt=file_t.readline().strip()

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
    paragum=int(0)
    paragum_1=len(['sentences'][0])
    print ("\033[1;32;40m \nEmotion-Positivity of this text is \033[0m")
    
    def who_sco():
        print('\033[1;32;40m the average positivity-score is \033[0m')
        print(text['documentSentiment']['score'])
        print('\033[1;32;40m the average strong-level of emotion in whole text is \033[0m')
        print(text['documentSentiment']['magnitude'])
        print('\n')

    def sen_sco():
        print('\033[1;32;40m sentence \033[0m:')
        print(text['sentences'][paragum]['text']['content'])
        print('\033[1;32;40m positivity-score: \033[0m')
        print(text['sentences'][paragum]['sentiment']['score'])

    who_sco()
    
    while paragum < paragum_1:
        if after_call.status_code == 200:
            sen_sco()
            paragum = paragum + 1
        else:
            print("error, pls check the file or your autho id")
            print (text)
    print ("\n New Search")
