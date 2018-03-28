#!python3

import configparser
import serial
import time
import irsdk

# Read the config file
config = configparser.ConfigParser(inline_comment_prefixes=';')
config.read('config.ini')

# Building up the Serial Connection to the Arduino
ser = serial.Serial(config['config']['COMPort'], config['config']['BaudRate'], timeout=int(config['config']['COMTimeout']))


#########################
###  Demo Mode        ###
#########################

# See if demo mode is active
demo = eval(config['config']['demoMode'])
demoShow = True

if(demo):
    while True:
        if demoShow == True:
            leds = "rgbkycmykrgb#"
            demoShow = False
        else:
            leds = "kcmyrgbrcmyk#"
            demoShow = True
        ser.write(leds.encode())
        time.sleep(.2)

		
#########################
###  Initialisation   ###
#########################

# Initialize global variables
class State:
    ir_connected = False
    rpm_shift_show = 0
    fuel_show = 0
	trackName = ""
	

	
# Check if iRacing is running
def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        ir.shutdown()
        print('irsdk disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        print('irsdk connected')
		state.trackName = ir['WeekendInfo']['TrackDisplayName']
		
		
		
##########################
### The mighty Program ###
##########################
def loop():
	# Freeze the buffer to not get any 2 different values because the API updated too soon
    ir.freeze_var_buffer_latest()

	# variables that always get reset
    fuelPct = ir['FuelLevelPct'] * 100		# fuel in percentage
    leds = ""								# reset leds
    deltaTime = int(round(ir[config['config']['DeltaTo']],1)*10)	# get deltaTime, truncate it, round it, convert to int
    
	
	#############################
	### Delta Time            ###
	#############################
	
	# if you are faster than the compared laptime
    if deltaTime < 0:
        i = 0
        while i > deltaTime:
            if deltaTime > 12:
                i = -999999999
                leds = "gggggggggggg"
            else:
                leds += "g"
                i -= 1
	# if you are slower than the compared laptime - noob
    if deltaTime > 0:
        i = 0
        while i < deltaTime:
            if deltaTime > 12:
                i = 999999999
                leds = "rrrrrrrrrrrr"
            else:
                leds += "r"
                i += 1
				
	# well, if the deltatime is 0, show nothing
    if deltaTime == 0:
        leds = "kkkkkkkkkkkk"
		
	# put as many "k" behind the leds String to get to 12 characters
    while len(leds) < 12:
        leds += "k"

		
		
	#############################
	### RPM                   ###
	#############################
    """
    startRPM = 5000
    endRPM = 6500
    shiftRPM = 6600
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
    """
	
	#############################
	### Fuel Alarm            ###
	#############################
	
	# Show only if the fuel is under the desired fuelAlarm threshold	
    if(fuelPct <= config['default']['fuelAlarm']):
		# let the led flash magenta
        if(state.fuel_show <= 10):
            leds = leds[:-1] + "m"
            state.fuel_show = state.fuel_show + 1
        elif(state.fuel_show > 10) and (state.fuel_show <= 20):
            leds = leds[:-1] + "k"
            state.fuel_show = state.fuel_show + 1
        else:
            state.fuel_show = 0

			
	#############################
	### End Stuff             ###
	#############################
    leds += "#"					# add the end character, to show the arduino that its the end of the string
    ser.write(leds.encode())	# Send the leds string to the arduino


	

if __name__ == '__main__':
    ir = irsdk.IRSDK()
    state = State()

    try:
        while True:
            check_iracing()
            if state.ir_connected:
                loop()
            time.sleep(.05)		# how often the loop will execute per second
    except KeyboardInterrupt:
        pass
