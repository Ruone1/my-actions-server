import platform
import psutil
import time
import os

def get_size(bytes):
    """把字节转换成人类能看懂的大小"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

print("=========================================")
print("🚀 欢迎使用微软 GitHub Actions 免费云端服务器！")
print("=========================================")

print(f"🖥️ 操作系统: {platform.system()} {platform.release()}")
print(f"⚙️ 处理器架构: {platform.machine()}")

# 获取 CPU 核心数
print(f"🧠 CPU 核心数: {psutil.cpu_count()} 核")
print(f"🔄 当前 CPU 使用率: {psutil.cpu_percent(interval=1)}%")

# 获取内存
mem = psutil.virtual_memory()
print(f"💾 总内存: {get_size(mem.total)}")
print(f"💾 空闲内存: {get_size(mem.available)}")

# 获取磁盘
disk = psutil.disk_usage('/')
print(f"💽 总硬盘: {get_size(disk.total)}")
print(f"💽 空闲硬盘: {get_size(disk.free)}")

print("\n⏳ 模拟正在执行高负载任务...")
for i in range(1, 4):
    time.sleep(1)
    print(f"任务执行中... 进度 {i*33}%")
    
print("\n🎉 任务执行完毕！这台价值几千块的服务器即将被微软销毁。")
print("=========================================")