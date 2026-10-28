user_data = {"name": "Sora"}


try:
    print(user_data["age"])
except Exception:
    print("数据缺失，使用默认年龄: 18")
