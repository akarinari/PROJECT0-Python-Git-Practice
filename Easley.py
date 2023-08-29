print("Welcome to the Space Travel Calculator")
distance = int(input("Enter the distance to the desired celestial object in light-years."))
speed = int(input("Enter the speed of your space craft in fraction of the speed of light"))
time = distance/speed
print("It would take", time, "hours to reach your destination in your space craft")