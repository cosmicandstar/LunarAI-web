from django.apps import AppConfig
import zmq


class StreamingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'streaming'

    context = zmq.Context()

    send_socket = context.socket(zmq.PUB)
    send_socket.bind('tcp://*:6000')
