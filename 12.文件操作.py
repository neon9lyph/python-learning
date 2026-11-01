from pathlib import Path


# open 是内置函数，不需要导入。with 会在代码块结束时自动关闭文件。
# 文本文件显式指定 encoding="utf-8"，方便正确读写中文。
def demo_write(file_path):
    print("\n--- 1. 写入文本：w 模式 ---")
    # w：文件不存在时创建，存在时清空原内容后写入。
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("你好，Python！\n")
        # writelines 不会自动添加换行，需要自己加 \n。
        file.writelines(["第一天：学习文件操作\n", "第二天：练习读取文件\n"])
    print("已写入：", file_path)


def demo_read(file_path):
    print("\n--- 2. 读取文本：r 模式 ---")
    # read() 一次读取全部内容，适合小文件。
    with open(file_path, "r", encoding="utf-8") as file:
        print("全部内容：\n" + file.read(), end="")

    # 每次重新 open，读取位置都会从文件开头开始。
    with open(file_path, "r", encoding="utf-8") as file:
        print("第一行：", repr(file.readline()))
        print("剩余行组成的列表：", file.readlines())
        # 已经读到末尾，再读会得到空字符串；seek(0) 可回到开头。
        print("读到末尾后再读：", repr(file.read()))

    # 遍历文件可逐行处理，不必一次把整个文件读进内存。
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"第 {line_number} 行：{line}", end="")


def demo_append(file_path):
    print("\n--- 3. 追加文本：a 模式 ---")
    # a：在末尾追加，保留已有内容；文件不存在时也会创建。
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("第三天：练习追加内容\n")
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read(), end="")


def demo_binary(directory):
    print("\n--- 4. 二进制读写：wb / rb 模式 ---")
    file_path = directory / "data.bin"
    # 二进制模式读写 bytes，不传 encoding；图片、音频也使用这种模式。
    data = bytes([0, 1, 2, 255])
    with open(file_path, "wb") as file:
        file.write(data)
    with open(file_path, "rb") as file:
        content = file.read()
    print("读取到的字节：", content)
    print("转成整数列表：", list(content))


def demo_paths(directory):
    print("\n--- 5. 使用 pathlib 操作路径和文件 ---")
    folder = directory / "notes"
    folder.mkdir(exist_ok=True)
    file_path = folder / "memo.txt"
    # pathlib 也提供简单的文本读写方法，无需手动 open。
    file_path.write_text("这是一条笔记。", encoding="utf-8")
    print("文件是否存在：", file_path.exists())
    print("笔记内容：", file_path.read_text(encoding="utf-8"))
    renamed_path = file_path.rename(folder / "memo_new.txt")
    print("重命名后目录中的文件：", [path.name for path in folder.iterdir()])
    renamed_path.unlink()
    print("删除后是否存在：", renamed_path.exists())


def main():
    # __file__ 是当前脚本的路径，parent 获取脚本所在目录。
    # 无论从哪个工作目录运行，都会写到当前脚本旁边。
    directory = Path(__file__).resolve().parent
    file_path = directory / "study.txt"
    print("示例目录：", directory)
    # demo_write(file_path)
    # demo_read(file_path)
    # demo_append(file_path)
    demo_binary(directory)
    # demo_paths(directory)
    print("\n演示结束，study.txt 和 data.bin 已保留在脚本同级目录。")


if __name__ == "__main__":
    main()
