import signal
import sys

def SigAlarmHandler(signal, frame) :
	print "Received alarm ....Shutting down..."
	sys.exit(0)

signal.signal(signal.SIGALRM, SigAlarmHandler)
signal.alarm(1000)

print "Starting work ... waiting for alarm to quit :) "
while True :
	# do something 
	pass
