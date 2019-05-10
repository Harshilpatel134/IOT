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
        tts = ALProxy("ALTextToSpeech")
        tts.say("hello")      
        result = json.loads(urllib2.urlopen(urllib2.Request("http://127.0.0.1:5000/")).read())
        output_str = "There are " + str(len(result["feeds"])) + " feeds and latest value is " + str(result["feeds"][-1]["field1"])
        tts = ALProxy("ALTextToSpeech")
        tts.say(str(output_str))

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box