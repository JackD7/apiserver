#!/usr/bin/python3

"""
Api Server
"""

import os
import argparse
import asyncio
import yaml

# aiohttp: asynchronous http client and server
import aiohttp
from aiohttp import web

from package.apiserver.apilogger import ApiLogger
from package.apiserver.apiserver import ApiServer

def main():
    """
    Main entrypoint

    :return:
    """
    parser = argparse.ArgumentParser(description='Ap Server')
    parser.add_argument('--loglevel', nargs=1, choices=['debug', 'info', 'error'],
                        help='Log level verbosity')    
    parser.add_argument('--port', help='Port', default=8888)
    parser.add_argument('--schema', help='YAML Schema', default='./package/apiserver/api.yaml')
    args = parser.parse_args()

    API_PORT = os.getenv('API_SERVER_PORT', args.port)
    if args.loglevel != None and args.loglevel[0] != 'debug':
        if args.loglevel[0] == 'info':
            logger = ApiLogger('info')
        else:
            logger = ApiLogger('error')
    else:
        logger = ApiLogger('debug')

    logger.info("Api Server starting...")

    loop = asyncio.get_event_loop()

    app = web.Application()

    gApiServer = ApiServer(logger)

    # Setup routes
    with open(args.schema, 'r') as inputfile:
        schema = yaml.safe_load(inputfile)
    routes = []
    for k0, v0 in schema["paths"].items():
        for k1, v1 in v0.items():
            routes.append({'route': k0, 'request': k1, 'operationId': v1['operationId']})

    for element in routes:
        app.router.add_route(element['request'], element['route'], eval("gApiServer."+element['operationId']))
        logger.info("Route added: {}".format(element))

    web.run_app(app, host='0.0.0.0', port=API_PORT)

    logger.info("End Api Server")

if __name__ == "__main__":
    main()
