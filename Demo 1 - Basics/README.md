# Demo 1: Basics

## How to open `.adpro` files

To open the `.adpro` files in this folder you need the "Productivity Suite" software. 
Please see the README.md at the top level of this repo for details where to get this software.

## Related section of the presentation

The examples in this repo appear in the PyCon talk video between [8:10](https://youtu.be/a0l29lgDf6k?t=490) and [13:14](https://youtu.be/a0l29lgDf6k?t=794).
In the talk I live-code the files and explain the basics of the ladder logic language as I go along.
I also run the programs on a PLC which is wired up to a traffic signal as a real-world example of controlling devices from PLC logic.

## How to use the examples when you don't have a traffic signal

If you have the PLC but not a traffic signal, you can wire up some other device to the PLC output terminals.
Or simply look at the built-in LEDs to see when the output is active (on) or off.
If you have the PLC but aren't quite sure what LED to look for, just load the `1-3 Blinking.adpro` project onto the PLC, put the PLC into "Run" mode (using the physical switch and the software button), and look for the blinking light!

## What are these examples

These `.adpro` files are project files that contain a single "task" (subroutine) written in ladder logic.
In the presentation which this repo accompanies, they served as the very first introduction to the ladder logic language and the concept of PLCs in general.
You can think of the examples as "Hello World" of PLC programming.
You can watch a recording of the presentation [here](https://youtu.be/a0l29lgDf6k), or jump directly to the section where I use these examples [here](https://youtu.be/a0l29lgDf6k?t=490).

If you watch the presentation video, you will see that I start with a "blank" file and then just keep editing this same file to go from one example to the next.
The files in this folder are intermediate snapshots from this process.

### `1-0 Blank Program.adpro`

This is the file that I start with at [8:15](https://youtu.be/a0l29lgDf6k?t=495) in the video. 
It looks like a blank file (all the ladder rungs are empty), but I did a little bit of prep work to make the demo flow quicker:
* The project is configured with the type of PLC CPU (Productivity1000), the I/O modules I have connected to the PLC's CPU (digital input and digital output) and the IP address of the PLC.
* The Tag Database (which you can find in the tree on the left side of the screen) contains the tags (variables) I will be using, that way I can rely on auto-complete when typing there names.

### `1-1 Simple Button.adpro`

This file represents the state of the demo program that can be seen on screen at [9:51](https://youtu.be/a0l29lgDf6k?t=591) in the video. 
It's a single ladder rung implementing this rule: When the input named `DI1` is on, then enable the output called `DQ1`.
The ladder logic elements used in this examples are "Normally Open Contact" and "Coil".
Watch the video to see this program running.

### `1-2 Delayed Button.adpro`

This file represents the state of the demo program that can be seen on screen at [11:40](https://youtu.be/a0l29lgDf6k?t=700) in the video.
It adds a delay to the previous example: `DQ1` only switches on after `DI1` has been on for two seconds.
On top of the "Normally Open Contact" and "Coil" from the previous example, this example uses the "Simple Timer" ladder logic element.
Watch the video to see this program running.

### `1-3 Blinking.adpro`

This file represents the state of the demo program that can be seen on screen at [12:38](https://youtu.be/a0l29lgDf6k?t=758) in the video.
It no longer uses the `DI1` input for anything.
Instead, it uses two different timers to yield a blinking light that switches state every two seconds.
On top of the previously used ladder logic elements, this example also uses a "Normally Closed Contact", which I explain in the talk as similar to using `if not` in Python.
Watch the video to see this program running.
