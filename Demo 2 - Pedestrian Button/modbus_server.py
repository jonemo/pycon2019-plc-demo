from pymodbus.datastore import ModbusServerContext
from pymodbus.datastore import ModbusSlaveContext
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.server.asynchronous import StartTcpServer

from datetime import datetime


def boolfmt(label: str, boolvar: bool):
    return f"[{label}]" if boolvar else "[   ]"


class MyDataBlock(ModbusSparseDataBlock):
    """A custom data "storage" class that logs all incoming requests"""
    def setValues(self, address, values):
        super().setValues(address, values)
        now = datetime.now().strftime("%H:%M:%S.%f")
        values_map = zip(["Grn", "Yel", "Red", "Hnd", "Fla", "Wlk"], values)
        g, y, r, h, f, w = [boolfmt(k, v) for k, v in values_map]
        print(f"{now} {g} {y} {r} {w} {f} {h}")


def main():
    block = MyDataBlock([0]*100)  # storing 100 words
    store = ModbusSlaveContext(di=block, co=block, hr=block, ir=block)
    context = ModbusServerContext(slaves=store)
    StartTcpServer(context, address=('0.0.0.0', 502))


if __name__ == "__main__":
    main()
