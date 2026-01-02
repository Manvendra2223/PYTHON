
## Transportation Mode Suggestion:

Distance =17 # distance in kilometers

if Distance <= 3:
    mode_of_transport = "Walk"
elif Distance <= 15:
    mode_of_transport = "Bike"
else:
    mode_of_transport = "Drive a car"
print(mode_of_transport)