import asyncio
import datetime
import random
import telnetlib

host = "192.168.1.151"
port = 9990

timeout_seconds = 5
endtime_seconds = 7 * 60 * 60 

streaming_output_channels = [11]
streaming_input_channels = [4, 5, 6, 7, 8, 9]

portrait_output_channels = [4, 5]
portrait_input_channels = [6, 7]

landscape_output_channels = [6, 7, 8]
landscape_input_channels = [4, 5, 8, 9]

tn = telnetlib.Telnet(host, port, timeout_seconds)

async def switch_channels(output_channels = [4, 5], input_channels = [6, 7], sleeptime_seconds = 1):
    loop = asyncio.get_running_loop()
    end_time = loop.time() + endtime_seconds
    print(f"\n{datetime.datetime.now()} __ Start auto switching.")
    while True:
        if (loop.time() + 1.0) >= end_time:
            break

        random.shuffle(input_channels)
        for index, output_channel in enumerate(output_channels):
            tn.write((f"video output routing:\n{output_channel} {input_channels[index]}\n\n").encode('ascii'))
            tn.read_until(b"ACK", timeout_seconds)
        print(f"{datetime.datetime.now()} __ switched channels, output:{output_channels}, input:{input_channels}")
        await asyncio.sleep(sleeptime_seconds)

    print(f"\n{datetime.datetime.now()} __ Finished auto switching.")

async def main():
    await asyncio.gather(
        # # for streaming
        switch_channels(streaming_output_channels, streaming_input_channels, 31),
        # # for portrait
        switch_channels(portrait_output_channels, portrait_input_channels, 23),
        # for landscape
        switch_channels(landscape_output_channels, landscape_input_channels, 47),
    )

if __name__ == "__main__":
    asyncio.run(main())
