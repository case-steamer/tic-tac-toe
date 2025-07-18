from PIL import Image
from tkinter import Canvas

class Player:
    name: str
    avatar: Image
    cells: list
    status: str
    score: int

    def __init__(self, name: str, avatar:Image, status:str):
        self.name = name
        self.avatar = avatar
        self.cells = []
        self.status = status
        self.score = 0

    def update(self):
        text = self.name + ': ' + str(self.score)
        return text