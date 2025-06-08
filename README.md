# SMEMCS – Smart Multi-Environmental Monitoring and Control System

## Overview

Many indoor environments suffer from inadequate ventilation, poor air quality, and high noise or pollution levels. However, many places in cities, suburbs, and infrastructure lack real-time environmental monitoring and automated response systems to address these issues.

SMEMCS aims to provide a low-cost, portable environmental monitoring solution that:
- Monitors key environmental parameters (lighting, air quality, sound, temperature, humidity)
- Detects unsafe levels for each condition
- Responds using a fan, buzzer, and OLED display
- Logs data for collection, analysis, and calibration

This system can be used as-is or expanded into IoT platforms similar to NEST.

## Folder Structure

- `/firmware` – Arduino code (.ino files) and utilities (`/utils`)
- `/hardware` – Schematics, wiring photos, parts list
- `/logs` – Raw and summarized sensor logs
- `/docs` – Planning notes, diagrams, final report
- `/media` – Photos/videos for demo and presentation

## Hardware Components

- KY-038 (Sound Sensor)
- LDR (Light Detector)
- Arduino Uno (Microcontroller)
- DHT22 (Temperature/Humidity Sensor)
- MQ135 (Gas Sensor)
- Breadboard
- LM358 Op-Amp
- IRF540N N-Channel MOSFET
- Flyback Diode
- Buzzer
- LED
- OLED Display
- DC Fan
- Buck Converter (LM2596)
- TVS Diode
- Power Supply
- USB Cable
- Jumper Wires
- Resistors
- Capacitors

## Notes

Initial sensor tests for the LDR and DHT22 showed stable results using Arduino `.ino` sketches. Further analysis will be included in the final report in the `/docs/` folder.
