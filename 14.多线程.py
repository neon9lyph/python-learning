import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def mock_ai_request(prompt, index):
    """
    模拟一个耗时的AI请求
    """
    print(f"线程 {index} 开始处理请求: {prompt}")

    # 模拟网络延迟
    delay = random.uniform(1, 2)  # 随机延迟
    time.sleep(delay)

    print(f"线程 {index} 完成请求(耗时: {delay:.2f} 秒)")
    return f"响应 {index}: {prompt} -> 结果"


def run_concurrency_demo():
    tasks = ["解释量子力学", "分析股票走势", "生成诗歌", "翻译文本", "图像识别"]

    # # Round 1: 传统的同步处理
    # start_time = time.time()

    # results_serial = []

    # for i, task in enumerate(tasks):
    #     result = mock_ai_request(task, i)
    #     results_serial.append(result)

    # end_time = time.time()
    # print(f"传统同步处理耗时: {end_time - start_time:.2f} 秒")
    # print("*" * 40)

    print("多线程并发处理示例")
    start_time = time.time()
    results_concurrent = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        # # 方法A: executor.map()，返回结果是按提交顺序排列的
        # results = executor.map(mock_ai_request, tasks, range(len(tasks)))
        # print(results)

        # 方法B: executor.submit() + as_completed()，返回结果是按完成顺序排列的
        futures = []
        for i, task in enumerate(tasks):
            future = executor.submit(mock_ai_request, task, i)
            futures.append(future)
        print("所有任务已提交，等待完成...")

        for future in as_completed(futures):
            try:
                result = future.result()
                results_concurrent.append(result)
            except Exception as e:
                print(f"任务执行出错: {e}")

    end_time = time.time()
    print(f"多线程并发处理耗时: {end_time - start_time:.2f} 秒")


run_concurrency_demo()
