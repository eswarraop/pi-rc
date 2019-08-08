#!/usr/bin/env python
"""Manually send commands to the RC car."""
import argparse
import socket
import sys
import time
import random


def send_signal_repeats_full(host, port, command_array):
    """Reads signal repeat bursts and sends commands to the Raspberry Pi."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # pylint: disable=star-args
    command = format_command(*command_array)

    if sys.version_info.major == 3:
        command = bytes(command, 'utf-8')

    sock.sendto(command, (host, port))

commands = {}

commands["forward"] = 10
commands["reverse"] = 40
commands["right"] = 64
commands["left"] = 58

commands["forward_right"] = 34
commands["forward_left"]  = 28
commands["reverse_right"] = 46
commands["reverse_left"]  = 52

def main():

    for i in range(50):
        choice = random.choice(list(commands.values()))
        send_command(choice, 0.1)
        time.sleep(0.1)

def send_command( command = 10, duration = 0.5):

    command_array =  [
        float(27.145),
        int(400),
        int(3),
        int(4),
        int(command)
    ]

    server = "10.0.0.12"
    port = 12345

    print('Sending commands to ' + server + ':' + str(port))
    send_signal_repeats_full(server, port, command_array)

    command_array[4] = 1
    time.sleep( duration )
    send_signal_repeats_full(server, port, command_array)


if __name__ == '__main__':
    main()
