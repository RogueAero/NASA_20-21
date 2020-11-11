import xbee, time

# Functions for receiving data
def format_eui64(addr):
	return ':'.join('%02x' % b for b in addr)
def format_packet(p):
	type = 'Broadcast' if p['broadcast'] else 'Unicast'
	print("%s message from EUI-64 %s (network 0x%04X)" % (type,
		format_eui64(p['sender_eui64']), p['sender_nwk']))
	print(" from EP 0x%02X to EP 0x%02X, Cluster 0x%04X, Profile 0x%04X:" %
		(p['source_ep'], p['dest_ep'], p['cluster'], p['profile']))
	print(p['payload'], "\n")
def network_status():
	# If the value of AI is non zero, the module is not connected to a network
	return xbee.atcmd("AI")

#Continuously receive data
while True:
	print("Receiving data...")
	print("Press CTRL+C to cancel.")
	p = xbee.receive()
	if p:
		format_packet(p)
	else:
		time.sleep(0.25) # wait 0.25 seconds before checking again





