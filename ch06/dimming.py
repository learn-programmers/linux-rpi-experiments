import RPi.GPIO as GPIO
import time

def led_dimming(led, duration, pwm_frequency=100):
    pwm = GPIO.PWM(led, pwm_frequency)

    try:
        pwm.start(0)
        for _ in range(int(duration * pwm_frequency)):
            # 밝아지는 과정
            for duty_cycle in range(0, 101, 5):
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(1 / (pwm_frequency * 2))

            # 어두워지는 과정
            for duty_cycle in range(100, -1, -5):
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(1 / (pwm_frequency * 2))
    finally:
        pwm.stop()

GPIO.setmode(GPIO.BCM)

# 사용 예시
led_pin = 2
GPIO.setup(led_pin, GPIO.OUT)
led_dimming(led_pin, 5)
GPIO.cleanup()
