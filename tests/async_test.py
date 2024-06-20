import asyncio


async def fetch_url(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # 模拟网络延迟
    return f"Result from {url}"


async def fetch_url2(url):
    print(f"Fetching {url}")
    await asyncio.sleep(5)  # 模拟网络延迟
    return f"Result from {url}"


async def main():
    url1 = fetch_url("http://example.com/1")
    url2 = fetch_url2("http://example.com/2")
    url3 = fetch_url("http://example.com/3")

    results = await asyncio.gather(url1, url2, url3)
    print(results)


asyncio.run(main())
