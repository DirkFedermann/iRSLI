#!python3

import serial
import time
import irsdk
ser = serial.Serial('COM3', 9600, timeout=1)

class State:
    ir_connected = False
    rpm_shift_show = 0
    fuel_show = 0

def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        ir.shutdown()
        print('irsdk disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        print('irsdk connected')
def loop():
    ir.freeze_var_buffer_latest()

    rpm = ir['RPM']
    fuelPct = ir['FuelLevelPct']
    leds = "kkkkkkkkkkkk#"
    

    startRPM = 7000
    endRPM = 8700
    shiftRPM = 8850
    betweenRPM = (endRPM - startRPM) / 12

    if(rpm >= startRPM):
        leds = "gkkkkkkkkkkk#"
    if(rpm >= startRPM + (betweenRPM * 1)):
        leds = "ggkkkkkkkkkk#"
    if(rpm >= startRPM + (betweenRPM * 2)):
        leds = "gggkkkkkkkkk#"
    if(rpm >= startRPM + (betweenRPM * 3)):
        leds = "ggggkkkkkkkk#"
    if(rpm >= startRPM + (betweenRPM * 4)):
        leds = "ggggykkkkkkk#"
    if(rpm >= startRPM + (betweenRPM * 5)):
        leds = "ggggyykkkkkk#"
    if(rpm >= startRPM + (betweenRPM * 6)):
        leds = "ggggyyykkkkk#"
    if(rpm >= startRPM + (betweenRPM * 7)):
        leds = "ggggyyyykkkk#"
    if(rpm >= startRPM + (betweenRPM * 8)):
        leds = "ggggyyyyrkkk#"
    if(rpm >= startRPM + (betweenRPM * 9)):
        leds = "ggggyyyyrrkk#"
    if(rpm >= startRPM + (betweenRPM * 10)):
        leds = "ggggyyyyrrrk#"
    if(rpm >= startRPM + (betweenRPM * 11)):
        leds = "ggggyyyyrrrr#"
    if(rpm >= shiftRPM):
        if(state.rpm_shift_show <= 10):
            leds = "bbbbbbbbbbbb#"
            state.rpm_shift_show = state.rpm_shift_show + 1
        elif(state.rpm_shift_show > 10) and (state.rpm_shift_show <= 20):
            leds = "kkkkkkkkkkkk#"
            state.rpm_shift_show = state.rpm_shift_show + 1
        else:
            state.rpm_shift_show = 0

    if(fuelPct <= 10):
        if(state.fuel_show <= 10):
            leds = 'm' + leds[1:]
            state.fuel_show = state.fuel_show + 1
        elif(state.fuel_show > 10) and (state.fuel_show <= 20):
            leds = 'k' + leds[1:]
            state.fuel_show = state.fuel_show + 1
        else:
            state.fuel_show = 0
    
    ser.write(leds.encode())

    """
        startRPM = 6000
        endRPM = 8800
        shiftRPM = 8600
    """


if __name__ == '__main__':
    ir = irsdk.IRSDK()
    state = State()

    try:
        while True:
            check_iracing()
            if state.ir_connected:
                loop()
            time.sleep(.01)
    except KeyboardInterrupt:
        pass
