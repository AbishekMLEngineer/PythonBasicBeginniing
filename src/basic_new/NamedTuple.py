from collections import namedtuple

Color = namedtuple('Color',['red','blue'])
color = Color(55,125,45)
print(color.red)

xmen = namedtuple('xmen',['wolf','cyclop','jean'])
xM=xmen(wolf='wolve',cyclop='cyc',jean='Jen')
print()
print(xM.wolf)
