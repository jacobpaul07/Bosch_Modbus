from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time

client = ModbusClient(method='rtu', port='COM5', timeout=1, stopbits = 1, bytesize = 8,  parity='N', baudrate= 9600)
client.connect()

while True:

    tempc = client.read_input_registers(address=8, count=1, unit=2)
    tc= tempc.registers[0]/10
    #time.sleep(0.25)
    tempf = client.read_input_registers(address=6, count=1, unit=2)
    tf= tempf.registers[0]/10
    #time.sleep(0.25)
    ldr = client.read_input_registers(address=4, count=1, unit=2)
    ld=ldr.registers[0]/10 
    #time.sleep(0.25)
    flow = client.read_input_registers(address=10, count=1, unit=2)
    fl=flow.registers[0]/10
    #time.sleep(0.25)
    
    print("Temp:", tc, "C")
    print("Temp:", tf, "F")
    print("LDR:", ld)
    print("Flow:", fl)
    print("---------------------------------")

     #10 - flow
     #8 - Temperature
     #4 - LDR

    # ADC = ldr.registers[0]
    # Vout = (ADC * 0.0048828125);
    # RLDR = (1000.0 * (5 - Vout))/Vout;     #Equation to calculate Resistance of LDR, [R-LDR =(R1 (Vin - Vout))/ Vout]
    #    # R1 = 10,000 Ohms , Vin = 5.0 Vdc.
    #
    #           # Vout = Output voltage from potential Divider. [Vout = ADC * (Vin / 1024)]
    # Lux = (500 / RLDR);
    # print(Vout)
    # print(Lux)

