"""
logical operators (o compare 2 or more conditions ) (always in bool)
AND
C1    C2     result
F     F         F
F     T         F
T     F         F
T     T         T


OR
C1    C2     result
F     F         F
F     T         T
T     F         T
T     T         T


NOT




"""

# AND OPERATION
# physics = 22
# chemistry = 32
# print(physics > 33 and chemistry > 33)
# output = false
# physics = 65
# chemistry = 43
# print(physics > 33 and chemistry > 33)
# output = true
# physics = 78
# chemistry = 32
# print(physics > 33 and chemistry > 33)
# output = false
# OR OPERATION
# physics = 22
# chemistry = 32
# print(physics > 33 or chemistry > 33)
# output = false
# physics = 58
# chemistry = 52
# print(physics > 33 or chemistry > 33)
# output = true
# physics = 31
# chemistry = 52
# print(physics > 33 or chemistry > 33)
# output = true
# physics = 31
# chemistry = 52
# print(physics > 33 or not chemistry > 33)
# output = false
# physics = 31
# chemistry = 52
# print(not (physics > 33 or chemistry > 33))
# output = false