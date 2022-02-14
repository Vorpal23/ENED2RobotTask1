#!/usr/bin/env pybricks-micropython



from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()




motorA = Motor(Port.A,Direction.CLOCKWISE)
motorB = Motor(Port.D,Direction.CLOCKWISE)
Frame = StopWatch()
# Write your program here.
fullrotation = 8.5 #in

def go_distance(inch,speed):
    degreeperinch = 360/fullrotation
    angleMA = motorA.angle()
    angleMB = motorB.angle()


    degrees_to_go = degreeperinch* inch
    print(degrees_to_go)
    motorA.run_target(speed, angleMA+ degrees_to_go, then=Stop.HOLD, wait=False)    
    motorB.run_target(speed, angleMB+ degrees_to_go, then=Stop.HOLD, wait=True) 

    

def rotate(angle,speed):
    #180 = 291
    a = 291 *4
    angleMA = motorA.angle()
    angleMB = motorB.angle()
    motorA.run_target(speed, angleMA+ a, then=Stop.HOLD, wait=False)    
    motorB.run_target(speed, angleMB- a, then=Stop.HOLD, wait=True) 




def main():
    print('Hello World')
    Frame.reset()
    Speed = 200
    #motorA.run(Speed)
        
    #motorB.run(Speed)
    motorA.reset_angle(0)
    motorB.reset_angle(0)
    #go_distance(8.5,200)

    rotate(360,Speed)
    
    
    while True:
        
        ev3.screen.draw_text(50,50,"Hello world!")

        #motorA.run(Speed)
        #motorB.run(-Speed)


        break

        if Frame.time() > 10000  :
            motorA.hold()
            motorB.hold()
            print(motorA.angle())
            break
        
        
        
        
        
        
    

if __name__ == '__main__':
    main()
