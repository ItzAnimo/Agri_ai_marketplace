# 🌾 Agri AI Marketplace

An AI-powered digital marketplace designed to connect **farmers/FPOs directly with consumers and bulk buyers**, while using machine learning for **demand forecasting, price prediction, and logistics estimation**.

The goal is to reduce unnecessary intermediaries, improve farmer realization, reduce wastage, and help buyers make better procurement decisions.

---

## 🚨 Problem

Agricultural supply chains often involve multiple intermediaries between farmers and final buyers.

This can result in:

* Lower prices received by farmers
* Higher prices for consumers
* Lack of direct access to buyers
* Difficulty predicting market demand
* Uncertain selling prices
* Inefficient transportation planning
* Post-harvest losses
* Poor coordination between supply and demand

---

## 💡 Proposed Solution

Agri AI Marketplace provides a digital platform that connects:

```text
Farmers / FPOs
       │
       ▼
┌─────────────────────┐
│ Agri AI Marketplace │
└─────────────────────┘
       │
       ├── Demand Prediction
       ├── Price Prediction
       ├── Logistics Prediction
       └── Buyer Matching
       │
       ▼
Consumers / Bulk Buyers
```

The platform uses historical agricultural and logistics data to generate predictions that can support better selling and procurement decisions.

---

# 🤖 AI Components

The initial prototype contains three machine-learning components.

### 1. 📈 Demand Prediction

Predicts expected demand for agricultural products using factors such as:

* Previous demand
* Supply
* Base price
* Temperature
* Rainfall
* Humidity
* Crop
* Location

**Model:** LightGBM Regressor

---

### 2. 💰 Price Prediction

Estimates the expected market price using factors such as:

* Base price
* Demand
* Supply
* Crop
* Location

**Model:** LightGBM Regressor

---

### 3. 🚚 Logistics Prediction

Estimates expected delivery time using:

* Distance
* Traffic level
* Rainfall
* Load
* Road quality
* Pickup delay
* Vehicle type
* Driver experience

**Model:** LightGBM Regressor

---

# 🧠 Technology Stack

### Programming

* Python

### Machine Learning

* LightGBM
* Scikit-learn
* NumPy
* Pandas

### Application

* Streamlit

### Model Management

* Joblib

### Version Control

* Git
* GitHub

---

# 📁 Project Structure

```text
agri-ai-marketplace/
│
├── app.py
├── requirement.txt
├── .gitignore
│
├── data/
│
├── models/
│
└── training/
    ├── create_data.py
    ├── train_demand.py
    ├── train_price.py
    └── train_logistics.py
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/agri-ai-marketplace.git
```

Move into the project directory:

```bash
cd agri-ai-marketplace
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

---

## 3. Install dependencies

```powershell
python -m pip install -r requirement.txt
```

---

# 📊 Generate Dataset

The prototype currently uses a generated agricultural dataset for development and testing.

Run:

```powershell
python training/create_data.py
```

This creates:

```text
data/agriculture_data.csv
```

The dataset contains agricultural, weather, market and logistics variables.

---

# 🤖 Train the Models

### Demand Model

```powershell
python training/train_demand.py
```

### Price Model

```powershell
python training/train_price.py
```

### Logistics Model

```powershell
python training/train_logistics.py
```

The trained models are stored inside:

```text
models/
```

---

# 🖥️ Run the Application

Start the Streamlit application:

```powershell
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

The dashboard allows users to enter agricultural and logistics information and receive AI-generated predictions.

---

# 🔄 AI Workflow

```text
                 DATA
                   │
        ┌──────────┴──────────┐
        │                     │
 Agricultural Data       Logistics Data
        │                     │
        └──────────┬──────────┘
                   │
                   ▼
             Data Processing
                   │
                   ▼
          ┌─────────────────┐
          │    LightGBM     │
          └─────────────────┘
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     Demand      Price     Delivery
   Prediction  Prediction    Time
        │          │          │
        └──────────┼──────────┘
                   ▼
             AI Dashboard
                   │
                   ▼
          Decision Support
```

---

# 🎯 Expected Benefits

### For Farmers

* Better access to buyers
* Improved price visibility
* Demand-based selling decisions
* Reduced dependence on intermediaries
* Better logistics planning

### For Buyers

* Better procurement planning
* Demand forecasting
* Price estimation
* Delivery-time estimation
* Direct access to agricultural suppliers

### For Consumers

* Potentially lower prices
* Better availability
* Improved supply-chain efficiency

---

# 🚀 Future Scope

The current prototype can be expanded into a complete agricultural marketplace.

### 🔹 Real-Time Market Data

Integrate:

* Mandi prices
* Government agricultural datasets
* Weather APIs
* Market demand
* Crop arrivals

---

### 🔹 Intelligent Farmer-Buyer Matching

The system can recommend the best buyer for a farmer based on:

```text
Crop
+
Quantity
+
Expected Price
+
Buyer Demand
+
Distance
+
Transportation Cost
```

---

### 🔹 Dynamic Pricing

The platform can estimate a recommended selling price based on:

* Current demand
* Supply
* Historical prices
* Seasonal trends
* Weather
* Market location

---

### 🔹 Logistics Optimization

Future versions can optimize:

```text
Farmer
   ↓
Collection Point
   ↓
Vehicle
   ↓
Buyer
```

based on distance, traffic, vehicle capacity, road conditions and delivery requirements.

---

### 🔹 IoT Integration

IoT sensors can provide real-time information such as:

* Temperature
* Humidity
* Soil conditions
* Storage conditions
* Milk/food temperature
* GPS/location

This data can be fed into the AI system for improved predictions.

---

### 🔹 AI Agent

A future AI agent can act as an agricultural marketplace assistant.

For example:

> "I have 800 kg of tomatoes available tomorrow. Where should I sell them?"

The agent could analyze:

```text
Current Demand
      +
Market Prices
      +
Nearby Buyers
      +
Transportation Cost
      +
Expected Profit
```

and recommend the best option.

---

# 🏆 SIH Vision

The long-term objective is to create an intelligent agricultural ecosystem where:

```text
Farmer
   ↓
AI Analysis
   ↓
Best Buyer
   ↓
Best Price
   ↓
Optimized Logistics
   ↓
Consumer / Bulk Buyer
```

Instead of simply creating another marketplace, the platform aims to provide **AI-powered decision support throughout the agricultural supply chain**.

---

# 👨‍💻 Project Status

### Current

* [x] Initial project structure
* [x] Streamlit application
* [x] Synthetic dataset generator
* [x] Demand prediction training script
* [x] Price prediction training script
* [x] Logistics prediction training script
* [x] LightGBM integration

### In Development

* [ ] Model evaluation
* [ ] Real agricultural dataset
* [ ] Farmer dashboard
* [ ] Buyer dashboard
* [ ] Buyer-farmer matching
* [ ] Dynamic pricing
* [ ] Logistics optimization
* [ ] Real-time market data
* [ ] AI assistant/agent
* [ ] IoT integration

---

# 📜 License

This project is developed as an academic/hackathon prototype.

License can be added when the project is finalized.
