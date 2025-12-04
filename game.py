#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
touch = TouchSensor(Port.S1)
remote = InfraredSensor(Port.S2)

def reveal():
    motor_a.run_angle(-200, -200)
    sleep(1)
    motor_a.run_angle(-200, 200)
    sleep(1)

def level1(): # Persönliche merkthilfe. erste zahl geschwindigkeit und zweite zahl winkel
    motor_b.run_angle(100, 233) 
    motor_b.run_angle(-100, 53)
    sleep(2)
    motor_c.run_angle(100, 233)
    motor_c.run_angle(-100, 52)
    sleep(2)
    motor_c.run_angle(100, 233)
    motor_c.run_angle(-100, 52)
    sleep(2)
    motor_b.run_angle(100, 233)
    motor_b.run_angle(-100, 52)
    sleep(2)

def level2():
    motor_b.run_angle(200, 233)
    motor_b.run_angle(-200, 52)
    sleep(1)
    motor_c.run_angle(200, 233)
    motor_c.run_angle(-250, 52)
    sleep(1)
    motor_c.run_angle(200, 233)
    motor_c.run_angle(-200, 52)
    sleep(1)
    motor_b.run_angle(200, 420)
    motor_b.run_angle(-200, 60)
    sleep(1)

def level3():
    motor_b.run_angle(250, 233)
    motor_b.run_angle(-250, 52)
    sleep(1)
    motor_c.run_angle(250, 233)
    motor_c.run_angle(-250, 52)
    sleep(1)
    motor_c.run_angle(250, 233)
    motor_c.run_angle(-250, 52)
    sleep(1)
    motor_b.run_angle(250, 420)
    motor_b.run_angle(-250, 60)
    sleep(1)

    motor_b.run_angle(-250, 233)
    motor_b.run_angle(250, 52)
    sleep(1)
    motor_c.run_angle(-250, 233)
    motor_c.run_angle(250, 52)
    sleep(1)
    motor_c.run_angle(-250, 233)
    motor_c.run_angle(250, 52)
    sleep(1)
    motor_b.run_angle(-250, 420)
    motor_b.run_angle(250, 60)
    sleep(1)

def level4():
    motor_c.run_angle(-350, 233)
    motor_c.run_angle(350, 52)
    sleep(1)
    motor_b.run_angle(350, 233)
    motor_b.run_angle(-350, 52)
    sleep(1)
    motor_b.run_angle(350, 233)
    motor_b.run_angle(-350, 52)
    sleep(1)
    motor_c.run_angle(-350, 420)
    motor_c.run_angle(350, 60)
    sleep(1)

    motor_c.run_angle(350, 233)
    motor_c.run_angle(-350, 52)
    sleep(1)
    motor_c.run_angle(350, 233)
    motor_c.run_angle(-350, 52)
    sleep(1)
    motor_b.run_angle(-350, 233)
    motor_b.run_angle(350, 52)
    sleep(1)
    motor_b.run_angle(-350, 420)
    motor_b.run_angle(350, 60)
    sleep(1)

def right_animation():
    ev3.screen.clear()
    ev3.screen.print("RICHTIG!")
    sleep(1)

def wrong_animation():
    ev3.screen.clear()
    ev3.screen.print("FALSCH!")
    sleep(1)

def player_choice_level1():
    ev3.screen.clear()
    ev3.screen.print("Wähle Links/Mitte/Rechts")
    ev3.screen.print("Links = LeftUp \nMitte = LeftDown \nRechts = RightUp")

    while True:
        buttons = remote.buttons(1)
        if Button.LEFT_UP in buttons:
            motor_b.run_angle(100, 233)
            motor_b.run_angle(-100, 52)
            sleep(2)
            wrong_animation()
            return "A"
        if Button.LEFT_DOWN in buttons:
            right_animation()
            return "B"
        if Button.RIGHT_UP in buttons:
            motor_c.run_angle(100, 233)
            motor_c.run_angle(-100, 52)
            sleep(2)
            wrong_animation()
            return "C"

def player_choice_level2():
    ev3.screen.clear()
    ev3.screen.print("Wähle Links/Mitte/Rechts")
    ev3.screen.print("Links = LeftUp \nMitte = LeftDown \nRechts = RightUp")

    while True:
        buttons = remote.buttons(1)
        if Button.LEFT_UP in buttons:
            motor_b.run_angle(100, 233) 
            motor_b.run_angle(-100, 52)
            sleep(2)
            right_animation()
            return "A"
        if Button.LEFT_DOWN in buttons:
            wrong_animation()
            return "B"
        if Button.RIGHT_UP in buttons:
            motor_c.run_angle(100, 233)
            motor_c.run_angle(-100, 52)
            sleep(2)
            wrong_animation()
            return "C"

def player_choice_level3():    
    ev3.screen.clear()
    ev3.screen.print("Wähle Links/Mitte/Rechts")
    ev3.screen.print("Links = LeftUp \nMitte = LeftDown \nRechts = RightUp")
    while True:
        buttons = remote.buttons(1)
        if Button.LEFT_UP in buttons:
            motor_b.run_angle(100, 233) 
            motor_b.run_angle(-100, 52)
            sleep(2)
            wrong_animation()
            return "A"
        if Button.LEFT_DOWN in buttons:
            right_animation()
            return "B"
        if Button.RIGHT_UP in buttons:
            motor_c.run_angle(100, 233)
            motor_c.run_angle(-100, 52)
            sleep(2)
            wrong_animation()
            return "C"

def player_choice_level4():    
    ev3.screen.clear()
    ev3.screen.print("Wähle Links/Mitte/Rechts")
    ev3.screen.print("Links = LeftUp \nMitte = LeftDown \nRechts = RightUp")
    while True:
        buttons = remote.buttons(1)
        if Button.LEFT_UP in buttons:
            motor_b.run_angle(100, 233) 
            motor_b.run_angle(-100, 52)
            sleep(2)
            wrong_animation()
            return "A"
        if Button.LEFT_DOWN in buttons:
            wrong_animation()
            return "B"
        if Button.RIGHT_UP in buttons:
            motor_c.run_angle(100, 233)
            motor_c.run_angle(-100, 52)
            sleep(2)
            right_animation()
            return "C"

def choose_level():
    ev3.screen.clear()
    ev3.screen.print("Level 1 = Left Up")
    ev3.screen.print("Level 2 = Left Down")
    ev3.screen.print("Level 3 = Right Up")
    ev3.screen.print("Level 4 = Right Down")
    sleep(1)

    buttons = remote.buttons(1)

    if Button.LEFT_UP in buttons:
        ev3.screen.clear()
        ev3.screen.print("Level 1 gewählt")
        sleep(2)
        if touch.pressed():
            ev3.screen.print("Level 1")
            ev3.screen.print("gestartet")
            level1()
            player_choice_level1()
            reveal()

    if Button.LEFT_DOWN in buttons:
        ev3.screen.clear()
        ev3.screen.print("Level 2 gewählt")
        sleep(2)
        if touch.pressed():
            ev3.screen.print("Level 2")
            ev3.screen.print("gestartet")
            level2()
            player_choice_level2()
            reveal()

    if Button.RIGHT_UP in buttons:
            ev3.screen.clear()
            ev3.screen.print("Level 3 gewählt")
            sleep(2)
            if touch.pressed():
                ev3.screen.print("Level 3")
                ev3.screen.print("gestartet")
                level3()
                player_choice_level3()
                reveal()

    if Button.RIGHT_DOWN in buttons:
            ev3.screen.clear()
            ev3.screen.print("Level 4 gewählt")
            sleep(2)
            if touch.pressed():
                ev3.screen.print("Level 4")
                ev3.screen.print("gestartet")
                level4()
                player_choice_level4()
                reveal()


while True:
    choose_level()
    motor_a.stop()
    motor_b.stop()
    motor_c.stop()