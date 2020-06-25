class partyanimal():
 x=0

 def __init__(self):
  print("iam constructed")
 print("nothing")
 def party(self):
  self.x = self.x + 1
  print("So far", self.x)

 def __del__(self):
  print("iam destructed", self.x)

an = partyanimal()

an.party()
an.party()

an = 42

print('an contains', an)
