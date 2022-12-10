import random
import telnetlib
import time

from InquirerPy import inquirer

prompt = inquirer.select(
        message="Select mode:",
        choices=["Auto", "Rotate"],
        long_instruction="ENTER:run, Q:quit",
        raise_keyboard_interrupt=False,
        mandatory_message="Prompt is mandatory, terminate the program using ctrl-d",
    )

@prompt.register_kb("q")
def _handle_quit(event):
    print("\nQuit control.")
    exit()


host = "192.168.1.151"
port = 9990
sleeptime_seconds = 20
timeout_seconds = 5
input_channels = [5, 6, 7, 8, 9]
tn = telnetlib.Telnet(host, port, timeout_seconds)

tn.read_until(b"END PRELUDE:")

mode = prompt.execute()
print(f"Run {mode} control.")
if mode == "Rotate":
    while True:
        for input in [0, 1, 2, 5, 6, 7, 8, 9]:
            tn.write(("video output routing:\n10 %s\n\n" % input).encode('ascii'))
            tn.read_until(b"ACK", timeout_seconds)
            time.sleep(1)
elif mode == "Auto":
    while True:
        channel = random.choice(input_channels)
        tn.write((f"video output routing:\n10 {channel}\n\n").encode('ascii'))
        tn.read_until(b"ACK", timeout_seconds)
        time.sleep(sleeptime_seconds)
