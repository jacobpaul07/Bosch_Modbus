import time
from pyModbusTCP.client import ModbusClient

# TCP auto connect on first modbus request
client = ModbusClient(host="localhost", port=502, unit_id=1)
client.open()

while True:
    """Modbus function READ_INPUT_REGISTERS (0x04)

            :param reg_addr: register address (0 to 65535)
            :type reg_addr: int
            :param reg_nb: number of registers to read (1 to 125)
            :type reg_nb: int
            :returns: registers list or None if fail
            :rtype: list of int or None
            """

# Read 2x 16 bits registers at modbus address 0 :

    regs = client.read_holding_registers(0, 2)
    if regs:
        print(regs)
    else:
        print("read error")

    time.sleep(3)