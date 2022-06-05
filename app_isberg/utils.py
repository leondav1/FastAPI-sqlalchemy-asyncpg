import random

import aioredis


def anagram_solution(s1, s2):
    c1 = [0]*50
    c2 = [0]*50
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 50 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok


async def get_answer(flag):
    redis = await aioredis.from_url('redis://localhost')
    value = await redis.get('count')
    if value is None:
        await redis.set('count', 0)
    if flag:
        await redis.set('count', int(value) + 1)
    count = await redis.get('count')
    await redis.close()
    return count


def get_dev_type_id():
    rd = random.Random()
    _hex = '%012x' % rd.getrandbits(48)
    choice = random.choice(['emeter', 'zigbee', 'lora', 'gsm'])
    return _hex, choice
