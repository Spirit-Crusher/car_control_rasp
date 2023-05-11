import RPi.GPIO as GPIO
from time import sleep

# pin definitions
front_in1 = 4
front_in2 = 5
front_in3 = 23
front_in4 = 24
front_enB = 17
front_enA = 25

rear_in1 = 26
rear_in2 = 6
rear_in3 = 27
rear_in4 = 22
rear_enB = 16
rear_enA = 8

temp1 = 1


# setting pin mode for all pins
GPIO.setmode(GPIO.BCM)

    # front motors
GPIO.setup(front_in1, GPIO.OUT)
GPIO.setup(front_in2, GPIO.OUT)
GPIO.setup(front_in3, GPIO.OUT)
GPIO.setup(front_in4, GPIO.OUT)
GPIO.setup(front_enA, GPIO.OUT)
GPIO.setup(front_enB, GPIO.OUT)
GPIO.output(front_in1, GPIO.LOW)
GPIO.output(front_in2, GPIO.LOW)
GPIO.output(front_in3, GPIO.LOW)
GPIO.output(front_in4, GPIO.LOW)
front_pA = GPIO.PWM(front_enA, 1000)
front_pA.start(25)
front_pB = GPIO.PWM(front_enB, 1000)
front_pB.start(25)

    # rear motors
GPIO.setup(rear_in1, GPIO.OUT)
GPIO.setup(rear_in2, GPIO.OUT)
GPIO.setup(rear_in3, GPIO.OUT)
GPIO.setup(rear_in4, GPIO.OUT)
GPIO.setup(rear_enA, GPIO.OUT)
GPIO.setup(rear_enB, GPIO.OUT)
GPIO.output(rear_in1, GPIO.LOW)
GPIO.output(rear_in2, GPIO.LOW)
GPIO.output(rear_in3, GPIO.LOW)
GPIO.output(rear_in4, GPIO.LOW)
rear_pA = GPIO.PWM(rear_enA, 1000)
rear_pA.start(25)
rear_pB = GPIO.PWM(rear_enB, 1000)
rear_pB.start(25)


# motor pin listing (list position 0 represents GND pin and position 1 represents VCC pin)
front_left_motor = [front_in2, front_in1]
front_right_motor = [front_in4, front_in3]
rear_left_motor = [rear_in2, rear_in1]
rear_right_motor = [rear_in4, rear_in3]


# function definitions
def forward_move():
    
    # all motors forward
    GPIO.output(front_left_motor[1], GPIO.HIGH)
    GPIO.output(front_left_motor[0], GPIO.LOW)
    GPIO.output(front_right_motor[1], GPIO.HIGH)
    GPIO.output(front_right_motor[0], GPIO.LOW)
    GPIO.output(rear_left_motor[1], GPIO.HIGH)
    GPIO.output(rear_left_motor[0], GPIO.LOW)
    GPIO.output(rear_right_motor[1], GPIO.HIGH)
    GPIO.output(rear_right_motor[0], GPIO.LOW)


def backwards_move():

    # all motors backward
    GPIO.output(front_left_motor[1], GPIO.LOW)
    GPIO.output(front_left_motor[0], GPIO.HIGH)
    GPIO.output(front_right_motor[1], GPIO.LOW)
    GPIO.output(front_right_motor[0], GPIO.HIGH)
    GPIO.output(rear_left_motor[1], GPIO.LOW)
    GPIO.output(rear_left_motor[0], GPIO.HIGH)
    GPIO.output(rear_right_motor[1], GPIO.LOW)
    GPIO.output(rear_right_motor[0], GPIO.HIGH)


# def quad1_move():

# def quad2_move():

# def quad3_move():

# def quad4_move():


def clock_move():

    # left forward & right backward
    GPIO.output(front_left_motor[1], GPIO.HIGH)
    GPIO.output(front_left_motor[0], GPIO.LOW)
    GPIO.output(rear_right_motor[1], GPIO.LOW)
    GPIO.output(rear_right_motor[0], GPIO.HIGH)
    GPIO.output(front_right_motor[1], GPIO.LOW)
    GPIO.output(front_right_motor[0], GPIO.HIGH)
    GPIO.output(rear_left_motor[1], GPIO.HIGH)
    GPIO.output(rear_left_motor[0], GPIO.LOW)


def anticlock_move():

    # right forward & left backward
    GPIO.output(front_right_motor[1], GPIO.HIGH)
    GPIO.output(front_right_motor[0], GPIO.LOW)
    GPIO.output(rear_left_motor[1], GPIO.LOW)
    GPIO.output(rear_left_motor[0], GPIO.HIGH)
    GPIO.output(front_left_motor[1], GPIO.LOW)
    GPIO.output(front_left_motor[0], GPIO.HIGH)
    GPIO.output(rear_right_motor[1], GPIO.HIGH)
    GPIO.output(rear_right_motor[0], GPIO.LOW)


def stop_move():

    # all motors off
    GPIO.output(front_left_motor[1], GPIO.LOW)
    GPIO.output(front_left_motor[0], GPIO.LOW)
    GPIO.output(front_right_motor[1], GPIO.LOW)
    GPIO.output(front_right_motor[0], GPIO.LOW)
    GPIO.output(rear_left_motor[1], GPIO.LOW)
    GPIO.output(rear_left_motor[0], GPIO.LOW)
    GPIO.output(rear_right_motor[1], GPIO.LOW)
    GPIO.output(rear_right_motor[0], GPIO.LOW)


# start message
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward r-clockwise rotation a-anti clockwise rotation l-low m-medium h-high e-exit")
print("\n")

# motor control loop
while(1):

    keyboard_in = input()

    if keyboard_in == 'r':
        print("run")
        if(temp1 == 1):
            forward_move()
            print("forward")
            keyboard_in = 'z'
        else:
            backwards_move()
            print("backward")
            keyboard_in = 'z'

    elif keyboard_in == 's':
        stop_move()
        print("stop")
        keyboard_in = 'z'

    elif keyboard_in == 'f':
        forward_move()
        print("forward")
        temp1 = 1
        keyboard_in = 'z'

    elif keyboard_in == 'b':
        backwards_move()
        print("backward")
        temp1 = 0
        keyboard_in = 'z'

    elif keyboard_in == 'r':
        clock_move()
        print("clockwise rotation")
        keyboard_in = 'z'

    elif keyboard_in == 'a':
        anticlock_move()
        print("anti-clockwise rotation")
        keyboard_in = 'z'

    elif keyboard_in == 'l':
        print("low")
        front_pA.ChangeDutyCycle(25)
        front_pB.ChangeDutyCycle(25)
        rear_pA.ChangeDutyCycle(25)
        rear_pB.ChangeDutyCycle(25)
        keyboard_in = 'z'

    elif keyboard_in == 'm':
        print("medium")
        front_pA.ChangeDutyCycle(50)
        front_pB.ChangeDutyCycle(50)
        rear_pA.ChangeDutyCycle(50)
        rear_pB.ChangeDutyCycle(50)
        keyboard_in = 'z'

    elif keyboard_in == 'h':
        print("high")
        front_pA.ChangeDutyCycle(75)
        front_pB.ChangeDutyCycle(75)
        rear_pA.ChangeDutyCycle(75)
        rear_pB.ChangeDutyCycle(75)
        keyboard_in = 'z'
    
    elif keyboard_in == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
