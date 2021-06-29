# Sal's Shipping
# The most affordable experience

weight = 4.8

# Ground Shipping
cost_ground = ""

if weight <= 2:
      cost_ground = (weight * 1.50) + 20
elif weight <= 6:
      cost_ground = (weight * 3) + 20
elif weight <= 10:
      cost_ground = (weight * 4) + 20
else:
      cost_ground = (weight * 10) + 20
print("Your shipping will cost:",cost_ground)

# Premium Shipping
premium = 125

print("Your shipping premium will cost:",premium)

# Drone Shipping
drone =""

if weight <= 2:
     drone = weight * 4.50
elif weight <= 6:
     drone = weight * 9
elif weight <= 10:
     drone = weight * 12
else:
   drone = weight * 14.25
print("Your drone shipping will cost:",drone)

# Choose the cheapeast way to shipping

if cost_ground < premium < drone:
  print("The best choice is:",cost_ground)
elif cost_ground < drone < premium:
  print("The best choice is:",cost_ground)
elif premium < cost_ground < drone:
  print("The best choice is:",premium)
elif premium < drone < cost_ground:
  print("The best choice is:",premium)
else:
  print("The best choice is:",drone)
