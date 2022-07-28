import time

def count(t):
    while t:
        mins, secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer, end="\r")
        timer.sleep(1)
        t -= 1

    print("Timer Completed! ")

t = input("Enter the time in seconds: ")

count(int(t))