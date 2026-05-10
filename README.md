# English Below

# 🖧 Network Monitor

Prosty monitor sieciowy napisany w Pythonie, który sprawdza dostępność hostów 
poprzez ping oraz skanowanie portów TCP, a wyniki zapisuje do pliku CSV.

## Jak działa

1. Dla każdego zdefiniowanego hosta wysyła pojedynczy pakiet ICMP (ping)
2. Mierzy czas odpowiedzi (latencję w ms)
3. Sprawdza dostępność wskazanych portów TCP (np. 53, 80)
4. Wszystkie wyniki zapisuje do pliku CSV z timestampem w nazwie

## wymagany Python 3.x


## Użycie

```bash
python network_monitor.py
```

Wynik zostanie wyświetlony w konsoli oraz zapisany do pliku `network_log_YYYY-MM-DD_HH-MM-SS.csv`.

## Konfiguracja

Listę monitorowanych hostów i portów można edytować bezpośrednio w skrypcie:

```python
hosts = [
    {"name": "Google DNS", "ip": "8.8.8.8", "ports": [53, 80]},
    {"name": "Cloudflare DNS", "ip": "1.1.1.1", "ports": [53, 80]}
]
```

## Przykładowy output CSV

| Time | Host | IP | Status | Latency_ms | Port | Port_Status |
|---|---|---|---|---|---|---|
| 2026-05-07 12:00:01 | Google DNS | 8.8.8.8 | UP | 14.0 | 80 | open |


-----------------------------------------------------------


# 🖧 Network Monitor

A simple network monitoring tool written in Python that checks host availability
using ping and TCP port scanning, and saves the results to a CSV file.

## How It Works

1. Sends a single ICMP packet (ping) to each defined host
2. Measures response time (latency in ms)
3. Checks the availability of specified TCP ports (e.g. 53, 80)
4. Saves all results to a CSV file with a timestamp in the filename

## Python 3.x required


## Usage

```bash
python network_monitor.py
