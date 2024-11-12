import pyvisa
import time

rm = pyvisa.ResourceManager()
instruments = rm.list_resources()

print(instruments)

# Follow your address
smu = rm.open_resource(instruments[2])

#Hard code all the parameters
smu.write("FUNC:MODE CURR")
# smu.write("SOURCE:SWEep:LINear")
smu.write("SWE:SPAC LIN")
smu.write("SWE:STA SINGLE")

smu.write("SWE:STAR 0.001") 
smu.write("SWE:STOP 0.05")
# smu.write("SWE:STEP 0.001")
smu.write("SWE:POIN 100")
smu.write("SOURce1:SWEep:TRIG:STArt:SOURCE IMMediate")
smu.write("OUTPUT 1")
smu.write("SOURce:SWEep:INITiate")