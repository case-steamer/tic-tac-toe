from PIL import Image

class Player:
    name: str
    avatar: Image
    cells: list
    status: str

    def __init__(self, name: str, avatar:Image, status:str):
        self.name = name
        self.avatar = avatar
        self.cells = []
        self.status = status