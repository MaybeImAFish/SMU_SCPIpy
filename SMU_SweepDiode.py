import pyvisa
import time

rm = pyvisa.ResourceManager()
instruments = rm.list_resources()

print(instruments)

# Follow your address
smu = rm.open_resource(instruments[2])

# USE Type switch to Host mode, else SMU cant export CSV files into Drive
# smu.write("SYST:COMM:USB:TYPE HOST")

# Make SMU into Current mode
smu.write("FUNC:MODE CURR")

#Sweep Linear Mode
# smu.write("SOURCE:SWEep:LINear")
smu.write("SWE:SPAC LIN")
smu.write("SWE:STA SINGLE")

# Sweep Parameter, start ~ end, step size, no of points
smu.write("SWE:STAR 0.001") 
smu.write("SWE:STOP 0.05")
# smu.write("SWE:STEP 0.001")
smu.write("SWE:POIN 100")
smu.write("SOURce1:SWEep:TRIG:STArt:SOURCE IMMediate")
smu.write("OUTPUT 1")
smu.write("SOURce:SWEep:INITiate")

#Setting on Graph
smu.write("SWE:GRAP:CONF:CURV:NUMB 1")
smu.write("SWE:GRAP:VOLT:SCAL LINear")
smu.write("SWE:GRAP:CURR:SCAL LINear")
smu.write("SWE:GRAP:VOLT:INVE 0")
smu.write("SWE:GRAP:CURR:INVE 0")
# Export to USB [Insert your filename here], hint you can create a loop to roll the name with cycle time.
print(smu.write("SWE:GRAP:VIEW:CURV:DATA? 10"))

smu.write("SWE:DATA:EXP IT2806_sweep_data00005") # error thrown here

# gago naman