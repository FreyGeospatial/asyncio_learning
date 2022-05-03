import asyncio

async def main(): # must prefix function with async, which acts as a wrapper for the function.
    print("frey")
    task = asyncio.create_task(foo("Just Kidding!")) # a task will run when the CPU is not doing anything
    # await task # this will cause task to run before main is finished
    print("finished")
# print(main()) # this won't workm BUT it will return a coroutine object- the wrapper from above

# foo will run when the CPU is not doing anything...
async def foo(text):
    print(text)
    await asyncio.sleep(1) # await can only be used within an async function.

# simulates server request
async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {'date': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main2():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

# future is like a placeholder for a value that will exist in the future


# can run the code below, but just keeping it commented out
# asyncio.run(main()) # asyncio.run() takes a coroutine object

asyncio.run(main2())