import asyncio
import os

from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

class Meross:
    def __init__(self):
        self.channels = [1, 2]
        self.device_uuid = '2208115470512254060448e1e9a1860b'

    async def turn_on(self):
        http_api_client = await self.get_http_client();
        manager = await self.get_meross_manager(http_api_client)

        # Retrieve all the devices that implement the electricity mixin
        await manager.async_device_discovery(meross_device_uuid='2208115470512254060448e1e9a1860b')
        devs = manager.find_devices(device_uuids=['2208115470512254060448e1e9a1860b'])
        if len(devs) < 1:
            print("No electricity-capable device found...")
        else:
            dev = devs[0]

            # Update device status: this is needed only the very first time we play with this device (or if the
            #  connection goes down)
            await dev.async_update()


            for channel in self.channels:
                print(f"Turing off {dev.name}: channel {channel}")
                await dev.async_turn_on(channel=channel)
                await asyncio.sleep(2)

        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()

    async def turn_off(self):
        http_api_client = await self.get_http_client();
        manager = await self.get_meross_manager(http_api_client)

        # Retrieve all the devices that implement the electricity mixin
        await manager.async_device_discovery(meross_device_uuid='2208115470512254060448e1e9a1860b')
        devs = manager.find_devices(device_uuids=['2208115470512254060448e1e9a1860b'])
        if len(devs) < 1:
            print("No electricity-capable device found...")
        else:
            dev = devs[0]

            # Update device status: this is needed only the very first time we play with this device (or if the
            #  connection goes down)
            await dev.async_update()


            for channel in self.channels:
                print(f"Turing off {dev.name}: channel {channel}")
                await dev.async_turn_off(channel=channel)
                await asyncio.sleep(2)

        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()

    async def get_meross_manager(self, http_api_client):
        # Setup and start the device manager
        manager = MerossManager(http_client=http_api_client)
        await manager.async_init()
        return manager
    
    def get_http_client(self):
        # Setup the HTTP client API from user-password
        return MerossHttpClient.async_from_user_password(email="", password="")


def turn_on():
    meross = Meross()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(meross.turn_on())
    loop.stop()

def turn_off():
    meross = Meross()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(meross.turn_off())
    loop.stop()
