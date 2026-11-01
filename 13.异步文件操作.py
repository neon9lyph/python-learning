import asyncio

import aiofiles  # ⚠️ 注意：这是一个第三方库，使用前需要 pip install aiofiles


async def async_file_demo():
    filename = "async_knowledge.txt"

    # --- 1. 异步写入 ---
    print("⏳ 开始异步写入...")
    # 注意这里使用的是 async with
    async with aiofiles.open(filename, mode="w", encoding="utf-8") as f:
        # 写入操作是耗时的 I/O，所以需要 await，交出控制权
        await f.write("RAG 技术结合了检索和生成。\n异步 I/O 能提高并发效率。")
    print("✅ 写入完成。")

    # --- 2. 异步读取 ---
    print("⏳ 开始异步读取...")
    async with aiofiles.open(filename, mode="r", encoding="utf-8") as f:
        # 读取同样需要 await
        content = await f.read()
        print(f"📜 读取到的内容:\n{content}")


if __name__ == "__main__":
    # 异步函数不能直接调用，需要通过事件循环运行
    asyncio.run(async_file_demo())
