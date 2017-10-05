void setup()
{
  // initialize serial comms
  Serial.begin(9600); 
}

void loop()
{
  // read A0
  int val1 = analogRead(0);
  // read A1
  int val2 = analogRead(1);
  // print to serial
  Serial.println(val1);
  Serial.println(val2);
  // wait 
  delay(50);
}
