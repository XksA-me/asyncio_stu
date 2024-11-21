import asyncio
import aiohttp

'''
gather() 用于并发执行多个协程，等待所有协程完成。

关键特性：

并发执行多个协程
返回结果顺序与输入顺序相同
return_exceptions=True 时不会因为单个任务失败而中断
'''

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        'https://baidu.com',
        'https://juejin.cn',
        'https://blog.csdn.net'
    ]
    
    async with aiohttp.ClientSession() as session:
        # 并发执行所有请求
        results = await asyncio.gather(
            *[fetch_url(session, url) for url in urls],
            return_exceptions=True  # 遇到异常继续执行其他任务
        )
        
        for url, html in zip(urls, results):
            if isinstance(html, Exception):
                print(f"{url}: Error - {html}")
            else:
                print(f"{url}: {len(html)} bytes")

asyncio.run(main())