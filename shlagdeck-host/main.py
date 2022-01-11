import time
import win32com.client as comctl
import serial
import sys

if not sys.platform.startswith('win'):
    print("My author was lazy, this script only works on Windows (for now). Bye now!")
    sys.exit()

wsh = comctl.Dispatch("WScript.Shell")

### Find the correct serial port. We try every port (except COM1, we already know it won't be this one for USB serial), and send "indentify", ShlagDeck will respond with its name.
### Any ports that fails to open, or does not respond to this command isn't the one we're looking for.
shlagDeckSerialPort = None
currentPort = 2
allPorts = ['COM%s' % (i + 1) for i in range(256)]
while shlagDeckSerialPort is None and currentPort <= 256:
    try:
        candidate = "COM" + str(currentPort)
        print("trying port", candidate, "...", end='')
        candidateSerial = serial.Serial(candidate, baudrate=115200)

        print("Port open, waiting a bit because otherwise it doesnt work...")
        time.sleep(2)
        print("Sending identify")
        candidateSerial.write(b"identify")

        responseRaw = candidateSerial.readline()
        responseClean = responseRaw.decode('utf-8').strip()

        print("Received", responseClean)
        if (responseClean == 'shlagdeck'):
            print ("Bingo, we've got a winner!")
            shlagDeckSerialPort = candidateSerial
        else:
            print ("Nope. Next!")
            currentPort += 1
            candidateSerial.close()
    except (OSError, serial.SerialException):
        print(" Nope! Next.")
        currentPort += 1
        pass


if shlagDeckSerialPort is None:
    print("ShlagDeck not found :( Is it plugged in?")
    sys.exit()


while True:
    rawBytes = shlagDeckSerialPort.readline()
    parsedString = rawBytes.decode('utf-8')
    cleanString = parsedString.strip()
    cleanNumber = int(cleanString)

    keyToSend = 12 + cleanNumber + 1
    keyString = '{F%d}' % keyToSend
    wsh.SendKeys(keyString)
    print("received", cleanString, ", sending:", keyString)
