import gpiozero
import time
red_led = gpiozero.LED(22)

def blink_red_led():
    
    red_led.on()
    time.sleep(1)
    red_led.off()
    time.sleep(1)

def fast_blink():
    counter = 3
    while counter != 0:
        red_led.on()
        time.sleep(0.3)
        red_led.off()
        time.sleep(0.3)
        counter -= 1

def blink_green_led():
    green_led = gpiozero.LED(17)
    green_led.on()
    time.sleep(1)
    green_led.off()
    time.sleep(1)


counter = input("Enter number of times to blink: ")
start = 0

if counter.isdigit():
    while True:
        blink_green_led()
        counter = int(counter)
        counter -= 1
        if int(counter) == 0:
            fast_blink()
            break
        
        # print(f"blinked -> {start}")
else:
    blink_red_led()
    
    
    
    