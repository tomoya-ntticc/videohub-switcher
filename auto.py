import random
import telnetlib
import time

host = "192.168.1.151"
port = 9990
sleeptime_seconds = 20
timeout_seconds = 5
input_channels = [5, 6, 7, 8, 9]
streaming_channel = 11
tn = telnetlib.Telnet(host, port, timeout_seconds)

while True:
    channel = random.choice(input_channels)
    tn.write((f"video output routing:\n{streaming_channel} {channel}\n\n").encode('ascii'))
    tn.read_until(b"ACK", timeout_seconds)
    time.sleep(sleeptime_seconds)
