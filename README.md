<div align="center">

# Remaining Useful Life Calculator

![last-commit](https://img.shields.io/github/last-commit/Gushtasp47/Remaining-Useful-Life-Calculator?style=flat&logo=git&logoColor=white&color=0080ff)
![repo-top-language](https://img.shields.io/github/languages/top/Gushtasp47/Remaining-Useful-Life-Calculator?style=flat&color=0080ff)
![repo-language-count](https://img.shields.io/github/languages/count/Gushtasp47/Remaining-Useful-Life-Calculator?style=flat&color=0080ff)

**Built with:**

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=flask&logoColor=white)

An application to estimate the **Remaining Useful Life (RUL)** of equipment or components by analyzing historical and real-time condition/sensor data using regression and machine learning models.

</div>

---

## Table of Contents

- [Project Description](#project-description)
- [Use Cases](#use-cases)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Example Usage](#example-usage)
- [Credits](#credits)

---

## Project Description

This project provides an interactive tool for estimating the **Remaining Useful Life (RUL)** of a machine, device, or component. RUL estimation is critical in predictive maintenance as it helps in planning maintenance actions before failure, minimizing downtime and operational costs. :contentReference[oaicite:0]{index=0}

The system takes sensor/usage inputs and uses predictive models to generate an estimate of how much operational life is left, expressed in cycles, time, or workload units.

---

## Use Cases

- Predict when industrial machinery requires maintenance
- Estimate battery life remaining based on usage profiles
- Support decision-making in maintenance scheduling
- Integration in IoT dashboards for real-time health monitoring

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python, scikit-learn, NumPy |
| **Models** | Regression, Time Series Models, Machine Learning |
| **Web UI** | Flask, HTML, Bootstrap (optional) |
| **Deployment** | Local server / cloud hosting |

---

## Key Features

- Supports multiple predictive models (linear regression, random forest, etc.)
- Processes sensor and time-series data
- Outputs RUL estimates and confidence metrics
- Interactive Flask web interface (optional)
- Extensible for new model integrations
- Clean modular Python codebase

---

## How It Works

### Data Input  
Input can be supplied as CSV sensor logs, time-series features, or real-time measurements.

### Preprocessing  
Data is cleaned, normalized, and transformed into features required by models.

### Model Inference  
Models are trained using historical degradation data and then infer the remaining useful life for current input data.

### Output  
The system returns a numeric RUL estimate and optionally visualization of degradation trends over time.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gushtasp47/Remaining-Useful-Life-Calculator.git
   cd Remaining-Useful-Life-Calculator
   ```

2. **Create a virtual environment(optional):**
    ```bash
    python -m venv venv
    source venv/bin/activate    #macOS/Linux
    venv/Scripts/actiate        #Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
lask, numpy
4. Run the Flask app(user-interface.py):
   ```bash
   python main.py
   ```
5. Open your browser:
   http://127.0.0.1:5000/


## Author

**Author:** Shehzada Gushtasp Khan Mahad Ajmal
**Course:** Data Mining  
**Institution:** Bahria University