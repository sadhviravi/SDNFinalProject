#from netmiko import ConnectHandler
import subprocess
print("Hi sadhvi!")
print("TEST")

# connecting to mininet vm
print("connecting to mininet default topology")
#print(net_connect.send_command_timing('sudo mn'))
# print(net_connect.send_command_timing('mininet'))
#print(net_connect.send_command_timing('sh ovs-vsctl get-controller'))

p1 = subprocess.Popen(['sudo', 'mn'], stdout=subprocess.PIPE)
[out, err] = p1.communicate()
print(out)
p2 = subprocess.Popen(['sh', 'ovs-vsctl', 'get-controller'], stdout=subprocess.PIPE)
[out, err] = p2.communicate()
