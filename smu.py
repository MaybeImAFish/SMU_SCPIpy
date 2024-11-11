import pyvisa
import time
import limits

rm = pyvisa.ResourceManager()
instruments = rm.list_resources()

print(instruments)

smu = rm.open_resource(instruments[2])

# system settings
# smu.write("SYSTEM:PRESET")
# smu.write("SYSTEM:POSETUP: LAST_OFF")
# smu.write("SYSTEM:BRIGHTNESS:LEVEL: 7")
# smu.write("SYSTEM:LFREQUENCY 60")

smu.write("OUTPUT:FILTER OFF")
smu.write("FUNCTION:SHAPE PULSE")
smu.write("FUNCTION:MODE VOLTAGE")

smu.write(f"CURRENT:RANGE {limits.i_range}")
smu.write(f"CURRENT {limits.i_set}")

smu.write(f"VOLTAGE:RANGE {limits.v_range}")

smu.write(f"PULSE:PEAK {limits.v_set}")  
smu.write("PULSE:WIDTH 500E-6")
# smu.write(f"PULSE:BASE {limits.pulse_base}")
smu.write("PULSE:DELAY 20E-3")

smu.write("OUTPUT ON")
time.sleep(10)
smu.write("OUTPUT OFF")

print("DONE!")
