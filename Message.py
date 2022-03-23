class Message():
    def __init__(self, senderConnector, messageType, data, dis=0):
        self.senderConnector = senderConnector
        self.messageType = messageType
        self.data = data
        self.dis = dis
