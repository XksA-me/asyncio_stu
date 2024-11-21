import asyncio
async def process_data(time, data):
    await asyncio.sleep(time)
    return f"Processed {data} in {time}s"

async def main():
    tasks = [
        process_data(3, "A"),
        process_data(1, "B"),
        process_data(2, "C")
    ]
    
    # 按完成顺序处理结果
    for coro in asyncio.as_completed(tasks, timeout=4):
        try:
            result = await coro
            print(result)
        except asyncio.TimeoutError:
            print("Task timed out")

asyncio.run(main())