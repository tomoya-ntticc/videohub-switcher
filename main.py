import asyncio
import datetime
import random
import telnetlib

import settings


tn = telnetlib.Telnet(settings.IP_ADDRESS, settings.PORT, settings.TIMEOUT_SECONDS)

streaming = settings.ROUTING["streaming"]
portrait = settings.ROUTING["portrait"]
landscape = settings.ROUTING["landscape"]

async def switch_channels(output_channels: list[int], input_channels: list[int], sleep_seconds: int = 1):
    while True:
        random.shuffle(input_channels)
        for index, output_channel in enumerate(output_channels):
            tn.write((f"video output routing:\n{output_channel} {input_channels[index]}\n\n").encode('ascii'))
            tn.read_until(b"ACK", settings.TIMEOUT_SECONDS)
        print(f"{datetime.datetime.now()} __ Switched channels, output:{output_channels}, input:{input_channels}")
        await asyncio.sleep(sleep_seconds)

async def main():
    print(f"\n{datetime.datetime.now()} __ Start auto switching.\n")
    await asyncio.gather(
        switch_channels(streaming["OUTPUT_CHANNELS"], streaming["INPUT_CHANNELS"], streaming["INTERVAL_SECONDS"]),
        switch_channels(portrait["OUTPUT_CHANNELS"], portrait["INPUT_CHANNELS"], portrait["INTERVAL_SECONDS"]),
        switch_channels(landscape["OUTPUT_CHANNELS"], landscape["INPUT_CHANNELS"], landscape["INTERVAL_SECONDS"]),
    )
    print(f"\n{datetime.datetime.now()} __ Finished auto switching.")

if __name__ == "__main__":
    asyncio.run(main())
