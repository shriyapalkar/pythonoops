class Point:
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return "({0})".format(self.value)

  def __add__(self):  
    return Point(+self.value)
  
a=Point(8)
add_num=+


