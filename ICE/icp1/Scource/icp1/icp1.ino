
int ss = 0;
void setup()
{
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(9, INPUT);
}
void loop()
{
  ss = digitalRead(9); 
  if (ss == LOW)
  {
    digitalWrite(3, HIGH); 
    digitalWrite(4, LOW); 
    digitalWrite(5, LOW); 
  }
  else
  {
    for(int l=0; l<=5; l++)
    {
      digitalWrite(3, HIGH); 
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      delay(500); 
      digitalWrite(3, LOW); 
      digitalWrite(4, HIGH);
      digitalWrite(5, LOW); 
      delay(500); 
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(5, HIGH); 
      delay(500);
    }
  }
}
