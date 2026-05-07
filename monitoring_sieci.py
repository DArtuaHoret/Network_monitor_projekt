#!/usr/bin/env python3
"""
Monitor sieciowy - wersja podstawowa
"""
import csv
import socket
import subprocess
import re
from datetime import datetime

# --- Konfiguracja ---
hosts = [
    {"name": "Google DNS", "ip": "8.8.8.8", "ports": [53, 80]},
    {"name": "Cloudflare DNS", "ip": "1.1.1.1", "ports": [53, 80]}
]
timeout = 2

import sys

def ping(host):
    """Windows i Linux"""
    try:
        if sys.platform == "win32":
            cmd = ["ping", "-n", "1", "-w", str(timeout * 1000), host]
        else:
            cmd = ["ping", "-c", "1", "-W", str(timeout), host]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            output = result.stdout
            
            # Windows: "czas=14ms" lub "czas<1ms"
            match = re.search(r'czas[=<]\s*([0-9.]+)', output, re.IGNORECASE)
            if match:
                return float(match.group(1))
            
            # Windows EN: "time=14ms"
            match = re.search(r'time[=<]\s*([0-9.]+)', output, re.IGNORECASE)
            if match:
                return float(match.group(1))
            
            # Linux: "time=14.2 ms"
            match = re.search(r'time=([0-9.]+)\s*ms', output, re.IGNORECASE)
            if match:
                return float(match.group(1))
        
        return None
    except Exception:
        return None

def check_tcp(ip, port):
    """Sprawdza dostępność portu TCP"""
    try:
        with socket.create_connection((ip, port), timeout):
            return True
    except Exception:
        return False

# --- Główna pętla ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_file = f"network_log_{timestamp}.csv"

with open(csv_file, mode="w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Host", "IP", "Status", "Latency_ms", "Port", "Port_Status"])

print("MONITOR SIECIOWY")
print("=" * 40)

for host in hosts:
    name = host["name"]
    ip = host["ip"]
    
    print(f"\n{name} [{ip}]")
    
    # Ping
    latency = ping(ip)
    if latency is not None:
        print(f"  Ping: {latency} ms (UP)")
        status = "UP"
    else:
        print(f"  Ping: BRAK (DOWN)")
        status = "DOWN"
    
    # Porty
    for port in host["ports"]:
        is_open = check_tcp(ip, port)
        if is_open:
            print(f"  Port {port}: open")
        else:
            print(f"  Port {port}: closed")
        
    # Log do CSV
    with open(csv_file, mode="a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), name, ip, status, latency or "", port, "open" if is_open else "closed"])

print("\n" + "=" * 40)
print(f"Log zapisany do: {csv_file}")
