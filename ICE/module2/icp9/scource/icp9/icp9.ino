int led = 8;   
char val;
const int AOUTpin= 0; 

int value; 
void setup()
{

pinMode(led, OUTPUT);  // Digital pin 13 set as output Pin
Serial.begin(9600);
pinMode(AOUTpin, INPUT);
}

void loop()
{
  while (Serial.available() > 0)
  {
  val = Serial.read();
  
  }

  if( val == '1') // Forward
    {
     
      digitalWrite(led, HIGH);
    }
  else if(val == '2') // Backward
    {
 
      digitalWrite(led, LOW);
    }
value= analogRead(AOUTpin);
 Serial.println(String(value));
 delay(1000); 
   
}
