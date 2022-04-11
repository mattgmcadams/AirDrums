import bluetooth as bt

devices = bt.discover_devices(lookup_names=True)

print(devices)