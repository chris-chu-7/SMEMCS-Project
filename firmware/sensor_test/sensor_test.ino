#include "Adafruit_Sensor.h"
#include "DHT.h" 

#define DHTPIN 2 
#define DHTTYPE DHT22 

unsigned long myTime;
float humidity; 
float temperature; 
unsigned long ldrValue; //variable for LDR reading


DHT dht = DHT(DHTPIN, DHTTYPE);

void setup() {
  //serial communication with a baud rate of 9600 (9600 bits per second) 
  Serial.begin(9600); 
  delay(2000); // wait for the serial connection to establish 
  dht.begin();
  Serial.println("Time (s),Temp (°F),Humidity (%), LDR (%)");
}

void loop() {
    delay(1000); //delay the time before initial sensor reading to wait for the dht to calibrate
    myTime = millis() / 1000;

    humidity = dht.readHumidity();
    temperature = dht.readTemperature(true);
    ldrValue = analogRead(A0);
    ldrValue = (ldrValue / 1023.0) * 100; //convert to percentage (0-100%) for friendly interface   

    if (isnan(humidity) || isnan(temperature)){ //ensure all readings are valid for easier data processing
      //ldr value cannot be nan since it is an integer
      Serial.println("Failed to read");
      return; //if there is an reading issue, just restart the loop
    }

    Serial.print(myTime); 
    Serial.print(",");
    Serial.print(humidity);
    Serial.print(",");
    Serial.print(temperature);   
    Serial.print(",");
    Serial.println(ldrValue);

}
