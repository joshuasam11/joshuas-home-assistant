# joshuas-home-assistant
Home Assistant MQTT Integration Assignment - Joshua S
# 🏠 Home Assistant – MQTT Integration Assignment  
### Submitted by **Joshua S**

---

## 👤 Student Details
- **Name:** ```Joshua S```
- **Register Number:** ```42612024```
- **MQTT Topic Used:** `home/joshuas-2025/sensor`  

---

## 📌 Project Overview
This project demonstrates integration between:

- **Python script** (sensor publisher)
- **Mosquitto MQTT broker**
- **Home Assistant**
- **Docker**
- **Live sensor visualization on Home Assistant Dashboard**


---

## 🛠 Tech Stack
- **Python**
- **Paho MQTT**
- **Docker Desktop (WSL2)**
- **Mosquitto MQTT Broker**
- **Home Assistant**
- **VS Code**
  
---

## 🧩 Components Used
| Component | Purpose |
|----------|----------|
| **Home Assistant (Docker)** | Displays live sensor data |
| **Mosquitto MQTT Broker** | Handles MQTT publish/subscribe |
| **Python (Paho MQTT)** | Publishes sensor JSON payload |
| **VS Code** | Development & execution |
| **Docker Desktop (WSL2)** | Runs Home Assistant & Mosquitto |

---

## 🗂️ Folder Structure
    joshuas-assignment/

    │── publisher.py

    │── docker-compose.yml

    │── README.md

    │── summary.pdf

    │── screenshots/

         ├── home_assistant_dashboard.png

         ├── mqtt_terminal.png

         └── python_running.png

    │  ── homeassistant/

         └── configuration.yaml


---

## 🛠️ Setup Instructions

### 1️⃣ Start Docker Containers
```docker compose up -d```

### 2️⃣ Check Running Containers

```docker compose ps```

### 3️⃣ Run the Python Publisher

```python publisher.py```

### 4️⃣ Verify MQTT Data

```docker exec -it mosquitto mosquitto_sub -t "home/joshuas-2025/sensor" -v```

### 5️⃣ Restart Home Assistant (if needed)

```docker compose restart homeassistant```


---

## 📡 MQTT Publishing Details

### ✔ Unique Topic

```home/joshuas-2025/sensor```

### ✔ JSON Payload Format

```
{
    "temperature": 25,
    "humidity": 60,
    "gas_level": 350
}
```

### ✔ Extra Sensor Used

```Gas Level Sensor: represents gas concentration(ppm), commonly used in safety and IoT monitoring systems.```


---

## 📊 Home Assistant Sensors

### Configured using value_json to decode the JSON payload:

```Temperature(°C)```

```Humidity(%)```

```Gas Level(ppm)```

All three update live every 5 seconds as the Python script publishes new data.


---

## 🖥️ Dashboard Preview

### Screenshot is included under:

```screenshots/home_assistant_dashboard.png```

It displays three live sensor cards.




