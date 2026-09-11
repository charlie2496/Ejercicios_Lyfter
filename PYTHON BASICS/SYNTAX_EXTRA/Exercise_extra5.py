Speed=float(input("Enter the speed in km/h: "))
Speed_ms = 0
if Speed <= 0:
    print("You can't enter 0 or a negative number.")
else:
    Speed_ms=(Speed * 1000) / 3600
    print(f"The speed in m/s is: {Speed_ms:.2f} m/s")