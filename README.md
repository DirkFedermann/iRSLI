# iRSLI
SLI for iRacing.com 
Its a SLI that consist of 12 addressable LEDs (SK6812) on a PCB that are driven by a Arduino Nano or Pro Micro.
This is a really early prototype. So expect that it will not work! - but hopefully it does.




## How To
For now you have to download Python3.x and install pyirsdk yourself.
And you have to start the application from the Python included IDE (IDLE).


### install Python and pyirSDK
Download the Python version 3 from here: https://www.python.org/downloads/windows/ and install it.
Open the commandline as administrator and type in "python -m pip install pyirsdk" and press enter.
Now Python will install PyYaml and the pyirsdk - which is needed for this application.

When thats finished you can close the commandline.


### Get the COM Port
Plugin the Arduino and go to the device-manager of windows.
Search for the Arduino (might have a different name) and open the properties and search for the COM Port and keep the number in mind.


### start the application
In order to start the application, download the "python.py" file from above.
Start IDLE (just type it into the startmenu) and/or open the .py file with it.
Change on line 6 the COM Port number save it and press F5 to run the application.

Now you should see the LEDs light up and blink. If not - you messed something up ;-)
Thats the demo/test mode.

Change the value "demo" to False to get rid of it.

Now you can start iRacing and try it for the first time.


### Changing Values for a different car
For now the RPM Range is set for the Porsche 919 LMP1.
In order to change that, you have to change the values of "startRPM", "endRPM" and "shiftRPM".
Its recommended to save the RPM ranges somewhere for future references.




## Futureplan
- Make a configfile for easier configuration
- Recognize the car and have the RPM Range select itself
- make a executable
- implement new features that my ~~guinea pig~~ alpha tester - come up with


## Changelog

### v0.1

  First commit
  
  Hardcoded RPM and Fuellevel warning for the Porsche 919
