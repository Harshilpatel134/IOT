import json
import urllib2
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        result = json.loads(urllib2.urlopen(urllib2.Request("http://thingspeak.com/channels/759553/feeds.json?key=4Q9EJB5HO1J245FQ")).read())
        output_str = "There are " + str(len(result["feeds"])) + " feeds and latest value is " + str(result["feeds"][-1]["field1"])
        #result = json.loads(urllib2.urlopen(urllib2.Request("http://api.openweathermap.org/data/2.5/weather?q=kansas,us&mode=json&units=metrics&appid=907a0d541e90e08a4700053800659309")).read())
        #output_str = "Temperature is " + str(result["main"]["temp"]-273.15) + " and pressure is " + str(result["main"]["pressure"])
        tts = ALProxy("ALTextToSpeech")
        tts.say(str(output_str))

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box