import asyncio
from typing import Union

import typer
from fastapi import FastAPI, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app_isberg import service
from app_isberg.db.base import init_models, get_session
from app_isberg.utils import anagram_solution, get_answer, get_dev_type_id

app = FastAPI()
cli = typer.Typer()


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


@app.get('/anagram')
async def read_item(s1: Union[str, None] = None, s2: Union[str, None] = None):
    anagram = anagram_solution(s1, s2)
    count = await get_answer(anagram)
    return {"is_anagram": anagram, "count": count}


@app.post("/devices/add/", status_code=status.HTTP_201_CREATED)
async def add_devices(session: AsyncSession = Depends(get_session)):
    for i in range(10):
        dev_id, dev_type = get_dev_type_id()
        device = service.add_device(session, dev_id, dev_type)
        await session.commit()
        if i < 5:
            service.add_endpoint(session, device.id, dev_type)
            await session.commit()
    return {"status": status.HTTP_201_CREATED}


@app.get("/devices_not_endpoint/")
async def devices(session: AsyncSession = Depends(get_session)):
    device_id = [i.device_id for i in await service.get_endpoints(session)]
    devicess = await service.get_devices_not_endpoints(session, tuple(device_id))
    return JSONResponse(dict(i for i in devicess))


if __name__ == "__main__":
    cli()
