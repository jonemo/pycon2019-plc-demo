from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.1.9')
client.read_holding_registers(0, 12)

# In [52]: client.read_holding_registers(0, 12).registers
# Out[52]: [0, 500, 0, 300, 0, 100, 0, 300, 0, 700, 0, 50]

# In [51]: client.write_registers(0, [0, 500])
# Out[51]: <pymodbus.register_write_message.WriteMultipleRegistersResponse at 0x196d1644048

client.close()