# Business Ideas Generator

## Overview
The **Business Ideas Generator** is an AI-powered application that creates innovative startup concepts based on a given industry or theme.  
It leverages the **Mistral** language model via Ollama, with a FastAPI backend for generating ideas and a Streamlit frontend for a simple, interactive interface.

This project is perfect for entrepreneurs, product managers, and innovators looking for fresh, AI-driven business ideas.

---

## ✨ Features

- Generate **three complete business ideas** from a single industry prompt.
- Output includes:
  - **Idea Name**
  - **Detailed Description**
  - **Target Audience**
  - **Revenue Model**
- Industry-focused idea generation.
- FastAPI backend for handling AI requests.
- Streamlit frontend for easy user interaction.
- Powered by **Ollama** and the **Mistral** LLM.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ABDULLAH-ibrahimm/Business-Ideas-Generator.git
cd business-ideas-generator
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull the AI Model
Make sure Ollama is installed, then run:
```bash
ollama pull mistral
```

### 5. Start the Backend
```bash
uvicorn backend.main:app --reload
```

### 6. Start the Frontend
In a separate terminal:
```bash
streamlit run frontend/app.py
```

---

## 📌 Example Usage

**Input:**

Industry: Renewable Energy

**Output:**

**Idea 1 – SolarTrack: Intelligent Solar Tracking System**  
A smart, cost-effective solar tracking system that optimizes energy production by automatically adjusting the angle of solar panels to follow the sun's movement throughout the day. This ensures maximum sunlight absorption and increased efficiency compared to fixed solar panels.  
**Target Audience:** Residential and commercial customers, solar panel installers, utility companies.  
**Revenue Model:** B2B sales of the SolarTrack system, maintenance contracts, and licensing of proprietary technology for international markets.

---

**Idea 2 – WindHarvest: Offshore Wind Energy Harvesting Technology**  
A revolutionary offshore wind energy harvesting technology that captures kinetic energy from ocean currents using a series of turbines designed to minimize environmental impact while maximizing energy output.  
**Target Audience:** Utility companies, renewable energy investors, and governments focused on clean energy transitions.  
**Revenue Model:** B2B sales of the WindHarvest system, long-term service agreements, and partnerships with offshore wind farm developers.

---

**Idea 3 – EcoCharge: Grid-scale Energy Storage Solutions for Renewables**  
A cutting-edge battery storage solution designed to store excess renewable energy generated during peak production hours for later use when demand is high or production is low, increasing efficiency and reliability.  
**Target Audience:** Utility companies, renewable energy project developers, and governments investing in storage infrastructure.  
**Revenue Model:** B2B sales of EcoCharge batteries and management software, long-term service agreements, and partnerships with energy storage system integrators.

---
