<img align="right" width="130" height="130" src="https://user-images.githubusercontent.com/22943366/175839311-833c917e-b70c-49a3-bdad-79baeb26e40d.jpg">

# Fiend's Gate

> Opens 2 portals, one next to the origin queue and one in the target queue. Messages can channel a portal to teleport to the other side. JSON text that pass through the portal temporarily gain Damage Reduction and Movement Speed. Portals have to be at least 2000 away from each other.

Simple script to handle sqs messages without deleting them.

## How does it work?

The script tries to poll messages, until it reaches the maximum number of empty receives, or it reaches at least the declared number of messages.

```
python3 get_messages.py <declared_number_of_messages>
```

The `declared_number_of_messages` should be an integer, and it's an optional argument.

Afterwards, the payloads are saved as json file at `/messages` directory.
It only works for json body.

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
