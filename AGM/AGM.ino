#include <Arduino_LSM9DS1.h>

const int buttonPin = 13;

int buttonState = 0;
float ax=0, ay=0, az=0;
float gx=0, gy=0, gz=0;
float mx=0, my=0, mz=0;

void setup() {
  Serial.begin(9600);

  Serial.println("Started");

  pinMode(buttonPin, INPUT);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
//  Serial.print("Magnetic field sample rate = ");
//  Serial.print(IMU.magneticFieldSampleRate());
//  Serial.println(" uT");
//  Serial.println();
//  Serial.print("Accelerometer sample rate = ");
//  Serial.print(IMU.accelerationSampleRate());
//  Serial.println(" Hz");
//  Serial.println();
//  Serial.print("Gyroscope sample rate = ");
//  Serial.print(IMU.gyroscopeSampleRate());
//  Serial.println(" Hz");
//  Serial.println();
//  
//  Serial.println("Acceleration in G's - Gyroscope in degrees/second - Magnetic Field in uT");
//  Serial.println("AX\tAY\tAZ\tGX\tGY\tGZ\tMX\tMY\tMZ");


}

void loop() {

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);

  }
  Serial.print(ax);
  Serial.print(':');
  Serial.print(ay);
  Serial.print(':');
  Serial.print(az);
  Serial.print(':');
  
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gx, gy, gz);
  }
  Serial.print(gx);
  Serial.print(':');
  Serial.print(gy);
  Serial.print(':');
  Serial.print(gz);
  Serial.print(':');
  
  if (IMU.magneticFieldAvailable()) {
    IMU.readMagneticField(mx, my, mz);
  }
  Serial.print(mx);
  Serial.print(':');
  Serial.print(my);
  Serial.print(':');
  Serial.print(mz);
  Serial.print(':');


  // buttonState = digitalRead(buttonPin);
  Serial.println(digitalRead(buttonPin));
}
