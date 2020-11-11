# Transmit custom messages to all nodes
# Perform a network discovery to gather destination address:
print("Discovering remote nodes, please wait...")
node_list = list(xbee.discover())
if not node_list:
	raise Exception("Network discovery did not find any remote devices")

for node in node_list:
	dest_addr = node['sender_nwk'] # 'sender_eui64' can also be used
	dest_node_id = node['node_id']
	payload_data = "Hello, " + dest_node_id + "!"

	try:
		print("Sending \"{}\" to {}".format(payload_data, hex(dest_addr)))
		xbee.transmit(dest_addr, payload_data)
	except Exception as err:
		print(err)

print("complete")