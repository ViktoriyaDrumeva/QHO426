perfect_height = float(input("What is the perfect grass height?
current_height = float(input("What is the height of grass at the moment?(in cm)"))

counter = 0 

if current_height <= perfect height:
  print("Do not cut the grass.Let it grow!")
  else:
    while perfect height < current_height:
      counter += 1
  print("Chop-chop numero {}".format(counter))
  current_height *=0.95
  print("Now the grass is {:3f}cm tall".format(current height))
