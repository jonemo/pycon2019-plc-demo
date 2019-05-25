# Demo 2: Pedestrian Button

## How to open `.adpro` files

To open the `.adpro` files in this folder you need the "Productivity Suite" software. 
Please see the README.md at the top level of this repo for details where to get this software.

## Related section of the presentation

The `Traffic Light.adpro` file in this folder appears in the PyCon talk video between [16:02](https://youtu.be/a0l29lgDf6k?t=972) and [21:21](https://youtu.be/a0l29lgDf6k?t=1281).
Not all of the `.py` files were part of the presentation because I had to trim the talk content quite aggressively to stay within the time limit.
Nonetheless, the `Traffic Light.adpro` PLC program contains everything necessary for the Python scripts to work.

If you have not read the README.md files at the top level of this repo and the one in the `Demo 1: Basics` folder, I suggest you read those first and then come back here.

## How to use the examples when you don't have a traffic signal

If you have the PLC but not a traffic signal, you can wire up other devices to the PLC input and output terminals.
Currently, I do not have a wiring diagram available for this setup; please send me an email if you are interested in using this example and need more details.

## What's in the `Traffic Light.adpro`?

The purpose of this PLC project is to demonstrate different network interfaces and protocols for communicating with a PLC from Python scripts running on a PC.
The presentation this was part of contains some discussion of the Modbus protocol as well as a review of other libraries and protocols that can be used with other brands of PLC.

`Traffic Light.adpro` contains several tasks (subroutines) written in ladder logic (the only language available in Productivity Suite).

### `MainTask` 

`MainTask` calls all the other tasks at every scan of the program

### `PedestrianXing`

`PedestrianXing` uses a sequence of timers to step through a traffic light cycle from green to yellow to red, then "walking" to "flashing" to "hand" for pedestrians, back to green. 
The trigger for the cycle is either `DI1` (wired to the pedestrian button) or one of the other tasks. 
This task is on screen at [16:41](https://youtu.be/a0l29lgDf6k?t=1001) in the presentation recording.

### `Demo2Part`

`Demo2Part2` contains ladder logic elements to write the current state of all outputs (i.e. the state of the traffic signal) to a remote Modbus server. 
Use the `modbus_server.py` script below to run a Modbus server on your laptop. 
The PLC program assumes that your laptop has the IP address `192.168.1.99` (you can change this value in `Demo2Part2`) and runs the Modbus server on port `502` (the default normally used with Modbus over TCP).

### `Demo2Part3`

`Demo2Part3` contains ladder logic elements to listen for incoming ASCII strings on port 50505 of the PLC (that port number is arbitrarily chosen and can be changed). 
See the `socket_client.py` script below for how to send commands to this "server". 
This task was not shown or used in the PyCon presentation.

### `Demo2Part4`

`Demo2Part4` contains ladder logic that implement the "Second Mode" aka "Disco Mode" of the traffic signal. 
See the `socket_client.py` section below for how to trigger "Disco Mode" and what it is.
The PLC tag names and program names are intentionally nondescript ("Second Mode" and "Demo2Part4") because this allows me to use the "Disco Mode" as a suprise/joke in live demonstrations.
This task was not shown or used in the PyCon presentation.

### Project Configuration

The `Traffic Light.adpro` also contains various configuration settings:
* The setup with information like which PLC CPU is used and what I/O modules are connected.
* Configuration for the Modbus server and which tags (variables) are exposed over the Modbus protocol.
* Configuration for the "Custom Protocol over Ethernet" (CPoE) server used in the `Demo2Part3` task.

## Python Scripts

### `modbus_client.py`


### `modbus_server.py`


### `socket_client.py`

```python
import socket

sock = socket.socket()
sock.connect(("192.168.1.9", 50505))
sock.sendall(b"REQ")  # request a pedestrian cycle
sock.recv(1024)  # if everything works, the PLC responds with "ACK"
sock.sendall(b"DISCO")  # the traffic signal flashes its lights until the pedestrian button is pressed
sock.close()
```

### `datascience/__init__.py`

This file is used to support a joke about data science in the presentation.
It's at approximately [20:47](https://youtu.be/a0l29lgDf6k?t=1247) in the video recording.
Basically, it allows me to write the following code in a REPL and get back a (static) list of values that happens to be exactly what I want for the next on-stage demo:

```python
from pymodbus.client.sync import ModbusTCPClient
from datascience import machine_learning

client = ModbusTCPClient("192.168.1.9")
client.write_registers(0, machine_learning())
```
