# pol.py
# This defines a simple point of load regulator.

from skidl import *

# create the power nets.
GND_net = Net('GND')
VIN_net = Net('VIN', drive=POWER)  # This turns off an ERC warning about drive strength into VIN of ldo.
V25_net = Net('V25')
ldo_adj_net = Net('ldo_adj')

# create some components.
div_res1 = Part('device', 'R', value='470',  footprint='Resistors_SMD:R_0805') # resistor 1
div_res2 = Part('device', 'R', value='768',  footprint='Resistors_SMD:R_0805') # resistor 2
c_in     = Part('device', 'C', value='10uF', footprint='device.lib:C')
c_out    = Part('device', 'C', value='10uF', footprint='device.lib:C')
ldo      = Part('regul.lib',  'LM317L_SO8',  footprint=' Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm')

# wire up the components.
ldo['VI'] += VIN_net; ldo['VO'] += V25_net; ldo['ADJ'] += ldo_adj_net; 
c_in[1] += VIN_net; c_in[2] += GND_net; 
c_out[1] += V25_net; c_out[2] += GND_net; 
div_res1[1] += V25_net; div_res1[2] += ldo_adj_net; 
div_res2[1] += ldo_adj_net; div_res2[2] += GND_net; 

# print the parts
print(div_res1)
print(div_res2)
print(c_in)
print(c_out)
print(ldo)

# print the nets
print(GND_net)
print(VIN_net)
print(V25_net)
print(ldo_adj_net)

ERC()
generate_netlist()

exit()

