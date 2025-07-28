from conversation import Conversation


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

        deserialized_list = []

        for conversation in data['conversations']:
            deserialized_list.append(Conversation.from_dict(conversation))

        conversations.conversations = deserialized_list
        return conversations
    
    def find_conversation_index(self, header):

        try:
        
            for conversation in self.conversations:
                if conversation.header == header:
                    return self.conversations.index(conversation)
                
        except ValueError:

            return None