Time_in_seconds= float(input("Enter time in seconds: "))
if Time_in_seconds < 600: 
    Diference = 600 - Time_in_seconds
    print(f"\nThe time is less than 10 minutes by {Diference:.2f} seconds")
elif Time_in_seconds == 600:
    print(f"\nThe time is exactly 10 minutes")
else:
    print(f"\nThe time is more than 10 minutes")