# weather-channel

My implementation of GrovePI kit, to monitor temperature and humidity where I put my RPi.
Requires 32-bit Raspbian for the GrovePi stuff to install.

Display is plugged to I2C-1.
Temperature sensor is plugged to D7.
Button sits with D4.

Also set up a service via systemctl to start up the code, so it works headless.
