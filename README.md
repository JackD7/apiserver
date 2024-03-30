# Simple and generic aiohttp server

This repository contains a simple project for a generic aiohttp server.
The server generates automatically routes from yaml schema.

Example of usage

```
curl --location --request GET 'http://0.0.0.0:8888/ping'
```

```
curl --location --request POST 'http://0.0.0.0:8888/data' \
--header 'Content-Type: application/json' \
--data-raw '{
    "content": {}
}'
```
