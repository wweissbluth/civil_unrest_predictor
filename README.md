---

# **Civil Unrest Predictor**
This repository demonstrates the use of a machine learning model to predict civil unrest in Chicago by analyzing real-time and historical data from the GDELT dataset.

## **Methodology**
The machine learning model is designed to analyze real-time event reporting by the GDELT. By leveraging patterns in the data, the model predicts the likelihood of civil unrest events.

## **Data**
### **Labels**
The target variable (label) is derived from GDELT Event records categorized with `145` or `145X` Event Codes. These tags correspond to incidents of civil unrest (e.g., riots, protests) as defined by the GDELT taxonomy.

### **Features**
7-day event vectors are the primary features, and the 8th day (the next day) is the label. (In that the prior 7 days help to predict the 8th day.

### Future Additions
Additional features may include economic indicators such as the S&P 500 index or an inflation index to contextualize potential underlying causes of unrest.

---
