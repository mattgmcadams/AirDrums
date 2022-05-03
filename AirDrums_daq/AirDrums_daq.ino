
#include <Arduino_LSM6DS3.h>

unsigned long clocktime;
// 2, 3 in
// 9, 10,  3.3v out

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");

    while (1);
  }

  Serial.println("Timestamp, ax, ay, az, gx, gy, gz");
}

void loop() {
  float ax, ay, az;
  float gx, gy, gz;
  clocktime = millis();

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
 
    IMU.readGyroscope(gx, gy, gz);

    Serial.print(clocktime);
    Serial.print(", ");
    Serial.print(ax);
    Serial.print(", ");
    Serial.print(ay);
    Serial.print(", ");
    Serial.print(az);
    Serial.print(", ");
    Serial.print(gx);
    Serial.print(", ");
    Serial.print(gy);
    Serial.print(", ");
    Serial.println(gz);
  }

}
