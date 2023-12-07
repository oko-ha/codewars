class Warrior:
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []
    
    def training(self, train:list):
        description, reward_exp, min_level = train
        if min_level > self.level:
            return "Not strong enough"
        else:
            self.experience += reward_exp
            self.achievements.append(description)
            self.update()
            return description

    def battle(self, enemy_level):
        if 0 < enemy_level <= 100:
            diff = enemy_level - self.level
            if diff > 4 and enemy_level // 10 > self.level // 10:
                return "You've been defeated"
            elif diff < -1:
                return "Easy fight"
            elif diff > 0:
                self.experience += 20 * diff * diff
                self.update()
                return "An intense fight"
            else:
                self.experience += 10 + (5 * diff)
                self.update()
                return "A good fight"
        return "Invalid level"

    def update(self):
        self.experience = min(10000, self.experience)
        self.level = self.experience // 100
        if self.level < 10:
            self.rank = "Pushover"
        elif self.level < 20:
            self.rank = "Novice"
        elif self.level < 30:
            self.rank = "Fighter"
        elif self.level < 40:
            self.rank = "Warrior"
        elif self.level < 50:
            self.rank = "Veteran"
        elif self.level < 60:
            self.rank = "Sage"
        elif self.level < 70:
            self.rank = "Elite"
        elif self.level < 80:
            self.rank = "Conqueror"
        elif self.level < 90:
            self.rank = "Champion"
        elif self.level < 100:
            self.rank = "Master"
        else:
            self.rank = "Greatest"