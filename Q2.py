import psutil
import time

THRESHOLD = 80  # CPU usage percentage

def monitor_cpu():
    try:
        while True:
            usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {usage}%")
            if usage > THRESHOLD:
                print(f"ALERT! CPU usage exceeded {THRESHOLD}%: {usage}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()