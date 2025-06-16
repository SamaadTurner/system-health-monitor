# System Health Monitor

A lightweight Python script that logs CPU and memory usage to a local file. 
## Features

- Logs timestamped CPU and memory usage
- Alerts when thresholds are breached
- Easy to schedule via cron or task scheduler

## Usage

Install dependencies:

```bash
pip install psutil
```

Run the script:

```bash
python monitor.py
```

Check `health.log` for saved metrics.

## 🔔 Coming in Next Version

Real-time alerting when CPU or memory usage exceeds defined thresholds.

This feature will use:

Python requests library to send HTTP POST requests

Slack Incoming Webhooks to deliver alerts directly to a designated Slack channel

Customizable thresholds defined in the script:

CPU_THRESHOLD = 70
MEMORY_THRESHOLD = 80
Example alert:

🚨 System Alert:
• CPU: 92.4%
• Memory: 87.3%
Alerts will be triggered automatically each time the script is run and resource usage crosses the specified limits.


