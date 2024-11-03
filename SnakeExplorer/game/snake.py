class Snake:
    def __init__(self):
        self._parts = []
        self.dir = (0, -1)

    def add_part(self,x, y):
        self._parts.append((x,y))

    def move(self,x, y, grow=False):
        self._parts.insert(0,(x,y))
        if not grow:
            return self._parts.pop()
        else:
            return None

    def list_parts(self):
        return self._parts

    def get_first_part(self):
        return self._parts[0]
