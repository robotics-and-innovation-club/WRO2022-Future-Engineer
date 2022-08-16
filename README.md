# Teams from the Robotics and Innovation Club (RIC)
Darunsikkhalai School (Engineering-Science Classroom)

## Our Teams
- Kitsada      Doungjitjaroen  Supervisor / Assistance
- Theekhathat  Wongsubsantati  Member
- Theeraphat   Thongbai        Member
- Nattavee     Sunitsakul      Member

## Contents
- ```team-photos``` contains two images of our team (an official photo and one funny photo with all of our team members)
- ```video``` contains a link to a video on YouTube that demonstrates how our vehicle operates.
- ```models``` include 3D-printed replicas of our car's parts.
- ```schemes``` contains all of our schematic diagram of the electromechanical parts that show all the parts (motors, electronics, and other electromechanical components) used in the vehicle and their connections.
- ```src``` contain all of source code of our vehicle. (Python source code)

## Introduction 

### How to use
1. Prepare all electronic parts and machanic parts
2. Bring your Raspberry Pi 4 Model B, then [install Raspberry Pi OS (64-bit)](https://github.com/robotics-and-innovation-club/WRO2022-Future-Engineer#how-to-install-raspberry-pi-os)
3. Install all of required libraries 
4. [Enable I2C](https://github.com/robotics-and-innovation-club/WRO2022-Future-Engineer/blob/main/README.md#how-to-enable-i2c)


## Software / Program
All of our source code is in ```src``` directory

Our software mainly use GPIOZERO and opencv libraries. With GPIOZERO we use this library control servo motor and motor. With opencv we use this library to do computer vision.

```Actuator.py``` we use hardware PWM of Raspberry Pi 4 Model B, so that we need to run ```sudo systemctl enable pigpiod``` to enable hardware PWM to work (every time Raspberry Pi boot it will start pigpiod services automatically)

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
