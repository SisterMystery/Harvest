import serial, sys


try:
	DarkSerial = serial.Serial("/dev/ttyUSB0")
except Exception as e1:
	print e1
	try:
		DarkSerial = serial.Serial("/dev/ttyUSB1")
	except Exception as e:
		print "Threre seems to be a serial problem: ", e
		sys.exit()

DarkSerial.timeout = .01
DarkSerial.baudrate = 9600
def getInputList(port):
	port.flushInput()
	byte = port.readline()
	if not byte: byte = 0
	try:
		byte = int(byte)
	except:
		byte = 0
	inlist = []
	for i in range(8):
		if pow(2,i) & byte:
			inlist.append(1)
		else:
			inlist.append(0)
	print inlist	
	return inlist
	



#while(1):	
#	getInputList(DarkSerial)
