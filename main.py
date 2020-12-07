import eel
import pyowm


owm = pyowm.OWM("7bdb8ba83dbaf8796b0327c7fd80dba6")

@eel.expose
def get_weather(place):


    
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    temp = round(temp)

    if temp == 1:
        
        return "Temperature in " + place + " is " + str(temp) + " degree!"
    else:
        return "Temperature in " + place + " is " + str(temp) + " degrees!"
    
   

eel.init('web')
eel.start('main.html', size=(700,700))