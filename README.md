# localstack with keda scaledJob sample
only queue-consumer + batch_jobs.yaml works now.

# run on ubuntu 20.04

requirement:

1. minikube + docker with sudo access
2. kubectl
3. helm install localstack and setup.
4. build docker image in queu_consumer folder.
```bash
docker build <image repo>/<image name>
# also can use vfive/py-aws-boto3:latest 
```
5. set parallelism to 1 in localstack

todo:
- redis and amq
- keda jobs