import boto3
import os
import json
import sys
from datetime import datetime

MAX_EMPTY_RECEIVES=int(os.getenv('MAX_EMPTY_RECEIVES'))
VISIBILITY_TIMEOUT=int(os.getenv('VISIBILITY_TIMEOUT'))

AWS_ACCESS_KEY_ID=os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN=os.getenv('AWS_SESSION_TOKEN')
AWS_REGION_NAME=os.getenv('AWS_REGION_NAME')

QUEUE_URL=os.getenv('QUEUE_NAME_URL')


if len(sys.argv) > 1:
    declared_number_of_messages = int(sys.argv[1])
else:
    declared_number_of_messages = 10000

time_now = datetime.now()
queue_name = QUEUE_URL.split("/")[-1]
file_prefix = "messages/"
file_name = file_prefix + time_now.strftime("%Y-%m-%d-%H-%M-%S-") + queue_name + ".json"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_NAME,
    aws_session_token=AWS_SESSION_TOKEN,
)
sqs_client = session.client('sqs')

all_messages = []
empty_receives = 0

while (empty_receives < MAX_EMPTY_RECEIVES and len(all_messages) < declared_number_of_messages):

    resp = sqs_client.receive_message(
        QueueUrl=QUEUE_URL,
        AttributeNames=['All'],
        VisibilityTimeout=VISIBILITY_TIMEOUT,
        MaxNumberOfMessages=10
    )

    try:
        all_messages += resp['Messages']
    except KeyError:
        print('Empty receive!')
        empty_receives += 1

all_body= list(map(lambda msg: json.loads(msg['Body']),all_messages))
f = open(file_name, "w")
f.write(json.dumps(all_body, indent=2))
f.close()

print("Messages retrieved: ", len(all_body))
print("Saved on ", file_name)