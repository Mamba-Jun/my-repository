'''from gpiozero import LED
from rpi_lcd import LCD
import time
import os

file = 'count.txt'
lcd = LCD(address=0x27)
Red  = LED(18)
Green = LED(20)


def read_value():
    if os.path.exists(file):
       with open(file, 'r') as f:
         try:
            return int(f.read().strip())
         except:
            return 0
    else:
        return 0
        
def save_value(count):
    with open(file,'w') as f:
       try:
          f.write(str(count))
       except:
          return 0
          
i = read_value()


def light_on():
    global i
    Red.on()
    Green.off()
    lcd.text("Red on", 1)
    time.sleep(5)
    Red.off()
    Green.on()
    lcd.text("Green on", 1)
    time.sleep(5)
    i = i+1
    lcd.text(f'Total:{i}', 2)
    save_value(i)
    
    
def destroy():
    Red.off()
    Green.off()
    lcd.clear()
    
if __name__ == '__main__':
    try:
        while True:
            light_on()
    except KeyboardInterrupt:
        destroy() '''