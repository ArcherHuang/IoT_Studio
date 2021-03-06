// DHT
#include "DHT.h"
#define DHTPIN A0
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

#include <Bridge.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  dht.begin();
  Bridge.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  float h = dht.readHumidity();
  float t = dht.readTemperature();
     
  // Bridge
  Bridge.put("Humidity", String(h));
  Bridge.put("Temperature", String(t));
        
  delay(1000); //每秒回傳一次資料
}

