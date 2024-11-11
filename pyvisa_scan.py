import pyvisa

rm = pyvisa.ResourceManager()
resources = rm.list_resources()

if resources:
    print("Connected VISA resources:")
    for resource in resources:
        print(resource)
else:
    print("No VISA resources found.")

rm.close()
