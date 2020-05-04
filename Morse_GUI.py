from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

#Setting GPIO number standard
GPIO.setmode(GPIO.BCM)

#Hardware
led = LED(17)

#GUI DEFINITIONS
win = Tk()
win.title('Morse Code GUI')
myFont = tkinter.font.Font(family = 'Helveltica', size = 12, weight = 'bold')

### EVENT FUNCTIONS ###
def blink(duration):
    if(duration == '1'):
        t = 1
    else:
        t = 0.5
        
    print(t)
    led.on()
    sleep(t)
    led.off()
    sleep(1)

def displayMorse():   
    text = inputText.get().lower()
    if len(text) > 12:
        errorText.delete("1.0",END)
        errorText.insert(END, '12 char max')
        return
    
    errorText.delete("1.0",END)
    errorText.insert("1.0",'Blinking')
    
    for char in text:
        for dot_dash in morse_code[ord(char)-97]:
            blink(dot_dash)
        
    
    errorText.delete("1.0",END)
    errorText.insert("1.0",'Done')
    
#Defining the each char morse code
morse_code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100']

### WIDGET ###
Label(win, text = "Input", font = myFont).grid(row = 0)
errorText = Text(win, height = 1, width = 15)
errorText.grid(row = 1 , column = 1)

inputText = Entry(win)
inputText.grid(row = 0, column = 1)

Button(win, text = 'Display Morse code', command = displayMorse).grid(row = 2, column = 1)