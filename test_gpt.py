import os
from openai import OpenAI

# 强制读取 MY_PAT
token = os.environ.get("MY_PAT")
if not token:
    print("❌ 错误：没有获取到 MY_PAT 环境变量！")
    exit(1)

# 打印前4位，确认拿到了钥匙
print(f"✅ 成功拿到 Token，开头为: {token[:4]}...")
print("⏳ 正在连接 Azure GPT 接口...")

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=token
)

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "请用一句话证明你已经被成功唤醒了。"}]
    )
    print("\n🤖 GPT-4o-mini 回答：")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"\n❌ 请求失败，完整报错如下:\n{e}")