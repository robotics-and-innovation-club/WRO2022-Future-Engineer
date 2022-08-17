import gpiozero as gpio
from gpiozero.pins.pigpio import PiGPIOFactory
import cv2
import numpy as np
import time
from gpiozero import DistanceSensor
from Actuator import *
from Ultrasonic import *

safe = 40
e_old = None
count = 0

lowBl = np.array([111, 80, 78]) 
upBl = np.array([179, 255, 255])

lowOl = np.array([0, 38, 145]) 
upOl = np.array([179, 255, 255])

lowgreen = np.array([52, 72, 107])  
upgreen = np.array([92, 134, 196])  

lowyellow = np.array([27, 167, 99]) 
upyellow = np.array([42, 255, 231])

lowred = np.array([0, 135, 50])  
upred = np.array([8, 255, 255])

lowred1 = np.array([165, 135, 50]) 
upred1 = np.array([180, 255, 255])

lowfl = np.array([100, 0, 151])
upfl = np.array([179, 255, 255])

lowwall = np.array([0, 0, 0])
upwall = np.array([179, 255, 50])

lowbitb = np.array([100,150,0])
upbitb = np.array([140,255,255])

xright21, yright21 = 430, 230
xright22, yright22 = 640, 270

xleft11, yleft11 = 0, 230
xleft12, yleft12 = 210, 270

xright41, yright41 = 590, 205
xright42, yright42 = 640, 230

xleft31, yleft31 = 0, 205
xleft32, yleft32 = 50, 230

xBl1, yBl1 = 320, 345
xBl2, yBl2 = 390, 405

xOl1, yOl1 = 250, 345
xOl2, yOl2 = 320, 405

xObj1, yObj1 = 110, 140
xObj2, yObj2 = 530, 330

xAbove1 , yAbove1 = 251, 20
xAbove2 , yAbove2 = 389, 190

#[0, 54, 2], [179, 255, 255]

def black_line(frame):  
    global xright21, yright21, xright22, yright22, xAbove1, yAbove1, xAbove2, yAbove2, left_track, right_track, mid_track,yleft11,yleft12, xleft11,xleft12
   
    datb1 = frame[yleft11:yleft12, xleft11:xleft12]
  
    dat1 = cv2.GaussianBlur(datb1, (5, 5), cv2.BORDER_DEFAULT)
 
    hsv = cv2.cvtColor(dat1, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, lowwall, upwall )

    bmask = cv2.inRange(hsv.copy(), lowOl, upOl)

    bmask1 = cv2.inRange(hsv.copy(), lowbitb, upbitb)

    bmask2 = cv2.inRange(hsv.copy(), lowfl, upfl)

    bmask3 = cv2.bitwise_or(bmask, bmask1)

    bmask4 = cv2.bitwise_or(bmask3, bmask2)

    maskd1 = cv2.bitwise_and(mask1, cv2.bitwise_not(bmask4))

    gray11 = cv2.cvtColor(maskd1, cv2.COLOR_GRAY2BGR)
   
    frame[yleft11:yleft12, xleft11:xleft12] = gray11


    contoursd1,_ = cv2.findContours(
        maskd1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  
    track1 = 0
    max1 = 0
    for contorb1 in contoursd1:
        
        x1, y1, w1, h1 = cv2.boundingRect(contorb1)
        a1 = cv2.contourArea(contorb1)  
       
        if a1 > 200 and a1 / (h1 * w1) > 0.3 and a1 > max1:
            track1 = h1 * (x1 + w1) 
            max1 = a1  
            cv2.rectangle(datb1, (x1, y1), (x1 + w1, y1 + h1),
                          (255, 0, 0), 2)  

   
    datb2 = frame[yright21:yright22, xright21:xright22]
    
    dat2 = cv2.GaussianBlur(datb2, (9, 9), cv2.BORDER_DEFAULT)
    
    hsv2 = cv2.cvtColor(dat2, cv2.COLOR_BGR2HSV)

    mask2 = cv2.inRange(hsv2, lowwall, upwall )

    bmask_ = cv2.inRange(hsv2.copy(), lowOl, upOl)

    bmask1_ = cv2.inRange(hsv2.copy(), lowbitb, upbitb)

    bmask2_ = cv2.inRange(hsv2.copy(), lowfl, upfl)

    bmask3_ = cv2.bitwise_or(bmask_, bmask1_)

    bmask4_ = cv2.bitwise_or(bmask3_, bmask2_)

    maskd2 = cv2.bitwise_and(mask2, cv2.bitwise_not(bmask4_))

    gray12 = cv2.cvtColor(maskd2, cv2.COLOR_GRAY2BGR)
   
    frame[yright21:yright22, xright21:xright22] = gray12

    contoursd2,_ = cv2.findContours(
        maskd2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
    track2 = 0
    max2 = 0
    for contorb2 in contoursd2:
       
        x1, y1, w1, h1 = cv2.boundingRect(contorb2)
        a1 = cv2.contourArea(contorb2)  
        
        if a1 > 200 and a1 / (h1 * w1) > 0.3 and a1 > max2:
            track2 = h1 * (250 - x1)  
            max2 = a1 
            cv2.rectangle(datb2, (x1, y1), (x1 + w1, y1 + h1),
                          (255, 0, 0), 2)
    
    
   
    # datb3 = frame[yAbove1:yAbove2, xAbove1:xAbove2]
    
    # dat3 = cv2.GaussianBlur(datb3, (9, 9), cv2.BORDER_DEFAULT)
    
    # hsv3 = cv2.cvtColor(dat3, cv2.COLOR_BGR2HSV)

    # mask3 = cv2.inRange(hsv3, lowwall, upwall )

    # bmask__ = cv2.inRange(hsv3.copy(), lowOl, upOl)

    # bmask1__ = cv2.inRange(hsv3.copy(), lowbitb, upbitb)

    # bmask2__ = cv2.inRange(hsv3.copy(), lowfl, upfl)

    # bmask3__ = cv2.bitwise_or(bmask__, bmask1__)

    # bmask4__ = cv2.bitwise_or(bmask3__, bmask2__)

    # maskd3 = cv2.bitwise_and(mask3, cv2.bitwise_not(bmask4__))

    # gray13 = cv2.cvtColor(maskd3, cv2.COLOR_GRAY2BGR)
   
    # frame[yAbove1:yAbove2, xAbove1:xAbove2] = gray13

    # contoursd3,_ = cv2.findContours(
    #     maskd3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
    # track3 = 0
    # max3 = 0
    # for contorb3 in contoursd3:
       
    #     x1, y1, w1, h1 = cv2.boundingRect(contorb3)
    #     a1 = cv2.contourArea(contorb3)  
        
    #     if a1 > 200 and a1 / (h1 * w1) > 0.3 and a1 > max2:
    #         track3 = h1 *(x1-251+w1)
    #         max3 = a1 
    #         cv2.rectangle(datb3, (x1, y1), (x1 + w1, y1 + h1),
    #                       (255, 0, 0), 2)
            
    
    left_track = int(track1/98)
    right_track = int(track2/98)
    # mid_track = -(int(track3/100))


def blue_line(frame): 
    global max2, yBl1, yBl2, xBl1, xBl2, Blueline, timeB
    line = frame[yBl1:yBl2, xBl1:xBl2]
    cv2.rectangle(frame, (xBl1, yBl1), (xBl2, yBl2),
                  (0, 0, 255), 2) 
    dat1 = cv2.GaussianBlur(line, (5, 5), cv2.BORDER_DEFAULT)
   
    hsv = cv2.cvtColor(dat1, cv2.COLOR_BGR2HSV)
   
    mask = cv2.inRange(hsv, lowBl, upBl)
   
    contours,_ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  
    max2 = 0
    for contor in contours: 
     
        x1, y1, w1, h1 = cv2.boundingRect(contor)
        a1 = cv2.contourArea(contor) 
        if a1 > 100: 
            cv2.rectangle(line, (x1, y1), (x1 + w1, y1 + h1),
                          (0, 255, 0), 2) 
            timeB = time.time()
            
            Blueline = True
         


def orange_line(frame): 
    global max2, yOl1, yOl2, xOl1, xOl2, Orangeline, timeO
   
    line = frame[yOl1:yOl2, xOl1:xOl2]
    cv2.rectangle(frame, (xOl1, yOl1), (xOl2, yOl2), (0, 0, 255),
                  2)  
    dat1 = cv2.GaussianBlur(line, (5, 5), cv2.BORDER_DEFAULT)
  
    hsv = cv2.cvtColor(dat1, cv2.COLOR_BGR2HSV)
   
    mask = cv2.inRange(hsv, lowOl, upOl)
   
    rmask = cv2.inRange(hsv.copy(), lowObjred, upObjred)
   
    rmask2 = cv2.inRange(hsv.copy(), lowObjred1, upObjred1)
   
    rmask3 = cv2.bitwise_or(rmask, rmask2)
  
    mask2 = cv2.bitwise_and(mask, cv2.bitwise_not(rmask3))
   
    contours,_ = cv2.findContours(
        mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  
    max2 = 0
    for contor in contours:
       
        x1, y1, w1, h1 = cv2.boundingRect(contor)
        a1 = cv2.contourArea(contor) 
        if a1 > 100: 
            cv2.rectangle(line, (x1, y1), (x1 + w1, y1 + h1),
                          (0, 255, 0), 2)
            timeO = time.time()
            Orangeline = True

LowBlue2 = np.array([111, 80, 78])  
UpBlue2 = np.array([124, 164, 141])

LowOrange2 = np.array([0, 38, 145])  
UpOrange2 = np.array([13, 223, 192])


def track_line(frame):
    global LowBlue2, UpBlue2, LowOrange2, UpOrange2, Blue_Line, Orange_Line
    trackline = frame[270:530,100:540]
    cv2.rectangle(frame, (100, 270), (540, 530), (0, 0, 255), 2)
    dat1 = cv2.GaussianBlur(trackline, (5, 5), cv2.BORDER_DEFAULT)
    hsv1 = cv2.cvtColor(dat1.copy(), cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(dat1.copy(), cv2.COLOR_BGR2HSV)
    maskdB = cv2.inRange(hsv1,LowBlue2,UpBlue2)
    maskdO = cv2.inRange(hsv2,LowOrange2,UpOrange2)
    contoursdB, _ = cv2.findContours(maskdB, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contoursdO, _ = cv2.findContours(maskdO, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   
    for contorb1 in contoursdO:
        x, y, w, h = cv2.boundingRect(contorb1)
        a1 = cv2.contourArea(contorb1)
        if a1 > 500:
            cv2.rectangle(trackline, (x, y), (x + w, y + h), (0, 0, 255), 2)
            Orange_Line = True
                     
    for contorb1 in contoursdB:
            x, y, w, h = cv2.boundingRect(contorb1)
            a1 = cv2.contourArea(contorb1)
            if a1 > 500:
                cv2.rectangle(trackline, (x, y), (x + w, y + h), (255, 0, 0), 2)
                Blue_Line = True

def count_line(frame):
    global LowOrange2, UpOrange2, timeO
    trackline = frame[270:530,100:540]
    dat1 = cv2.GaussianBlur(trackline, (5, 5), cv2.BORDER_DEFAULT)
    hsv1 = cv2.cvtColor(dat1.copy(), cv2.COLOR_BGR2HSV)
    maskdO = cv2.inRange(hsv1,LowOrange2,UpOrange2)
    contoursdO, _ = cv2.findContours(maskdO, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   
    for contorb1 in contoursdO:
        x, y, w, h = cv2.boundingRect(contorb1)
        a1 = cv2.contourArea(contorb1)
        if a1 > 100:
            cv2.rectangle(trackline, (x, y), (x + w, y + h), (0, 0, 0), 2)
            timeO = time.time()
            

def blue_tr():
    global e, ul, ul_need_turn
    if e==0 and ul_need_turn:
        car.left(40,25)
    elif e<0:
        car.left(15,15)
    elif e>40:
        car.right(15,15)

def orange_tr():
    global e, ul, ul_need_turn
    if e==0 and ul_need_turn:
        car.right(40,25)
    elif e>0:
        car.right(15,15)
    elif e<-40:
        car.left(15,15)


Orange_Line = False
Blue_Line = False

car = Car()
car.right(30,0)
cap = cv2.VideoCapture(0)
ultrasonic = gpio.DistanceSensor(echo=27, trigger=17,max_distance=5)
ul_need_turn = None
last_ul_need_turn = None
cam_near_right = None
cam_near_right = None
init = True
direction = None
turn_cycle = 0
timeO_old = 0
timeO = 0

sen = VL53L0X()

while init:
    car.straight_forward(15)
    _, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    track_line(frame)
    if Blue_Line and not Orange_Line:
        direction = True
        init = False
    elif Orange_Line and not Blue_Line:
        direction = False
        init = False
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


while 1:
     
    _, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
   
    black_line(frame)
    track_line(frame)
    count_line(frame)
    # if Blueline and Orangeline:
    #     count+=1
    #     Blueline = False
    #     Orangeline = False
    #     print(count)
    # Orangeline = False
    # print(Blueline,Orangeline)

    e = left_track-right_track
    print(e)
    if -5 < e < 5:
        e=0
        
    ul = sen.get_distance()+10
    
    car.straight_forward(22) #เซฟโซนปลอดภัยๆ
    if ul<55:
          ul_need_turn = True
    
    else :
          ul_need_turn = False

    if direction:
        blue_tr()
    else:
        orange_tr()
        
    if timeO-timeO_old>1.5:
        turn_cycle+=1
        print("turn cycle", turn_cycle)

    timeO_old = timeO

    # if ul_need_turn:
    #     ang = 40
    #     spe = 25
    #     if direction:
    #         car.left(ang,spe)
    #     else:
    #         car.right(ang,spe)
    # if not ul_need_turn and last_ul_need_turn:
    #     turn_cycle += 1
    #     print("turn cycle", turn_cycle)
    # if last_ul_need_turn != ul_need_turn:
    #     last_ul_need_turn = ul_need_turn

    if turn_cycle>=12:
        if direction:
           car.left(25,25)
           time.sleep(1.5)
           car.stop()
           break
        else:
           car.right(25,25)
           time.sleep(1.5)
           car.stop()
           break
            

    # if count==12:
    #     time.sleep(2)
    #     car.stop()
    #     break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        car.stop()
        break


