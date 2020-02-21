
class Soldier():
    def __init__(self, name):
        self.name = name

class Guns():
    def __init__(self):
        self.bullets = 30

    def fire(self):
        print(f"{self.name} fire in the hall")
        for i in range(self.bullets, -1, -1):
            self.bullets -=1
            print("Tah-tah-tah =", i)
        print("Empty, need RELOAD")
        
    def reload(self):
        self.bullets = 30
        print("Перезарядил")
        self.fire()

    def voina(self):
        self.fire()
        self.reload()
        self.fire()

class Act_of_Shooting(Soldier, Guns):
    def __init__(self, name):
        Soldier.__init__(self, name)
        Guns.__init__(self)

terror = Act_of_Shooting("Ryan")
terror.voina()
# terror.fire()
# for i in range(30, 0, -1):
#     print(i)