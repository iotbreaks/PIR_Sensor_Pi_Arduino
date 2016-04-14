/*
  PIR_Polling.ino
  Created by Kenny from www.iotbreaks.vn, April 14, 2016.
  Released into the public domain.
  Tutorial: 
*/
const byte ledOutPin = 13; // LED connected to digital pin 13
const byte pirInPin = 12;  // HC-SR501 DOut connected to digital pin 12
volatile byte val = HIGH; // variable to store the read value from PIR sensor. 
                          // Default is HIGH for inactive state of PIR sensor

void setup() {
  pinMode(ledOutPin, OUTPUT);
  pinMode(pirInPin, INPUT);
}

void loop() {
  val = digitalRead(pirInPin);
  digitalWrite(ledOutPin, val);
  delay(200);
}
