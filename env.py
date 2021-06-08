import config

class Env:
    def __init__(self, client, message):
        self.client = client
        self.message = message
        self.args = message.content[len(config.PREFIX): ].lower().split()