import os
import time
import psutil
import platform

def get_temp():
    """Les CPU-temperatur fra Raspberry Pi"""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_c = int(f.read()) / 1000
        return f"{temp_c:.1f} °C"
    except FileNotFoundError:
        return "Temperatur ikke tilgjengelig"

def get_uptime():
    """Hent system uptime"""
    with open("/proc/uptime", "r") as f:
        uptime_seconds = float(f.readline().split()[0])
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    return f"{uptime_str} (timer:min:sek)"

def main():
    print("=== Raspberry Pi Status ===")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"CPU temp: {get_temp()}")
    print(f"Uptime: {get_uptime()}")
    print(f"CPU usage: {psutil.cpu_percent(interval=1)} %")
    print(f"Memory usage: {psutil.virtual_memory().percent} %")
    print(f"Disk usage (/): {psutil.disk_usage('/').percent} %")

if __name__ == "__main__":
    main()
