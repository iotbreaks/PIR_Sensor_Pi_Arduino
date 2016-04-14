/*
  PIR_Interrupt.ino
  Created by Kenny from www.iotbreaks.vn, April 14, 2016.
  Released into the public domain.
  Tutorial: 
*/
const byte ledOutPin = 13; // LED connected to digital pin 13
const byte pirInPin = 2;  // HC-SR501 DOut connected to interrupt pin 2 (Int.0)
volatile byte val = HIGH; // variable to store the read value from PIR sensor. 
                          // Default is HIGH for inactive state of PIR sensor
void setup() {
  pinMode(ledOutPin, OUTPUT);
  pinMode(pirInPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pirInPin), pirSensorDidChange, CHANGE);
  digitalWrite(ledOutPin,1);
}

void loop() {
  // Do nothing here
}

void pirSensorDidChange() {
  val = digitalRead(pirInPin);
  digitalWrite(ledOutPin, val);
}
