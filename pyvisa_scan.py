import pyvisa

rm = pyvisa.ResourceManager()
resources = rm.list_resources()

if resources:
    for resource in resources:
        # print("Resource:" , resource)
        equipment = rm.open_resource(resource)
        # print("Equipment:" , equipment)
        # print("Connected VISA resources:" + resource + ". IDN:" + equipment.write("IDN"))
        IDN = equipment.write("*IDN?")
        print(f"Connected VISA resources: {resource} IDN: {IDN}")
        # equipment.close()
else:
    print("No VISA resources found.")

rm.close()
