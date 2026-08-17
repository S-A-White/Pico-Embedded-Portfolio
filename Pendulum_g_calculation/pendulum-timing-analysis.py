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
    whil True:
    time.sleep_ms(50)
except KeyboardInterrupt:
    print("Stopped.")

#analysing results (done in same code file as collection for pico efficiency)