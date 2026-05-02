from Entity import Entity


class Aizel(Entity):
    def on_meet(self, game, player):
        print("遇到艾泽尔：选择帮助")

        choice = input("1: 咖啡加速  2: 减少任务\n")

        if choice == "1":
            player.speed += 1
        elif choice == "2":
            game.reduce_tasks()

class Supriya(Entity):
    def __init__(self, game_map):
        super().__init__(...)
        self.meet_count = 0
        self.is_enemy = False

    def on_meet(self, game, player):
        from Enemy import Federico

        self.meet_count += 1

        if self.meet_count == 1:
            print("获得无人机：显示所有人位置")
            game.reveal_all = True

        elif self.meet_count >= 2:
            print("费德里科获得你的位置！")
            for enemy in game.enemies:
                if isinstance(enemy, Federico):
                    enemy.target_position = player.position

    def become_enemy(self, game):
        self.is_enemy = True
        game.enemies.append(self)


class Oren(Entity):
    def on_player_caught(self, game):
        choice = input("是否出卖奥伦？(y/n)")

        if choice == "y":
            print("奥伦被卖掉了...")
            game.save_flag["oren_sold"] = True
            return True  # 替死成功

        return False