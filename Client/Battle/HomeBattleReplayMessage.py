from Server.Battle.BattleLogMessage import BattleLogMessage
from Utils.Reader import BSMessageReader


class HomeBattleReplayMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        BattleLogMessage(self.client, self.player).send()