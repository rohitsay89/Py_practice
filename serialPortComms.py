# =============================================================#
import sys
import datetime

import curses
import time
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
#from pymodbus.payload import BinaryPayloadBuilder

# =============================================================#
print("This is python Data Analysis learning codebase")
print("Python Version = ", sys.version_info.major,
      ".", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now(), "\n")
# =============================================================#

# as I am considering the command window in 4th quadrant of rectangular co ordinate system and treating negative x and y values as positive
# ----> is x axis
#   |
#   |  is y axis
#   |
#   |

boxStartXCord = 0
boxStartYCord = 0

boxEndXCord = 45
boxEndYCord = 25

headerStringXCord = 1
headerStringYCord = 1

conStringXCord = 2
conStringYCord = 3

datatringXCord = 1
datatringYCord = 7

dateStringXCord = 1
dateStringYCord = 5

exitStringXCord = 27
exitStringYCord = 22

client = ModbusSerialClient(
      method='rtu',
      port='COM6',
      baudrate=115200,
      timeout=3,
      parity='N',
      stopbits=1,
      bytesize=8
)


# Helper functions
def num_to_state(num):
      if (num > 2):
            return 'UNASSIGNED'

      switcher = {
            0: 'OFF',
            1: 'IDLE',
            2: 'RUNNING'
      }
      return switcher.get(num)


# Modbus data read
def data_read():
      res = client.read_input_registers(address=9, count=20, unit=1)
      if not res.isError():
            stdscr.addstr(conStringYCord, conStringXCord, "Connected !    ")
            decoder = BinaryPayloadDecoder.fromRegisters(res.registers,
                                                         byteorder=Endian.Big,
                                                         wordorder=Endian.Big)
            # print(res.registers)
            stdscr.addstr((datatringYCord + 1), (datatringXCord + 2),
                          'Voltage  = {0} V '.format(decoder.decode_16bit_int() / 100))
            stdscr.addstr((datatringYCord + 2), (datatringXCord + 2),
                          'Current  = {0} A '.format(decoder.decode_16bit_int() / 100))
            stdscr.addstr((datatringYCord + 3), (datatringXCord + 2),
                          'Temp     = {0} C '.format(decoder.decode_16bit_int()))
            stdscr.addstr((datatringYCord + 4), (datatringXCord + 2),
                          'Distance = {0} cm   '.format(decoder.decode_16bit_uint()))

            stdscr.addstr((dateStringYCord + 1), (dateStringXCord + 1),
                          '{}-{}-{}, {}:{}:{}     '.format(decoder.decode_16bit_uint(),
                                                           decoder.decode_16bit_uint(),
                                                           decoder.decode_16bit_uint(),
                                                           decoder.decode_16bit_uint(),
                                                           decoder.decode_16bit_uint(),
                                                           decoder.decode_16bit_uint(), ))

            stdscr.addstr((datatringYCord + 5), (datatringXCord + 2),
                          'Accel_X  = {0}     '.format(decoder.decode_16bit_int()))
            stdscr.addstr((datatringYCord + 6), (datatringXCord + 2),
                          'Accel_Y  = {0}     '.format(decoder.decode_16bit_int()))
            stdscr.addstr((datatringYCord + 7), (datatringXCord + 2),
                          'Accel_Z  = {0}     '.format(decoder.decode_16bit_int()))
            stdscr.addstr((datatringYCord + 8), (datatringXCord + 2),
                          'Gyro__X  = {0}     '.format(decoder.decode_16bit_int()))
            stdscr.addstr((datatringYCord + 9), (datatringXCord + 2),
                          'Gyro__Y  = {0}     '.format(decoder.decode_16bit_int()))
            stdscr.addstr((datatringYCord + 10), (datatringXCord + 2),
                          'Gyro__Z  = {0}     '.format(decoder.decode_16bit_int()))

            stdscr.addstr((datatringYCord + 11), (datatringXCord + 2),
                          'State    = {0}   '.format(num_to_state(decoder.decode_16bit_int())))
            stdscr.addstr((datatringYCord + 12), (datatringXCord + 2),
                          'Key      = {0}   '.format(hex(decoder.decode_16bit_uint())))
            stdscr.refresh()
      else:
            stdscr.addstr(conStringYCord, conStringXCord, "Not Connected !")


'''
print('Temperature reading here')
for i in range(1,100):
    time.sleep(1)
    temp_read()

'''

if __name__ == "__main__":
      if client.connect():
            stdscr = curses.initscr()
            stdscr.clear()
            curses.noecho()
            curses.cbreak()
            stdscr.nodelay(True)

            w = stdscr.subwin(boxEndYCord, boxEndXCord, boxStartYCord, boxStartXCord)
            w.box()

            stdscr.addstr(headerStringYCord, headerStringXCord, " =========== Modbus Data =========== ")
            stdscr.addstr(dateStringYCord, dateStringXCord, "   Date            Time    ")
            stdscr.addstr(conStringYCord, conStringXCord, "Not Connected !")
            stdscr.addstr(exitStringYCord, exitStringXCord, "Press q to quit")

            try:
                  stdscr.addstr(conStringYCord, conStringXCord, "Connected !    ")
                  while True:
                        data_read()
                        c = stdscr.getch()
                        if (c == ord('q')):  # keep looking for 'q' key on keyboard
                              break
                        time.sleep(0.1)  # refresh every 100ms
            finally:
                  curses.echo()
                  curses.nocbreak()
                  curses.endwin()
            client.close()
      else:
            print('=== CONNECT MODBUS CABLE ===')




# EOF