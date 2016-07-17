/*
  Read a photo resistor's value and send out it out of the Serial port
*/

// Photo Resistor is connected on Analog Pin 0
int photoresistor_pin = 0;

void setup()
{
    // Begin serial communication
    Serial.begin(9600);
}

void loop()
{
    // Write the value of the photoresistor to the serial port.
    Serial.println(analogRead(photoresistor_pin));

    // Add a sub-second delay. This isn't required, but makes
    // the readings a little more managing if watching them through
    // the serial monitor.
    delay(500);
}
