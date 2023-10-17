import json
import pika
from pika import exceptions
from sendmail import SendEmail
import os

file_path = os.path.join(os.path.dirname(__file__), 'backendcred.json')
# with open('backendcred.json', "r") as cred:
dlog_cred = json.load(open(file_path))

mail_path = os.path.join(os.path.dirname(__file__), 'mailformat.json')
mail_format = json.load(open(mail_path))

qurl = dlog_cred.get("RABBIT_MQ_CRED").get("QUEUE_PROCESS")
backend_exchange = "test"


def mail_task(task: str, data: dict):
    mail_tasks = {
        'test': test_mail
    }
    res = mail_tasks[task](data)
    return True


def test_mail(data: dict):
    try:
        process = SendEmail(to=data.get('email'))
        process.test_mail(data.get('email'), data.get('name'))
        process.send()
        return "Test: Requested OTP for {}".format(data.get('email'))
    except Exception as e:
        pass



def ex_task(task, data):
    res =mail_task(task, data)
    return True if res else False


def callback(channel, method, properties, body):
    try:
        if body != '':
            data = json.loads(body.decode("utf-8"))
            print(data, "data")
            metadata = data.get("_metadata")  # if data need to send only to the enterprice user them make use of this.
            task = data.get("task")
            payload = data.get('data')
            if task and data:
                try:
                    if ex_task(task, payload):
                        channel.basic_ack(method.delivery_tag)
                    else:
                        channel.basic_ack(method.delivery_tag)
                except Exception as e:
                    channel.basic_ack(method.delivery_tag)
            else:
                channel.basic_ack(method.delivery_tag)
        else:
            channel.basic_ack(method.delivery_tag)
    except Exception:
        pass


def main():
    try:
        type_ = "direct"
        queue = "hello"
        key = "hello"
        credentials = pika.URLParameters(qurl)
        connection = pika.BlockingConnection(credentials)
        channel = connection.channel()
        channel.confirm_delivery()
        channel.exchange_declare(exchange=backend_exchange, exchange_type=type_, durable=True)
        channel.queue_declare(queue=queue, durable=False)
        channel.queue_bind(exchange=backend_exchange, queue=queue, routing_key=key)
        channel.basic_consume(queue, callback, auto_ack=False)
        channel.start_consuming()
    except Exception as e:
        pass
