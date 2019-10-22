import time

t = int(input("Countdown from: "))
while t >= 0:
	mins, secs = divmod(t, 60)
	timeformat = '{:02d}:{:02d}'.format(mins, secs)
	time.sleep(1)
	print("Time Remaining: "+ timeformat)
	t -= 1
print("Kaboom")
