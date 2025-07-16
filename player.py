from PIL import Image

class Player:
    name: str
    avatar: Image

    def __init__(self, name: str, avatar:Image):
        self.name = name
        self.avatar = avatar