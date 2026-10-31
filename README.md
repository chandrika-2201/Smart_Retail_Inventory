# 🛍️ Smart Retail Inventory & Sales Management System

## 📌 Project Overview

The **Smart Retail Inventory & Sales Management System** is a web-based application developed to help retailers monitor inventory, analyze retail data, identify products that require restocking, and generate AI-assisted business recommendations.

The application provides an interactive dashboard that displays inventory information, product stock levels, inventory valuation, demand forecast estimates, and customer segmentation. It uses Python and Flask for backend processing, pandas for data handling, scikit-learn for customer segmentation, and Chart.js for data visualization.

This project is an academic prototype designed to demonstrate how data analytics and machine learning techniques can support retail inventory management and business decision-making.

## 🎯 Objectives

- Develop a web-based retail intelligence dashboard.
- Display product details, stock levels, and reorder thresholds.
- Identify products that require restocking.
- Estimate product demand using a rule-based forecasting approach.
- Perform customer segmentation using the K-Means clustering algorithm.
- Generate recommendations to support inventory planning and retail decisions.
- Present retail information through charts and summary metrics.

## ✨ Key Features

### 1. Retail Dashboard
- Displays summary metrics for revenue, inventory value, customers, and products.
- Provides an overview of retail inventory status.
- Presents information through an interactive dashboard.

### 2. Inventory Management
- Reads product information from a CSV file.
- Displays product names, categories, current stock, and reorder levels.
- Identifies products that have reached or fallen below their reorder thresholds.
- Calculates inventory value using stock quantity and unit price.

### 3. Demand Forecasting
- Provides estimated demand-related values for individual products.
- Compares current stock with reorder levels.
- Assigns a recommended action, such as `REORDER` or `MONITOR`.
- Exposes forecasting information through a Flask API endpoint.

**Note:** The current forecasting logic uses predefined rules rather than a trained predictive forecasting model.

### 4. Customer Segmentation
- Uses the K-Means clustering algorithm from scikit-learn.
- Groups sample customer records using recency, frequency, and monetary-value features.
- Returns the number of customers assigned to each segment through an API endpoint.

**Note:** The current implementation uses sample customer data for demonstrating segmentation.

### 5. AI-Assisted Business Recommendations
The application generates recommendations such as:
- Prioritize replenishment for high-demand products.
- Monitor products approaching their reorder thresholds.
- Use customer segments to support targeted campaigns.
- Improve forecasting when current stock and supplier lead-time data become available.

### 6. Data Visualization
- Displays retail information through dashboard charts.
- Uses Chart.js for frontend visualizations.
- Presents inventory and forecasting information in a graphical format.

## 🛠️ Technologies Used

| Component | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| Data Processing | pandas |
| Machine Learning | scikit-learn |
| Clustering Algorithm | K-Means |
| Data Visualization | Chart.js |
| Input Data | CSV |
| Development Environment | Visual Studio Code |

## 🏗️ System Architecture

The application follows a web-based client-server architecture.

```text
                Retail User
                     |
                     v
          Frontend Web Application
             HTML, CSS, JavaScript
                     |
                     v
             Flask Web Server
                     |
          +----------+----------+
          |          |          |
          v          v          v
      Dashboard   Forecast   Segmentation
       Metrics      API          API
          |          |          |
          +----------+----------+
                     |
                     v
              Data Processing
              Python + pandas
                     |
          +----------+----------+
          |                     |
          v                     v
      products.csv       Sample Customer Data
          |                     |
          v                     v
    Inventory Analysis     K-Means Clustering
                     |
                     v
           Results and Insights
```

**Current implementation:** Product information is loaded from `data/products.csv`. Forecast estimates and customer segmentation are generated through Python backend routes. The supplied project does not configure a persistent SQL database.

## 📂 Project Structure

```text
Smart_Retail_Advanced_App/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── data/
│   └── products.csv
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── app.js
```

### File Description

- **`app.py`** — Creates the Flask application, reads product data, calculates dashboard metrics, and provides forecast, segmentation, and recommendation endpoints.
- **`requirements.txt`** — Lists the Python dependencies required to run the application.
- **`data/products.csv`** — Contains the product information used by the application.
- **`templates/index.html`** — Defines the dashboard layout and inventory table.
- **`static/css/style.css`** — Contains the dashboard styling.
- **`static/js/app.js`** — Handles frontend interactions and chart rendering.
- **`README.md`** — Provides project documentation and setup instructions.

## ⚙️ Installation and Setup

### Prerequisites

Install the following software before running the project:

- Python 3.10 or a compatible Python version.
- Visual Studio Code or another code editor.
- A modern web browser.
- pip, the Python package installer.

### Step 1: Extract the Project

Extract the `Smart_Retail_Advanced_App.zip` file into your preferred directory.

Open the extracted project folder in Visual Studio Code.

### Step 2: Create a Virtual Environment

Open the VS Code terminal and execute:

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows Command Prompt:**

```bash
venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

Run the following command:

```bash
python -m pip install -r requirements.txt
```

The project requires Flask, pandas, and scikit-learn.

### Step 5: Start the Application

Execute:

```bash
python app.py
```

### Step 6: Open the Dashboard

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

The Smart Retail Intelligence dashboard should appear.

To stop the server, press `Ctrl + C` in the terminal.

## 🔗 Backend API Endpoints

The Flask application provides the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Loads the main dashboard and product information. |
| GET | `/api/forecast` | Returns estimated product demand values and recommended actions. |
| GET | `/api/segments` | Returns customer counts for the generated K-Means segments. |
| GET | `/api/insights` | Returns a list of business recommendations. |

### Example: Forecast API

Open the following endpoint in your browser while the application is running:

```text
http://127.0.0.1:5000/api/forecast
```

The endpoint returns JSON containing product names, estimated values, and recommended actions.

### Example: Recommendations API

```text
http://127.0.0.1:5000/api/insights
```

This endpoint returns recommendations related to inventory replenishment, stock monitoring, customer segmentation, and future forecasting improvements.

## 📊 Data Processing and Algorithms

### Inventory Analysis

The application compares each product's current stock with its configured reorder level.

- If stock is less than or equal to the reorder level, the product is marked for reordering.
- Otherwise, the product is marked as healthy or assigned a monitoring action, depending on the application module.

Inventory value is calculated using:

**Inventory Value = Sum of (Stock Quantity × Unit Price)**

### Demand Forecast Estimation

The current forecast endpoint calculates an estimated value using the product's stock quantity and reorder level.

The calculation is:

```text
Predicted Value = max(Reorder Level × 1.15, Current Stock × 0.75)
```

The endpoint then assigns a `REORDER` or `MONITOR` action based on the current stock level.

This is a rule-based estimate, not a trained time-series forecasting model. Its accuracy has not been established through validation against historical sales data.

### Customer Segmentation

The project uses **K-Means clustering** with four clusters and sample customer features representing:

- Recency
- Frequency
- Monetary value

The algorithm groups the sample records into four clusters. The current implementation is a demonstration and does not establish validated customer segments from a real retail customer dataset.

## 🧪 Testing and Evaluation

The application can be tested using the following checks:

1. Verify that the dashboard loads successfully.
2. Confirm that product information is displayed from the CSV file.
3. Check whether products at or below their reorder levels are identified.
4. Open the forecast API and verify its JSON response.
5. Open the segmentation API and verify the returned cluster counts.
6. Open the insights API and confirm that recommendations are returned.
7. Verify that dashboard charts render correctly in the browser.

Actual test results should be recorded after running these checks. Forecast accuracy, performance improvements, and business benefits should not be claimed without appropriate experimental evidence.

## 🔒 Limitations

- The application uses CSV-based product data rather than a configured persistent database.
- Customer segmentation currently uses sample data.
- Demand forecasting is based on a rule-based calculation.
- Revenue and customer dashboard figures include predefined demonstration values.
- Authentication, role-based access control, and production security have not been established by the supplied implementation.
- The application has not been demonstrated to be deployed in a production retail environment.

## 🚀 Future Enhancements

- Integrate a persistent database such as MySQL or SQLite.
- Add secure login and role-based access for administrators and salespersons.
- Connect sales transactions to automatic inventory updates.
- Import historical sales records for demand analysis.
- Train and evaluate forecasting models using suitable historical data.
- Evaluate forecasting performance using metrics such as MAE and RMSE.
- Improve customer segmentation using real customer purchase data.
- Add supplier lead-time tracking and automated reorder recommendations.
- Deploy the application to a cloud platform.
- Add automated testing, logging, and error monitoring.

## 🎓 Academic Project

**Project Title:** Smart Retail Inventory & Sales Management System

**Project Type:** Academic Prototype

**Domain:** Retail Management, Data Analytics, Inventory Intelligence, and Machine Learning

**Purpose:** To demonstrate how web technologies, data processing, clustering, and data visualization can support retail inventory monitoring and business decision-making.

## 📄 License

This project was developed for academic and educational purposes. Add a suitable open-source license before distributing the source code publicly.
