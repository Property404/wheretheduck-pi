import time
import RPi.GPIO as GPIO
from clocko import*
GPIO.setmode(GPIO.BOARD)

_forward = 11
_backward = 8
_right = 5
_left = 10
_stop = 7

_last_stop = 0

_all_pins = [_forward, _backward, _right, _left, _stop]

_current_pin = None

for pin in _all_pins:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)

def _sleep():
    time.sleep(1)

def _turnPinOn(pin_num):
    GPIO.output(pin_num, GPIO.HIGH)
def _turnPinOff(pin_num):
    global _current_pin
    GPIO.output(pin_num, GPIO.LOW)
    if pin_num == _current_pin:
        _current_pin = None
def _turnAllPinsOff():
    for pin in _all_pins:
        _turnPinOff(pin)

_bytes = 2

def _dothedo(pin):
    global _current_pin
    if pin != _stop:
        stop()
    while ui[ 
    _turnAllPinsOff()
    _turnPinOn(pin)
    _current_pin = pin

def stop():
    _last_stop = getTime()
    if not hasStopped():
        _dothedo(_stop)

def moveForward():
    if not movingForward():
        _dothedo(_forward)

def moveBackward():
    if not movingBackward():
        _dothedo(_backward)

def rotateLeft():
    if not rotatingLeft():
        _dothedo(_left)

def rotateRight():
    if not rotatingRight():
        _dothedo(_right)

def hasStopped():
    return _current_pin == _stop

def movingForward():
    return _current_pin == _forward

def movingBackward():
    return _current_pin == _backward

def rotatingLeft():
    return _current_pin == _left

def rotatingRight():
    return _current_pin == _right

stop()

