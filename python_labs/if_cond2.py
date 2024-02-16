VERSION = 18
if (VERSION < 0):
    print("Version is negative.")
elif (VERSION > 0):
    if (VERSION <= 10):
        print("Version is between 1-10")
    elif (VERSION > 10 and VERSION <= 20):
        print("Version is between 11-20")
    else:
        print("Version is greater than 20")
else:
    print("Version is zero")
