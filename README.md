---

# **Civil Unrest Predictor**
This repository demonstrates the use of a machine learning model to predict civil unrest in Chicago by analyzing real-time and historical data from the GDELT Event API.

## **Methodology**
The machine learning model is designed to analyze real-time event reporting published every 15 minutes by the GDELT Event API. By leveraging patterns in the data, the model predicts the likelihood of recurring civil unrest events.

## **Data**
### **Labels**
- The target variable (label) is derived from GDELT Event API records categorized with `145` or `145X` Event Codes. These tags correspond to incidents of civil unrest (e.g., riots, protests) as defined by the GDELT taxonomy.

### **Features**
- The primary feature is the "AvgTone," which reflects the sentiment of media reporting at the time of the event. 
- Additional features may include economic indicators such as the S&P 500 index or an inflation index to contextualize potential underlying causes of unrest.

---
