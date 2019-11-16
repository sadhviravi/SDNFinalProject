from netmiko import ConnectHandler
print("Hi sadhvi!")
print("TEST")

ios_r2 = {
    'device_type': 'linux',
    'username': 'mininet',
    'password': 'mininet',
    'ip': '192.168.56.103',
}
# connecting to mininet vm
net_connect = ConnectHandler(**ios_r2)
print("connecting to mininet default topology")
print(net_connect.send_command_timing('sudo mn'))
print(net_connect.send_command_timing('mininet'))
print(net_connect.send_command_timing('sh ovs-vsctl get-controller'))
