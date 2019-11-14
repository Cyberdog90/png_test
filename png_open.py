class PngOpen:
    def __init__(self, name):
        with open(name + ".png", "rb") as f:
            data = f.read().hex()
        self.image = data
        self.signature = "89504e470d0a1a0a"

    def check_image(self):
        if self.signature == self.image[0:16]:
            return 1
        else:
            return 0
