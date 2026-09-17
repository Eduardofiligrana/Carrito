from machine import Pin, PWM
from time import sleep

# ===== CONFIGURACIÓN =====

IN1 = Pin(27, Pin.OUT)
IN2 = Pin(26, Pin.OUT)

ENA = PWM(Pin(14), freq=1000)

IN3 = Pin(25, Pin.OUT)
IN4 = Pin(33, Pin.OUT)

ENA_2 = PWM(Pin(12), freq=1000)

IN5 = Pin(18, Pin.OUT)
IN6 = Pin(19, Pin.OUT)

ENA_3 = PWM(Pin(32), freq=1000)

IN7 = Pin(5, Pin.OUT)
IN8 = Pin(4, Pin.OUT)

ENA_4 = PWM(Pin(13), freq=1000)

# ===== VELOCIDAD =====
# 0 = detenido
# 65535 = máxima velocidad

velocidad = 30000

# ===== SENTIDO =====

IN1.value(1)
IN2.value(0)

IN3.value(0)
IN4.value(1)

IN5.value(0)
IN6.value(1)

IN7.value(0)
IN8.value(1)

# ===== ENCENDER MOTOR =====

ENA.duty_u16(velocidad)

sleep(10)

ENA_2.duty_u16(velocidad)

sleep(10)

ENA_3.duty_u16(velocidad)

sleep(10)

ENA_4.duty_u16(velocidad)

sleep(10)
# ===== DETENER MOTOR =====

ENA.duty_u16(0)
IN1.value(0)
IN2.value(0)

ENA_2.duty_u16(0)
IN3.value(0)
IN4.value(0)

ENA_3.duty_u16(0)
IN5.value(0)
IN6.value(0)

ENA_4.duty_u16(0)
IN7.value(0)
IN8.value(0)