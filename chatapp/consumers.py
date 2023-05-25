import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import ChatMessage

class Consumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        media = text_data_json.get('media', '')

        print('Media: ==> ', media, '\nMessage: ==>', message)

        # Save the received data to the database
        chat_message = ChatMessage.objects.create(message=message, media=media)
        chat_message.save()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'media': media,
            }
        )

    def chat_message(self, event):
        message = event.get('message', '')
        media = event.get('media', '')

        data = {}
        if message:
            data['message'] = message
        if media:
            data['media'] = media

        self.send(text_data=json.dumps(data))
