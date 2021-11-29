import time

from protobuf import message_pb2
from messages.base import Base

class RoomUserSeqMessage(Base):
    def __init__(self):
        self.instance = message_pb2.RoomUserSeqMessage()

    def format_content(self):
        return self.instance.totalUserStr

    def __str__(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【观看人数】' + self.format_content()