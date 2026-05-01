class Entity:
    def __init__(self, id, name, speed, position):
        self.id = id
        self.name = name
        self.speed = speed
        self.position = position

    def move(self, direction):
        # 简单移动逻辑
        pass

    def update(self):
        pass

class Player(Entity):
    def __init__(self):
        super().__init__(
            id = 0,
            name = "Richele",
            speed = 1,
            position = [0, 0]
        )

    def update(self):
        # 从输入读取方向（先可以写死）
        cmd = input("move (w/a/s/d): ")
        if cmd == "w":
            self.position[1] -= 1
        elif cmd == "s":
            self.position[1] += 1
        elif cmd == "a":
            self.position[0] -= 1
        elif cmd == "d":
            self.position[0] += 1


class Enemy(Entity):
    def __init__(self):
        super().__init__(
            id = 2,
            name = "Enemy",
            speed = 1,
            position = [5, 5]
        )

    def update(self):
        # 简单AI：随机走 or 朝玩家走
        pass