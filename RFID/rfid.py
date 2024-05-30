import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522 
ledVerde = 7 
ledRojo = 37 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(ledVerde,GPIO.OUT) 
GPIO.output(ledVerde, GPIO.LOW) 
GPIO.setup(ledRojo,GPIO.OUT) 
GPIO.output(ledRojo,GPIO.LOW) 
reader = SimpleMFRC522() 
while True: 
   try: 
       id, text = reader.read()
       print(id) 
       if id==702720218568: 
           print("Estas autorizado") 
           GPIO.output(ledVerde,GPIO.HIGH)
           GPIO.output(ledRojo,GPIO.LOW) 
       else: 
           GPIO.output(ledRojo,GPIO.HIGH)
           GPIO.output(ledVerde,GPIO.LOW)
   except  KeyboardInterrupt:
       GPIO.cleanup()
       exit()
