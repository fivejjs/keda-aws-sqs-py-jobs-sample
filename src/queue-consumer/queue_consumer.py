import logging
import sys

import boto3
import time

logger = logging.getLogger(__name__)

endpoint_url = 'http://192.168.49.2:31566'
queue_name = 'crop-mask-dev'
sqs = boto3.resource('sqs', endpoint_url=endpoint_url, region_name='ap-southeast-2')
queue = sqs.get_queue_by_name(QueueName=queue_name)

print(queue.url)


def count_message():
    queue.load()
    return int(queue.attributes['ApproximateNumberOfMessages'])


def main():
    while count_message():
        messages = queue.receive_messages()
        for m in messages:
            print(m.body)
            m.delete()
            time.sleep(10)
    print('!done the queue!')
    return 0


if __name__ == '__main__':
    sys.exit(main())
