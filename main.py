import eel
import pyowm


owm = pyowm.OWM("")

@eel.expose
def get_weather(place):


    
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather
    except:
        return "DID NOT FOUND CITY LOL" + place + " !"

    temp = w.temperature('celsius')['temp']
    temp = round(temp)

    if temp == 1:
        
        return "Temperature in " + place + " is " + str(temp) + " degree!"
    else:
        return "Temperature in " + place + " is " + str(temp) + " degrees!"
    
   

eel.init('web')
eel.start('main.html', size=(700,700))
