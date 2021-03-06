# import os
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
# props = queue.get_queue_properties()
#
# print(props)

import boto3

endpoint_url = 'http://192.168.49.2:31566'
queue_name = 'crop-mask-dev'
sqs = boto3.resource('sqs', endpoint_url=endpoint_url)
queue = sqs.get_queue_by_name(QueueName=queue_name)
qnum = int(queue.attributes['ApproximateNumberOfMessages'])
print(f'number of messages: {qnum}')
