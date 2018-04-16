import turtle
sides_list = [3,7,9,15]

dict_list = [
{"num_of_sides":"5", "length":"120", "turn_angle": "72", "x":-50, "y":50},
{"num_of_sides":"3", "length":"60", "turn_angle": "120", "x":50, "y":-50},
{"num_of_sides":"8", "length":"30", "turn_angle": "45", "x":-100, "y":-100},
]

def standard_shape(sides,size):
  angle = 360 / sides  
  print angle
  for side in range(1,sides+1):
    turtle.forward(size)
    turtle.right(angle)

# q1 tests
# standard_shape(5,120)
# standard_shape(9,60)

# q2 tests
# for item in sides_list:
#   print item
#   standard_shape(item,50)

#q3 tests
# for j in range(0,len(dict_list)):
#   print j
#   turtle.penup()
#   turtle.setx(int(dict_list[j]["x"]))
#   turtle.sety(int(dict_list[j]["y"]))
#   turtle.pendown()
#   for shape_side in range(1, int(dict_list[j]["num_of_sides"])+1):
#     turtle.forward(int(dict_list[j]["length"]))
#     turtle.right(int(dict_list[j]["turn_angle"]))
    
  




