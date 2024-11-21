import asyncio
'''
wait() 提供了更灵活的等待机制，可以设置超时和完成条件。

wait() 的 return_when 选项：

FIRST_COMPLETED: 任何一个任务完成就返回
FIRST_EXCEPTION: 遇到第一个异常就返回
ALL_COMPLETED: 所有任务完成才返回（默认）
'''

async def process_item(item):
    await asyncio.sleep(item)
    return f"item {item} completed"

async def main():
    # 创建三个任务
    tasks = [
        asyncio.create_task(process_item(2)),
        asyncio.create_task(process_item(1)),
        asyncio.create_task(process_item(3))
    ]
    
    # 等待直到有任务完成或超时
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.Sec,  # 第一个任务完成就返回
        timeout=2.5  # 最多等待2.5秒
    )
    print(done, pending)
    # 处理已完成的任务
    for task in done:
        result = await task
        print(f"Completed: {result}")
    
    # 取消剩余任务
    for task in pending:
        task.cancel()

asyncio.run(main())