from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app_isberg.models.models import Device, Endpoint


async def get_devices_not_endpoints(session: AsyncSession, device_id: tuple):
    result = await session.execute(
        f'select dev_type, COUNT(*) as "count" from devices where id not in {device_id} group by dev_type order by dev_type ')
    return result


def add_device(session: AsyncSession, dev_id: str, dev_type: str):
    new_device = Device(dev_id=dev_id, dev_type=dev_type)
    session.add(new_device)
    return new_device


async def get_endpoints(session: AsyncSession):
    result = await session.execute(select(Endpoint))
    return result.scalars().all()


def add_endpoint(session: AsyncSession, device_id: int, comment: str):
    new_endpoint = Endpoint(device_id=device_id, comment=comment)
    session.add(new_endpoint)
    return new_endpoint
