from adafruit_circuitplayground.express import cpx
import time
import random

def randgen():
	r = random.randint(0,10)
	g = random.randint(0,10)
	b = random.randint(0,10)
	return (r,g,b)

while True:
    a = randgen()
    for i in range(0,10,1):
        cpx.pixels[i] = a
        time.sleep(0.05)

    a = randgen()
    for i in range(0,10,1):
        cpx.pixels[i] = a
        time.sleep(0.05)

    a = randgen()
    for i in range(0,10,1):
        cpx.pixels[i] = a
        time.sleep(0.05)