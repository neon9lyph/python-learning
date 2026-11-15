import random
import sys
import time


# --- 场景 1: 模拟 GPT 的流式输出 ---
def mock_llm_stream(prompt):
    """
    假装自己是一个大模型，一个字一个字地往外蹦。
    """
    full_response = f"关于'{prompt}'的分析如下：Python 生成器是实现流式传输的关键技术。它允许数据按需生成，而不是一次性加载。"

    # 模拟 AI 思考过程
    # 将长句子拆分成单个字符或词组
    tokens = list(full_response)
    print(tokens)
    for token in tokens:
        # 模拟网络传输和推理延迟 (0.05 ~ 0.2秒)
        time.sleep(random.uniform(0.05, 0.2))

        # 【核心】把这个字交出去，然后暂停，等待下一次召唤
        yield token


# --- 场景 2: 内存杀手 vs 内存救星 ---
def infinite_sequence():
    """
    一个永远数不完的生成器。
    如果用普通列表存 infinite_list = [1, 2, ... 无穷]，内存立刻爆炸。
    但生成器完全没压力，因为它是算一个给一个。
    """
    num = 0
    while True:
        yield num
        num += 1
        # 为了防止演示死循环，我强行加个上限，但逻辑上它是无限的
        if num > 10000000:
            break


def run_generator_demo():
    print("=== 🌊 生成器与流式输出 Demo ===\n")

    # --- 实战 1: 体验 ChatGPT 的打字机效果 ---
    print("1. [模拟 AI] 正在流式生成回复 (请盯着屏幕):")
    print("-" * 30)

    prompt = "解释生成器"
    # 获取生成器对象
    stream = mock_llm_stream(prompt)

    # 就像 for 循环遍历列表一样，遍历生成器
    for token in stream:
        # print 默认会换行，end="" 让它不换行
        # flush=True 强制刷新缓冲区，保证字立马跳出来，而不是攒一堆才出来
        print(token, end="", flush=True)

    print("\n" + "-" * 30)
    print("✅ 回复生成完毕。\n")

    # # --- 实战 2: 内存占用对比 ---
    # print("2. [性能] 生成器 vs 列表 内存大比拼")

    # # 创建一个包含 100 万个数字的列表 (一次性生成)
    # large_list = [i for i in range(1000000)]

    # # 创建一个生成 100 万个数字的生成器 (此时并未生成，只存了逻辑)
    # large_gen = (i for i in range(1000000))  # 注意是用圆括号 ()

    # # sys.getsizeof() 查看对象占用内存字节数
    # size_list = sys.getsizeof(large_list)
    # size_gen = sys.getsizeof(large_gen)

    # print(
    #     f"   📦 列表占用内存: {size_list:,} Bytes (约 {size_list / 1024 / 1024:.2f} MB)"
    # )
    # print(f"   ⚡️ 生成器占用内存: {size_gen:,} Bytes (极小！)")
    # print(f"   🏆 结论: 生成器省了 {size_list / size_gen:.0f} 倍的内存！")

    # # 证明生成器也能用
    # print(
    #     f"   (从生成器取前3个数: {next(large_gen)}, {next(large_gen)}, {next(large_gen)})"
    # )


if __name__ == "__main__":
    run_generator_demo()
