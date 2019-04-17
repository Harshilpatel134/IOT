#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp; // I2C

const int AOUTpin= 0; 

int value; 

String output;
void setup()   
{ 
Serial.begin(57600);
pinMode(AOUTpin, INPUT);


}  
void loop() 
{ 
value= analogRead(AOUTpin);
 Serial.println(String(value));
/*
Serial.print("light: "); 
Serial.println(value);
Serial.print("dust: "); 
Serial.println(value1);
Serial.print("heart: "); 
Serial.println(value2);

 Serial.print(F("Temperature = "));
    Serial.print(bmp.readTemperature());
    Serial.println(" *C");
    
    Serial.print(F("Pressure = "));
    Serial.print(bmp.readPressure());
    Serial.println(" Pa");

    Serial.print(F("Approx altitude = "));
    Serial.print(bmp.readAltitude(1013.25)); // this should be adjusted to your local forcase
    Serial.println(" m");
    
    Serial.println();
    */
   // output=String(value)+","+String(value1)+","+String(value2)+","+String(bmp.readTemperature())+","+String(bmp.readPressure())+","+String(bmp.readAltitude(1013.25));
   // Serial.println(output);
delay(100000); 
} 
