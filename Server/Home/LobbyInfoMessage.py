from Utils.Writer import Writer
from datetime import datetime
import random
class LobbyInfoMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23457
        self.player = player

    def encode(self):
        now = datetime.now()
        ping = random.randint(19,33)
        self.writeVint(0)#\nPlayer Online: {self.count}
        self.writeString(f'RiseBrawl v28.189-Private Servers\nWebsite: https://risebunny.github.io/brawl\nDiscord: https://dsc.gg/risebunny\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        self.writeVint(0)