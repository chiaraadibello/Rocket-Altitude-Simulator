#######
#ROCKET ALTITUDE SIMULATOR
#One of my first lil projects in python, 
#simulating the altitude of a rocket over time.

import time

# Rocket parameters
acceleration = 20      # m/s²
time_elapsed = 0       # seconds
time_step = 1          # seconds

print("ROCKET ALTITUDE SIMULATOR")
print("--------------------------------")

while time_elapsed <= 20:

    # Calculate altitude
    altitude = 0.5 * acceleration * time_elapsed ** 2

    # Calculate velocity
    velocity = acceleration * time_elapsed

    print(f"Time: {time_elapsed:2} s | "
          f"Altitude: {altitude:6.1f} m | "
          f"Velocity: {velocity:6.1f} m/s")

    time_elapsed += time_step

    time.sleep(0.2)