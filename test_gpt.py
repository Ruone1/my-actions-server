import os
from openai import OpenAI

# GitHub Actions 运行时会自动注入 GITHUB_TOKEN 环境变量
token = os.environ.get("MY_PAT")

# 加一行打印，让你在 Actions 里能一眼看到底有没有拿到真的密码
if token:
    print(f"✅ 成功拿到 Token，长度: {len(token)}，开头是: {token[:4]}")
else:
    print("❌ 没拿到 Token，请检查 Secrets 配置！")
    exit(1)

# 连接到微软提供的 GitHub Models
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=token 
)

print("⏳ 正在呼叫 GPT-4o-mini 模型...")

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个幽默的 AI，回答简短点。"},
            {"role": "user", "content": "请用一句话证明你已经成功在微软的云端服务器上苏醒了！"}
        ]
    )
    print("\n🤖 GPT 的回答：")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"❌ 调用失败: {e}")