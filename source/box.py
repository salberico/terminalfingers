class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.inner_height = max(0, h - 2)
        self.inner_width = max(0, w - 2)

    def size(self):
        return self.width * self.height

    def inner_size(self):
        return self.inner_height * self.inner_width