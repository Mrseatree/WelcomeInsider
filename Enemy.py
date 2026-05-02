from Entity import Enemy
from Neutral import Supriya


class v2leaf(Enemy):
    def __init__(self, game_map, player):
        super().__init__(
            game_map, player,
            id = 4,
            name="Weierlife",
            speed= 2,
            position=[6, 6]
        )

    def on_catch_player(self, game):
        print("由于遇到【薇尔丽芙】，【费德里科】获得了你的位置。")
        for enemy in game.enemies:
            if isinstance(enemy, Federico):
                enemy.target_position = game.player.position


class Leimuan(Enemy):
    def __init__(self, game_map, player):
        super().__init__(
            game_map, player,
            id=5,
            name="Leimuan",
            speed=1,
            position=[10, 10]
        )
        self.vision_range = 5

    def on_detect_player(self, game):
        print("被蕾缪安通缉！")

        game.player.has_second_chance = False  # 禁用回旋余地
        game.player.wanted = True  # 标记通缉

        # 斯普莉雅变敌对
        for npc in game.neutrals:
            if isinstance(npc, Supriya):
                npc.become_enemy(game)


class Federico(Enemy):
    def __init__(self, game_map, player):
        super().__init__(
            game_map, player,
            id = 3,
            name = "Federico",
            speed = 3,
            position = [8, 8]
        )
        self.vision_range = 3
        self.target_position = None

    def update(self):
        for _ in range(self.speed):  # 一回合走多步
            if self.target_position:
                self.move_towards(self.target_position)
            else:
                self.chase_player()

    def move_towards(self, target):
        tx, ty = target
        ex, ey = self.position

        dx = tx - ex
        dy = ty - ey

        if abs(dx) > abs(dy):
            self.move(1 if dx > 0 else -1, 0)
        else:
            self.move(0, 1 if dy > 0 else -1)