from json import loads as json_loads, JSONDecodeError

from fastapi.applications import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response

APP = FastAPI()


@APP.post('/data')
async def post_data(request: Request):
    input_data = await request.body()
    try:
        json_loads(input_data)
    except JSONDecodeError:
        response = Response(status_code=400)
    else:
        response = Response(status_code=201)

    return response
