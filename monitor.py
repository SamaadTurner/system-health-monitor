import psutil
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 70
MEMORY_THRESHOLD = 80

# Get current usage
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log message
log_line = f"[{timestamp}] CPU: {cpu_usage}% | Memory: {memory_usage}%\n"

# Write to log file
with open("health.log", "a") as f:
    f.write(log_line)

# Print alert if thresholds are exceeded
if cpu_usage > CPU_THRESHOLD or memory_usage > MEMORY_THRESHOLD:
    print("⚠️ Alert: Resource usage exceeded threshold!")
    print(log_line)
else:
    print("✅ System healthy.")
