
class Conversations():
    def __init__(self):
        self.conversations = []

    def to_dict(self):

        serializeable_list = []

        for conversation in self.conversations:
            serializeable_list.append(conversation.to_dict())

        return {"conversations": serializeable_list}
    
    @classmethod
    def from_dict(cls, data):
        conversations = cls()
        conversations.conversations = data['conversations']
        return conversations