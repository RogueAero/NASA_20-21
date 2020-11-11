import os
	os.format()
import xbee, time

print("Joining network as an end device...")
xbee.atcmd("NI", "End Device")
network_settings = {"CE": 0, "A1": 4, "CH": 0x13, "ID": 0x3332, "EE": 0}
for command, value in network_settings.items():
	xbee.atcmd(command, value)
xbee.atcmd("AC") # Apply changes
time.sleep(1)

while network_status() != 0:
	time.sleep(0.1)
print("Connected to Network\n")

last_sent = time.ticks_ms()
interval = 5000 # How often to send a message

# Start the transmit/receive loop
print("Sending temp data every {} seconds".format(interval/1000))
while True:
	p = xbee.receive()
	if p:
		format_packet(p)
	else:
		# Transmit temperature if ready
		if time.ticks_diff(time.ticks_ms(), last_sent) > interval:
			temp = "Temperature: {}C".format(xbee.atcmd("TP"))
			print("\tsending " + temp)
			try:
				xbee.transmit(xbee.ADDR_COORDINATOR, temp)
			except Exception as err:
				print(err)
			last_sent = time.ticks_ms()
		time.sleep(0.25)


