import os
from openai import OpenAI

token = os.environ.get("OPENROUTER_KEY")
if not token:
    print("❌ 没拿到 OpenRouter Key，请检查 Secrets 配置！")
    exit(1)

print(f"✅ 成功拿到 Key，开头是: {token[:8]}...")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=token
)

print("⏳ 正在呼叫海外顶尖大模型...")

try:
    response = client.chat.completions.create(
        # 🌟 这里用的是 Google Gemini 的免费版本，极度聪明且免费
        model="google/gemini-flash-1.5:free", 
        messages=[{"role": "user", "content": "请用一句话证明你已经在微软的云端服务器上苏醒了！"}]
    )
    print("\n🤖 AI 的回答：")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"\n❌ 报错了，完整错误如下：\n{e}")