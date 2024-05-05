from kasa import Discover
import asyncio
import time


async def main():
    device = await Discover.discover_single("192.168.1.162", discovery_timeout=10)

    await device.update()
    if device.is_on:
        await device.turn_off()
    else:
        await device.turn_on()


if __name__ == "__main__":
    asyncio.run(main())
