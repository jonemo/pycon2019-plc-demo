# What is this?

This repo contains scripts and Programmable Logic Controller (PLC) programs from my talk at PyCon 2019. 

All information about this talk, including slides and a link to the video recording, are available on my website: https://jonasneubert.com/talks/pycon2019.html

# Contents

I prepared various demos for this talk, each consisting of a ladder logic program for the Automation Direct Productivity1000 PLC as well as Python code.
Some demos share a PLC program.
Not all demos included in this repo appeared in the talk.

Each folder contains a separate Readme file with information on what the demo was and how to use it.

# PLC and Programming Software

The demos in this talk are about working with a PLC, i.e. a piece of hardware separate from your computer. 
There exists no simulator for the brand of PLC I used in the talk, i.e. you can only use the code in this repo if you have an Automation Direct Productivity1000 PLC. 

The bill of materials for the PLC used in the talk is this:

| Description | Part No | Link | Quantity | Unit Price |
| --- | --- | --- | --- | --- |
| CPU Unit | P1-540 | [Link](https://www.automationdirect.com/pn/P1-540) | 1 | $171.00 |
| Power Supply | P1-01AC | [Link](https://www.automationdirect.com/pn/P1-01AC) | 1 | $37.50 |
| Digital Input Module | P1-08ND3 | [Link](https://www.automationdirect.com/pn/P1-08ND3) | 1 | $34.50 |
| Digital Output Module | P1-08TD2 | [Link](https://www.automationdirect.com/pn/P1-08TD2) | 1 | $34.00 |
| Spring Clamps | P1-10RTB-1 | [Link](https://www.automationdirect.com/pn/P1-10RTB-1) | 1 | $5 |

To connect it all together, you will also need wires, terminal blocks, fasteners, maybe a DIN rail. 
I do not currently have a wiring diagram available.

To edit the PLC program and "download" it to the PLC you will need the free "Productivity Suite" software. 
You can download it here: https://support.automationdirect.com/products/p3000.html
