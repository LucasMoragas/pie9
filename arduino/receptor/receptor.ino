void setup() {
  Serial.begin(9600);
}

void loop() {
  int mockTemperature = random(200, 301); 

  float temperature = mockTemperature / 10.0; 

  Serial.println(temperature);      

  delay(100); 
}
