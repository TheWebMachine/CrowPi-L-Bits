# 前面省略，从下面直奔主题，举个代码例子：
#!/usr/bin/python3

import logging
import subprocess
import re
import smbus
import time

address   = 0x03
shutdown_reg = 0x45
bus = smbus.SMBus(1)
"""
logging.basicConfig(
    filename = '/home/pi/Desktop/pistatus.log',
    level = logging.DEBUG,
    format = '%(asctime)s %(message)s',
    datefmt = '%d/%m/%Y %H:%M:%S')
"""
sysJobTargets = subprocess.check_output(["sudo","systemctl","list-jobs"]).decode('utf-8')
if re.search('reboot.target.*start',sysJobTargets) == None:
    logging.info('Raspberry Pi power off')
    bus.write_byte_data(address,shutdown_reg,0x88)
