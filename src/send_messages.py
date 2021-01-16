# import os
# import sys
# import time
# from azure.storage.queue import QueueClient
#
# try:
#   connection_string = os.environ['AzureWebJobsStorage']
#   queue_name = os.environ['QUEUE_NAME']
# except KeyError:
#   print('Error: missing environment variable AzureWebJobsStorage or QUEUE_NAME')
#   exit(1)
#
# queue = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queue_name)
#
# for message in range(0, int(sys.argv[1])):
#   queue.send_message(content='foo_'+str(message))

import boto3
import json

endpoint_url = 'http://192.168.49.2:31566'
queue_name = 'crop-mask-dev'
sqs = boto3.resource('sqs', endpoint_url=endpoint_url)
queue = sqs.get_queue_by_name(QueueName=queue_name)
qnum = 10

for i in range(qnum):
    message = json.dumps({'name': f'm{i}', 'value': i})
    queue.send_message(MessageBody=message)
print('done!')
