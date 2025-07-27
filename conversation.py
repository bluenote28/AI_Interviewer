

class Conversation():
    def __init__(self):
        self.conversation = {"prompts": [], "answers": [] }
        self.header = ""
        self.introduction = ""


    def to_dict(self):

        return {"header": self.header, ""
        "introduction": self.introduction,
        "conversation": self.conversation }
    
    @classmethod
    def from_dict(cls, data):
        conversation = cls()
        conversation.header = data['header']
        conversation.introduction = data['introduction']
        conversation.conversation = data['conversation']
        return conversation