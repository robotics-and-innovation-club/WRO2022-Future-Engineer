# Teams from the Robotics and Innovation Club (RIC)
Darunsikkhalai School (Engineering-Science Classroom)

## Our Teams
- Kitsada      Doungjitjaroen  Supervisor / Assistance
- Theekhathat  Wongsubsantati  Member
- Theeraphat   Thongbai        Member
- Nattavee     Sunitsakul      Member

## Contents
- ```models``` include 3D-printed replicas of our car's parts.
- ```src``` contain all of source code of our vehicle. (Python source code)
- ```schemes``` contains all of our schematic diagram of the electromechanical parts that show all the parts (motors, electronics, and other electromechanical components) used in the vehicle and their connections.
- ```team-photos``` contains two images of our team (an official photo and one funny photo with all of our team members)
- ```vehicle-photos``` contains 6 photos of the vehicle (from every side, from top and bottom)
- ```video``` contains a link to a video on YouTube that demonstrates how our vehicle operates.

## Introduction 
How can we make the car go straight, We use computer vision to detect side environment. Then wew can approximate how far is teh car from the enviroment. 

We use HSV colour space then we find a range of colour in the feild that we will met on the competition. we need to config the upper and lowwer of color such as Orange, Blue, Black, White

Side environment we use our upper and lower HSV of black wall that we find the filter black pixel that in upper and lower range. after that we will filter blue line out of this frame so that it have more accuracy of detcting black pixel of colour

On floor we use the same method to detect Blue and Orange line, we use upper and lower of Orange and Blue color that we found, then detct if the area is more than one constance value that we research to filter the error detection. 

We also use computer vision to detect with turn do we wnat when the car init. This method help our can can go in clock wise and counter clock wise direction. with out strugle in any direction

Next, We use data that our computer vision detected before to make a decision to turn left or right how many degree. or go straight with some speed. we also use data from our 2 distance sensor to help making decision more accurate, on when to turn hard when to stop.

Then, we use the computer vission to detect line and count how many round do counting round that pass by, so that we can control how many round that we want the car to drive automaticaly.

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
All of our source code is in ```src``` directory

Our software mainly use GPIOZERO and opencv libraries. With GPIOZERO we use this library control servo motor and motor. With opencv we use this library to do computer vision.

```Actuator.py``` we use hardware PWM of Raspberry Pi 4 Model B, so that we need to run ```sudo systemctl enable pigpiod``` to enable hardware PWM to work (every time Raspberry Pi boot it will start pigpiod services automatically)

```Radar_Distance_Sensor.py``` we use for getting distance from Radar Distance Sensor (VL53L0X). In VL53L0X class, get_distance medthod will return distance in centimeter.

### How to install Raspberry Pi OS
1. go to ```https://www.raspberrypi.com/software/``` website, then if you are Windows user click```Download for Windows```, if you are macOS user click```Download for macOS```, if you are Ubuntu use click```Download for Ubuntu for x86```, but if you are Raspberry Pi OS user, type ```sudo apt install rpi-imager``` in a Terminal window.
2. Choose OS, In this car we use ```Raspberry Pi OS (64-bit)```
3. Choose Storage (SD-CARD)
4. (OPTIONAL) If you prefer to config any thing before install OS to storage, you can config it by click ```Advcance Option``` or the gear sign (on the bottom left of the window)
5. Click ```Write```

### How to enable I2C
1. open terminal
2. type ```sudo raspi-config```
3. select ```Interfacing Options```
4. select ```I2C```
5. select ```<Yes>```
6. select ```Ok```
7. if it required you to reboot, select ```<Yes>```


## Models
- ```base with nut hole.STL``` The STL file is the base component that will be used to attach the electronic mounter component to the vehicle base.
- ```step down mount.STL``` The component that will be mounted to the electronic mounter base is this. This is used to insert a step-down DC to DC converter.

## Electronic
- Raspberry Pi 4 Model B (OS : Raspberry Pi OS 64-bits) 1 ea. 
- Battery (18650 Lithium-ion battery) 3 ea.
- USB HD Camera (720p camera) 1 ea.
- DC to DC step down converter (from 9VDC - 36VDC to 5VDC 3A) 1 ea.
- Motor Driver Module (L298N) 1 ea.
- DC Motor (12VDC) 1 ea.
- Servo Motor (MG996R) 1 ea.
- Ultrasonic sensor 1 ea.
- Radar Distance sensor 1 ea.

How all electronic components are wired show in schematic diagrams in ```schemes``` directory.
In ```schemes``` directory, ```diagram_fritzing.png``` is the property diagram from Fritzing program and ```Easy Diagram.pdf``` is a easy diagram of our circuit.
