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

## Coming in Next Version

Alerts if usage exceeds defined thresholds.
