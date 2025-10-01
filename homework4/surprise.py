# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_name_star (targets):
    for name in targets:
        return(name)

print_name_star(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_name_type (targets):
    for key in targets:
        print (f"The star is: {key}, and its spectral type is: {targets[key]['Spectral Type']}")

print_name_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def mag_condition (targets):
    for name in targets:
        if targets[name]['Magnitude'] > 0.1:
            print(f"The star {name} has a magnited of {targets[name]['Magnitude']} which is greater than 0.1 ")

mag_condition(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Altair"] = {
    "RA": "19h 50m 47s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"
}

print (targets)
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

#dont know how to do this. pls post solution

# 6) What is your favorite constellation?
# Big Dipper