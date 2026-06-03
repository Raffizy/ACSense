# ACSence | DualSense Adaptive Trigger Integration for Assetto Corsa

## Overview
This project integrates real-time telemetry from Assetto Corsa with the PlayStation DualSense controller, mapping driving inputs such as throttle and brake pressure to adaptive trigger resistance to enhance driving immersion.

The goal of the project is to explore real-time telemetry processing, hardware interaction, and low-latency feedback using a modular, hybrid architecture.

---

## Architecture
The system is split into two independent components:

- **Telemetry Reader (C#)**  
  Reads real-time telemetry from Assetto Corsa via shared memory and outputs normalized values (e.g. throttle and brake).

- **DualSense Controller (Python)**  
  Uses a DualSense HID library to control adaptive trigger resistance based on incoming telemetry data.

- **Inter-process Communication**  
  Telemetry data is transmitted locally using a lightweight mechanism such as UDP or standard input/output.

This separation keeps telemetry processing and hardware control isolated and easier to maintain.

---

## Planned Features (Minimum Viable Scope)
- Real-time throttle input mapped to right trigger resistance
- Real-time brake input mapped to left trigger resistance
- Low-latency local data transfer
- Clean start/stop lifecycle for both components

---

## Tech Stack
- **Python** — DualSense HID control and trigger mapping
- **C#** — Assetto Corsa telemetry reader
- **Windows** — Target platform

---

## Project Status
**In progress**

- DualSense adaptive trigger control implemented in Python
- Telemetry extraction currently being replaced with a stable C# implementation
- Minimum viable version targets throttle and brake support only

---

