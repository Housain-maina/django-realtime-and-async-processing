from channels.generic.websocket import AsyncWebsocketConsumer


class QuizConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('quiz', self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('quiz', self.channel_name)

    async def send_quiz(self, event):
        text_message = event['text']
        await self.send(text_message)
