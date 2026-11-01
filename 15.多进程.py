import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def calculate_heavy_task(n):
    """
    模拟一个计算密集型任务
    n越大，CPU消耗越大
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


def run_multiprocessing_demo():
    COMPLEXITY = 300_000  # 计算复杂度
    # 模拟需要执行10次同样的任务
    task_inputs = [COMPLEXITY] * 10

    # 1.多进程执行
    start_mp = time.time()
    # 创建一个进程池，使用最多4个核心并行计算
    with ProcessPoolExecutor(max_workers=5) as executor:
        # map方法会自动将任务分配 给进程池中的worker
        results_mp = list(executor.map(calculate_heavy_task, task_inputs))
        print(f"多进程完成任务数: {len(results_mp)}")
    end_mp = time.time()
    print(f"多进程执行耗时: {end_mp - start_mp:.2f} 秒")

    # 2.单进程执行
    start_sp = time.time()
    results_sp = [calculate_heavy_task(n) for n in task_inputs]
    print(f"单进程完成任务数: {len(results_sp)}")
    end_sp = time.time()
    print(f"单进程执行耗时: {end_sp - start_sp:.2f} 秒")
    print(f"两种方式计算结果是否一致: {results_mp == results_sp}")


if __name__ == "__main__":
    run_multiprocessing_demo()
