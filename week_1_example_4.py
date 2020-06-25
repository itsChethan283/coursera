class partyanimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
class fotballfan(partyanimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 1
        self.party()
        print(self.name, "party count", self.points)

s = partyanimal("sally")
s.party()

j = fotballfan("jim")
j.party()
j.touchdown()
