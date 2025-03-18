# 📟 911 Calls Data Analysis 📊  
![Header Image](https://images.squarespace-cdn.com/content/v1/51dc541ce4b03ebab8c5c88c/1472239169814-XBT5J2JNIYW8B3BSX5F7/image-asset.jpeg)  

**Visual representation of emergency services and data analysis.**

---

## 🚀 Project Overview  
This project involves analyzing a real-world dataset of 911 emergency calls from Montgomery County, PA. Through data cleaning, transformation, and visualization, we explore trends in call volume, reasons for calls, and time-based patterns to gain actionable insights.

---

## 📂 Dataset  
**Source:** [Kaggle Dataset - 911 Calls](https://www.kaggle.com/datasets)  
**Description:**  
The dataset contains over 50,000 records of 911 calls in Montgomery County, Pennsylvania.  
It includes information about the type of emergency, location (zip, township), timestamp, and more.

---

## 🔧 Technologies & Libraries  
- **Python 3.x**  
- **Pandas** - Data manipulation  
- **NumPy** - Numerical operations  
- **Matplotlib** - Data visualization  
- **Seaborn** - Statistical data visualization  

---

## 📈 Key Analysis & Insights  
- Top ZIP codes and townships receiving the most calls.  
- Reasons for the 911 calls: EMS, Fire, Traffic.  
- Temporal trends: Calls by hour, day of the week, month.  
- Time series plots of call volume over time for different reasons.  
- Heatmaps and cluster maps showing the frequency of calls by time and day.  

---

## 🗂️ Project Structure  
```plaintext
📁 911-Calls-Data-Analysis
│
├── 911.csv # Dataset (not uploaded in repo due to size)
├── src/ # Source code directory
│   └── 911calls/ # Main package for 911 calls analysis
│       ├── 911CallsCapstone.py # Python script with analysis code
│       └── __init__.py # Package initialization file
├── tests/ # Test cases directory
├── 911CallsCapstone.ipynb # Jupyter Notebook for analysis
├── poetry.lock # Poetry dependency lock file
├── pyproject.toml # Poetry project configuration
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── Images/ # (Optional) Folder for output plots/screenshots
```
---
# 📝 How to Run This Project

## Clone the Repository
```bash
git clone https://github.com/AH-ojaghi/911-Calls-Data-Analysis.git
cd 911-Calls-Data-Analysis
```
Install Dependencies
Make sure you have Python 3.x installed.
Then install the required libraries:

```bash
pip install -r requirements.txt
```
Run the Analysis Script

```bash
python src/911calls/911CallsCapstone.py
```
Explore the Visualizations!
Graphs and charts will be displayed showing insights from the data.

✨ **Features**
- Clean and well-commented code
- Exploratory Data Analysis (EDA)
- Insightful visualizations
- Time series analysis and heatmaps

📌 **Future Enhancements**
- Build an interactive dashboard using Plotly Dash or Streamlit
- Deploy the dashboard as a web app
- Perform predictive modeling on call volume trends

📜 **License**
This project is open source and available under the MIT License.

## ✍️ Author  
**Amirhossein Ojaghi**  
🔗 [GitHub](https://github.com/AH-ojaghi/911-Calls-Capstone)