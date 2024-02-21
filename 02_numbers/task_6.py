def compare_speeds(speed_kmh, speed_ms):
    speed_kmh_to_ms = speed_kmh / 3.6

    if speed_kmh_to_ms > speed_ms:
        return "speed km/h bigger"
    elif speed_kmh_to_ms < speed_ms:
        return "speed m/s bigger"
    else:
        return "The speeds are equal"


speed_kmh = float(input("Enter your speed in km/h: "))
speed_ms = float(input("Enter your speed in m/s: "))

print(compare_speeds(speed_kmh, speed_ms))
