'''from rpi_lcd import LCD
import time

# 初始化，默认地址是 0x27，如果是 0x3F 需要指定
# lcd = LCD(address=0x3F) 
lcd = LCD(address=0x27)

# 显示文字
lcd.text("Hello, World!", 1)
lcd.text("Raspberry Pi", 2)

# 等待5秒后退出了，否则程序会直接结束，屏幕可能清空
time.sleep(5)
lcd.clear()'''