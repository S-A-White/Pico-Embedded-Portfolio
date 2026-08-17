from machine import Pin
import time
import math

gate = Pin(15, Pin.IN, Pin.PULL_UP)

break_ts = []

#Creating array t to hold times
def gate_handler(pin):
    t = time.ticks_ms()
    break_ts.append(t)
    print(f"Beam Broken at {t} ms")
#records time for every beam break
gate.irq(trigger = Pin.IRQ_FALLING, handler = gate_handler)


print("Swing the pendulum throught the gate to start data recording")

try:
    while True:
        time.sleep_ms(50)
except KeyboardInterrupt:
    print("Stopped.")

#analysing results (done in same code file as collection for pico efficiency)

print(f"\nTotal beam breaks: {len(break_ts)}")

if len(break_ts) >= 3:
    periods = []
    for i in range(2, len(break_ts)):
        period = time.ticks_diff(break_ts[i], break_ts[i-2]) / 1000
        periods.append(period)

        avg_T = sum(periods) / len(periods)
        print(f"Individual Periods (s): {[round(p,3) for p in periods]}")
        print(f"Average Period (s): {round(avg_T, 3)}")
        print(f"Average Periods (T) = {avg_T:.4g} s")

else:
    print("Not eenough beam breaks to find a period, try swinging the pendulum again for more oscillations")

L = 0.78486 #Length of pendulum in meters
g = 4*math.pi**2*(L/(avg_T**2)) #Calculating g using the formula g = 4π²L/T² 
g_diff = g - 9.81582 #measured value compared to accuraely knowl local value of g (obtained from the national geographic survey
print(f"The value of g found by this pendulum setup was {g:.4f}, which is accurate to ±{abs(g_diff):.4f}")