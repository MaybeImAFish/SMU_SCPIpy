import pyvisa
import time

# Initialize the connection
rm = pyvisa.ResourceManager()
power_supply = rm.open_resource('USB0::0x2EC7::0x3633::803485011757350006::INSTR')  # Replace with your device's VISA address

# Simple SCPI commands to control the power supply
try:
    # Identify the instrument
    response = power_supply.query('*IDN?')
    print(f"Connected to: {response}")

    # Set Power Supply to Source Mode
    power_supply.write('SYST:FUNC SOUR')

    # Set voltage to 1V
    power_supply.write('VOLT 1.00')

    # Set current limit to 1A
    # power_supply.write('CURR 0.01')

    # Turn on the output
    power_supply.write('OUTP ON')

    voltage = power_supply.query('MEAS:VOLT?')
    current = power_supply.query('MEAS:CURR?')

    time.sleep(2)

    print(f"Output Voltage: {voltage.strip()} V")
    print(f"Output Current: {current.strip()} A")

finally:
    # Close the connection
    power_supply.close()
    rm.close()
