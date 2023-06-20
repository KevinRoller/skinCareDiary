import asyncio
import random
async def te():
    print("1 entering")
    sec=random.randint(1,3)
    await asyncio.sleep(sec)
    print("1"+str(sec))
async def te1():
    print("2 entering")
    sec=random.randint(1,3)
    await asyncio.sleep(sec)
    print("2"+str(sec))
async def te2():
    print("3 entering")
    sec=random.randint(1,3)
    await asyncio.sleep(sec)
    print("3"+str(sec))

async def main():
    task1=asyncio.create_task(te())
    task2=asyncio.create_task(te1())
    task3=asyncio.create_task(te2())
    print("hahah, i run first")
    await asyncio.sleep(10)

asyncio.get_event_loop().run_until_complete(main())

     