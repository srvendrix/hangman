class Horse():
    def __init__(self, name, wight):
        self.name = name
        self.wight = wight
        

class Rider():
    def __init__(self, name, age, horse):
        self.name = name
        self.age = age
        self.horse = horse

horse_1 = Horse("bakayoko", 45)
rider_1 = Rider('mario', 12, horse_1)

print(rider_1.name)
print(rider_1.horse.name)
print(rider_1.horse.wight)


