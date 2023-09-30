# PyBlueChat

### Current state

A connection can be established and the chat is mostly working fine. It will probably still be buggy, and upon terminating the connection weird things will happen.

## Python-based chat using RFCOMM protocol

PyBlueChat is a simple CLI Bluetooth chat app built in Python. It has been tested on Windows and Linux, although it might work on other platforms, due to it using the PyBlueZ library, which is cross-platform.

## Same app for server and client

Upon running PyBlueChat, the user will be prompted to enter the mode of the application (either server or client), and the application will act accordingly.

In client mode, PyBlueChat will ask for an address (or remember the last address used), and a port to create the connection.

In server mode, the connection will be created automatically and the address and port will be displayed to the user.

## I'm running out of things to write

I don't have anything else to showcase. This project was started to provide myself and my classmates with a way of communicating in class while avoiding the use of the school's Wi-Fi network and our phones. If you're any of my teachers reading this, please don't expell me.
