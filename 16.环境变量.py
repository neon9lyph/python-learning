import os

from dotenv import load_dotenv

load_dotenv()  # 这行代码一跑，.env 里的东西就进内存了# ✅ 安全写法：读不到返回 None，不报错
key = os.getenv("OPENAI_API_KEY")

print(key)
# ❌ 危险写法：读不到直接崩溃 (KeyError)# key = os.environ["OPENAI_API_KEY"]
