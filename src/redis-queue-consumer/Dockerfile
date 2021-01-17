FROM python

WORKDIR /app

RUN pip install boto3

COPY ../queue-consumer/queue_consumer.py /app

CMD ["python", "queue_consumer.py"]
