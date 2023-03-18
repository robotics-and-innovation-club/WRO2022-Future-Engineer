# Teams from the Robotics and Innovation Club (RIC)
Darunsikkhalai School (Engineering-Science Classroom & KOSEN KMUTT)

## Our Teams
- Kitsada      Doungjitjaroen  Supervisor / Assistance
- Theekhathat  Wongsubsantati  Member
- Theeraphat   Thongbai        Member
- Nattavee     Sunitsakul      Member

## Contents
- ```models``` include 3D-printed replicas of our car's parts.
- ```src``` contain all of the source code of our vehicle. (Python source code)
- ```schemes``` contains all of our schematic diagrams of the electromechanical parts that show all the parts (motors, electronics, and other electromechanical components) used in the vehicle and their connections.
- ```team-photos``` contains two images of our team (an official photo and one funny photo with all of our team members)
- ```vehicle-photos``` contains 6 photos of the vehicle (from every side, from top and bottom)
- ```video``` contains a link to a video on YouTube that demonstrates how our vehicle operates.

## Introduction
How can we control electronics with the Raspberry Pi 4? We use the GPIOZERO library to control the GPIO pins of the Raspberry Pi, so that we can control motors and servos. Thanks to the hardware PWM of the Raspberry Pi 4 Model B, it helps our servo motor turn at an accurate angle as well as control the speed of the motor accurately.

How can we make the car go straight? We use computer vision to detect the environment. Then we can approximate how far the car is from the environment.

We use HSV colour space, and then we find a range of colours in the field that we will see in the competition. We need to configure the upper and lower colors, such as orange, blue, black, and white.

In the side environment, we use our upper and lower HSV of black walls. We find the filter black pixels in the upper and lower range. After that, we will filter the blue line out of this frame so that it has more accuracy in detaching black pixels of color.

On the floor, we use the same method to detect blue and orange lines. We use the upper and lower range of orange and blue colors that we found, then detect if the area has more than one consistency value that we researched to filter the error detection.

We also use computer vision to detect which turn we want when the car is initial. This method helps us go in a clockwise and counter-clockwise direction. without a struggle in any direction.

Next, we use data that our computer vision detected before to make a decision to turn left or right by how many degrees or go straight with some speed. We also use data from our 2 distance sensors to help make decisions more accurately on when to turn hard and when to stop.

Then, we use the computer vission to detect the line and count how many rounds have passed by, so that we can control how many rounds we want the car to drive automatically.

### How to use
1. Prepare all electronic parts and machanic parts
2. Bring your Raspberry Pi 4 Model B, then [install Raspberry Pi OS (64-bit)](https://github.com/robotics-and-innovation-club/WRO2022-Future-Engineer#how-to-install-raspberry-pi-os)
3. Install Python 3.10.5 and pip3
4. Install all of required libraries (GPIOZERO, openCV, adafruit-circuitpython-vl53l0x)
5. [Enable I2C](https://github.com/robotics-and-innovation-club/WRO2022-Future-Engineer/blob/main/README.md#how-to-enable-i2c)
6. Enable Hardware PWM, by run ```sudo systemctl enable pigpiod``` in terminal.
7. git clone this github repository
8. open terminal and run ```cd WRO2022-FUTURE-ENGINEER/src```
9. run ```sudo python main1.py``` or ```sudo python main2.py```


## Software / Program
All of our source code is in ```src``` directory. All of it is Python source code.

Our software mainly uses GPIOZERO and openCV libraries. With GPIOZERO, we use this library to control servo motors and motors. With openCV, we use this library to do computer vision.

```Actuator.py``` we use hardware PWM of the Raspberry Pi 4 Model B, so we need to run ```sudo systemctl enable pigpiod``` to enable hardware PWM to work (every time the Raspberry Pi boots it will start pigpiod services automatically).

```Radar_Distance_Sensor.py``` we use for getting the distance from the Radar Distance Sensor (VL53L0X). In the VL53L0X class, the get_distance method will return the distance in centimeters.

### How to install Raspberry Pi OS
1. go to ```https://www.raspberrypi.com/software/``` website, then if you are Windows user click```Download for Windows```, if you are macOS user click```Download for macOS```, if you are Ubuntu use click```Download for Ubuntu for x86```, but if you are Raspberry Pi OS user, type ```sudo apt install rpi-imager``` in a Terminal window.
2. Choose OS, In this car we use ```Raspberry Pi OS (64-bit)```
3. Choose Storage (SD-CARD)
4. (OPTIONAL) If you prefer to configure anything before installing the OS to storage, you can configure it by click ```Advcance Option``` or the gear sign (on the bottom left of the window).
5. Click ```Write```

### How to enable I2C
1. open terminal
2. type ```sudo raspi-config```
3. select ```Interfacing Options```
4. select ```I2C```
5. select ```<Yes>```
6. select ```Ok```
7. If it requires you to reboot, select ```<Yes>```


## Models
- ```base with nut hole.STL``` The STL file is the base component that will be used to attach the electronic mounter component to the vehicle base.
- ```step down mount.STL``` This is the component that will be mounted to the electronic mounter base. This is used to insert a step-down DC to DC converter.

## Electronic
- Raspberry Pi 4 Model B (OS : Raspberry Pi OS 64-bits) 1 ea.
- Battery (18650 Lithium-ion battery) 3 ea.
- USB HD Camera (720p camera) 1 ea.
- DC to DC step down converter (from 9VDC-36VDC to 5VDC-3A) 1 ea.
- Motor Driver Module (L298N) 1 ea.
- DC Motor (12VDC) 1 ea.
- Servo Motor (MG996R) 1 ea.
- Ultrasonic sensor 1 ea.
- Radar Distance sensor 1 ea.

All electronic components are wired as shown in schematic diagrams in ```schemes``` directory.
In ```schemes``` directory, ```diagram_fritzing.png``` is the property diagram from the Fritzing program, and ```Easy Diagram.pdf``` is an easy diagram of our circuit.
