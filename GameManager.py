from Enemy import Federico, v2leaf, Leimuan
from Entity import Player, Enemy


class GameManager:
    def __init__(self,game_map):
        self.state = "INIT"  # INIT / RUNNING / GAME_OVER
        self.player = None
        self.enemies = []
        self.neutrals = []
        self.game_map = game_map

        # 全局状态
        self.reveal_all = False
        self.save_flag = {}

    def start_game(self):
        self.state = "RUNNING"
        self.player = Player(self.game_map)

        # 追捕
        self.enemies = [
            Federico(self.game_map, self.player),
            v2leaf(self.game_map, self.player),
            Leimuan(self.game_map, self.player)
        ]

        # 中立角色
        self.neutrals=[]

    def update(self):
        if self.state != "RUNNING":
            return

        # 里凯莱行动
        self.player.update()
        # 调试
        print(f"Player:{self.player.position}")

        # 追捕者行动
        for enemy in self.enemies:
            enemy.update()
            # 调试
            print(f"{enemy.name}: {enemy.position}")

        # 检测被发现
        self.check_detection()

        # 检测游戏结束
        self.check_game_over()

    def check_detection(self):
        for enemy in self.enemies:
            if self.can_detect(enemy, self.player):
                if hasattr(enemy, "on_detect_player"):
                    enemy.on_detect_player(self)

    def can_detect(self, enemy, player):
        ex, ey = enemy.position
        px, py = player.position

        # 默认视野（如果没有就给个默认值）
        vision = getattr(enemy, "vision_range", 2)

        return abs(ex - px) + abs(ey - py) <= vision

    def check_game_over(self):
        for enemy in self.enemies:
            if enemy.position == self.player.position:

                print(f"{enemy.name} 抓住了玩家！")

                # 1. 玩家尝试回旋
                if hasattr(self.player, "try_escape"):
                    if self.player.try_escape():
                        return

                # 2. 中立角色替死
                for npc in self.neutrals:
                    if hasattr(npc, "on_player_caught"):
                        if npc.on_player_caught(self):
                            return

                # 3. 敌人触发能力
                if hasattr(enemy,"on_catch_player"):
                    enemy.on_catch_player(self)

                # 4. 游戏结束
                self.state = "GAME_OVER"
                return