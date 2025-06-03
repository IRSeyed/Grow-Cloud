# 🌱 GrowCloud – Smart Environmental Monitor

GrowCloud is a MicroPython-based smart monitor built with an ESP32-S2 Mini that keeps track of:
- 🌡️ **Ambient temperature**
- 💧 **Humidity**
- 🌿 **Soil moisture**

The soil moisture is visualized using a dynamic root graphic on a 1.3" SH1106 OLED display, making plant care intuitive and fun!

---

## 📦 Features

- 🧠 Written entirely in **MicroPython**
- 🌫️ Reads temperature & humidity using **DHT22**
- 🌱 Measures soil moisture using a capacitive analog sensor
- 🖥️ Displays data + animations on a **1.3" SH1106 OLED**
- ⚡ Low power, compact design with **ESP32-S2 Mini**

---

## 🛠️ Hardware Used

| Component                 | Description                          |
|--------------------------|--------------------------------------|
| ESP32-S2 Mini (WEMOS)    | Microcontroller board                |
| DHT22                    | Temperature & humidity sensor        |
| Capacitive Soil Sensor   | Analog soil moisture sensor          |
| SH1106 OLED 128x64       | I2C display module                   |
| 3D Printed Cloud Enclosure | Custom-designed case               |

---

## 📂 File Overview

| File         | Purpose                                  |
|--------------|------------------------------------------|
| `main.py`    | Main logic: sensor reading + OLED output |
| `sh1106.py`  | OLED display driver for SH1106 over I2C  |
| `sprites.py` | Contains `root` sprite for visualization |

---

## 🔌 Wiring Diagram (Pinout)

| Component                | Description                         | ESP32-S2 Mini Pin | Notes                              |
|--------------------------|-------------------------------------|-------------------|-------------------------------------|
| **DHT22**                | Temp & Humidity Sensor (Data)       | GPIO **10**       | Pull-up 10kΩ between Data & VCC *   |
| **Soil Moisture Sensor** | Analog output                       | GPIO **1**        | ADC input (0–3.3V)                  |
| **OLED Display (SDA)**   | I2C Data Line                       | GPIO **8**        | SH1106 1.3" OLED                    |
| **OLED Display (SCL)**   | I2C Clock Line                      | GPIO **9**        | SH1106 1.3" OLED                    |
| **OLED Display (ADDR)**  | I2C Address                         | `0x3C`            | Default SH1106 I2C address          |
| **OLED Reset**           | Reset pin                           | `None`            | Not connected in this project       |

> ℹ️ *If using a bare DHT22 module, place a 10kΩ resistor between VCC and DATA.

---

## 🖨️ 3D Printed Case

Download the 3D printable cloud-shaped enclosure from Thingiverse:  
👉 [https://www.thingiverse.com/thing:7055873](https://www.thingiverse.com/thing:7055873)

---

## 🎥 Demo Video

Watch the full design and build process:  
🎬 **[GrowCloud – This Cloud Knows When Your Plants Need Water!](https://youtube.com/your_video_link_here)**  
*(Replace with your actual YouTube link)*

---

## 🧑‍💻 Author

**Seyed**


