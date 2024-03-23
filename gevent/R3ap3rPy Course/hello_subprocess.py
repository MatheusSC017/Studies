from gevent import monkey
monkey.patch_all()
import gevent
import subprocess

commands = [
    "systeminfo",
    "ipconfig /all",
]


def asynccommand(command):
    print(f"Performing command: {command}")
    stdout, stderr = subprocess.Popen(command).communicate()
    print(f"stdout: {stdout}")


result = [gevent.spawn(asynccommand, command) for command in commands]

gevent.wait(result)

