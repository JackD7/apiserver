import asyncio
import json

# aiohttp: asynchronous http client and server
import aiohttp
from aiohttp import web

class ApiServer:

    def __init__(self, logger):
        self.logger = logger

    async def API_Ping(self, request):
        try:
            body = await request.json()
        except:
            body = {}
        self.logger.info("API_Ping received {} - body: {}".format(request, body))
        return web.HTTPOk()

    async def API_createData(self, request):
        try:
            body = await request.json()
        except:
            body = {}
        self.logger.info("API_createData received {} - body: {}".format(request, body))
        return web.HTTPOk()