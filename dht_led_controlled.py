from grovepi import *
from grove_rgb_lcd import *
from time import sleep

dht_sensor_port = 7
dht_sensor_type = 0
button_port = 4

pinMode(button_port,"INPUT")

sleep_state = 0

while True:
    try:
        button_status = digitalRead(button_port)      
        
        if button_status == 1 and sleep_state == 1:
            sleep_state = 0
        elif button_status == 1 and sleep_state == 0:
            sleep_state = 1
        
        [ temp, hum ] = dht(dht_sensor_port,dht_sensor_type)
        #print ("temp = ", temp, "C, humidity = ", hum,", button: ", button_status, "sleep_state: ", sleep_state)
        t = str(temp)
        hum = str(hum)
        
        if not sleep_state:
            setRGB(0,255,0)
            setText("Temp: " + t +"C" + "\n" + "Hum: " + hum+"%")
        else:
            setRGB(0,0,0)
            
        sleep(5)
 
    except (IOError, TypeError) as e:
        print("Error")
        setRGB(0,0,0)
        setText("Error")
                
    except KeyboardInterrupt as e:
        print(str(e))    
        setText("")
        setRGB(0,0,0)
        break
