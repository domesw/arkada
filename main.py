'''
Created on 27 lut 2018

@author: user
'''

if __name__ == '__main__':
    pass
from maxcube.cube import MaxCube
from maxcube.connection import MaxCubeConnection

cube = MaxCube(MaxCubeConnection('192.168.0.222', 62910))

for device in cube.devices:
    print(device.name)
    print("actual:", device.actual_temperature)