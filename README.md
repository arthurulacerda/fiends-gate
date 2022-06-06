# poll-sqs-queue

Simple script to retrieve messages from an SQS queue, without deleting it.

## How does it work?

The script tries to poll messages, until it reaches the maximum number of empty receives, or it reaches at least the declared number of messages.

```
python3 get_messages.py <declared_number_of_messages>
```

The `declared_number_of_messages` should be an integer, and it's an optional argument.

Afterwards, the payloads are saved as json text file at `/messages` directory.

## Config

Set environment variables to configure the behaviour:

**VISIBILITY_TIMEOUT:** The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request.
**MAX_EMPTY_RECEIVES:** Maximum number of empty receives before stop polling messages.

```
export VISIBILITY_TIMEOUT=60
export MAX_EMPTY_RECEIVES=3
```

Set environment variables to connect to a specific queue:

```
export AWS_REGION_NAME=''
export AWS_ACCESS_KEY_ID=''
export AWS_SECRET_ACCESS_KEY=''
export AWS_SESSION_TOKEN=''
export QUEUE_NAME_URL=''
```