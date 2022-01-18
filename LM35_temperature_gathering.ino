/*
Modular Heated Tiles | Prototype 2.0
OSEPP LM35 Temperature Sensor Module used to gather temperature data for data processing purposes
*/
int LM35 = A0; //Change this when plugging the sensor to a different analog pin
int temperatureLED = 13; //LED used to keep track of the temperature fluctuation

int analogValue = 0;
float voltsValue = 0.0;      
float temperatureValue = 0.0;      

void setup() {
   Serial.begin(9600);
   pinMode(tempLED1, OUTPUT);   
}

void loop() {  
  delay(1000);
  
  analogValue = analogRead(LM35); //Reads raw input value from analog pin A0
  voltsValue=(analogValue/1024.0)*5.0; //Converts the initial value to volts
  temperatureValue = temperatureValue*100.0; //Converts the volts value to the corresponding temperature value (in °C)
  
  Serial.print("Current temperature : "); 
  Serial.println(temperatureValue);

  if (temperatureValue>30.0) { //Turns on the LED to be alerted when a certain temperature threshold is reached
    digitalWrite(temperatureLED, HIGH);
  }
  else {
    digitalWrite(temperatureLED, LOW);
  }
}
