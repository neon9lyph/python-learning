import sys
from unittest import result


def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield (3)
    print("step 3")
    yield (5)


o = odd()

result = next(o)

result2 = next(o)

# --- 实战 2: 内存占用对比 ---
print("2. [性能] 生成器 vs 列表 内存大比拼")

# 创建一个包含 100 万个数字的列表 (一次性生成)
large_list = [i for i in range(1000000)]

# 创建一个生成 100 万个数字的生成器 (此时并未生成，只存了逻辑)
large_gen = (i for i in range(1000000))  # 注意是用圆括号 ()

# sys.getsizeof() 查看对象占用内存字节数
size_list = sys.getsizeof(large_list)
size_gen = sys.getsizeof(large_gen)

print(f"   📦 列表占用内存: {size_list:,} Bytes (约 {size_list / 1024 / 1024:.2f} MB)")
print(f"   ⚡️ 生成器占用内存: {size_gen:,} Bytes (极小！)")
print(f"   🏆 结论: 生成器省了 {size_list / size_gen:.0f} 倍的内存！")

# 证明生成器也能用
print(
    f"   (从生成器取前3个数: {next(large_gen)}, {next(large_gen)}, {next(large_gen)})"
)
