import threading, subprocess
import RPi.GPIO as GPIO

PIN = 5 # Same as power on/resume hardwired pin --> pressing same button when powered off will start the RPi

def shutdown():
    subprocess.call('sudo shutdown -h now', shell=True)

def pressed(pin):
    t.cancel()
    subprocess.call('sudo reboot', shell=True)

def released(pin): # Button released, start timer
    t.start()


if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIN, GPIO.IN)

        GPIO.add_event_detect(5, GPIO.RISING, callback=pressed, bouncetime=12)
        GPIO.add_event_detect(5, GPIO.FALLING, callback=released, bouncetime=12)

        t = threading.Timer(3.0, shutdown)

        while True:
            pass
    finally:
        GPIO.cleanup()