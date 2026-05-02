# Hair Loss Risk Factors Analysis

Overview
This project explores how various medical, biological, and lifestyle factors relate to hair loss patterns. The analysis combines exploratory data analysis and a basic machine learning approach to understand which factors show stronger associations when considered individually and collectively.

The focus is not only on identifying trends, but also on evaluating how multiple variables interact in influencing outcomes.

---

Dataset Description
The dataset includes a mix of categorical and numerical variables representing:

- Medical conditions (e.g., alopecia, dermatitis, psoriasis)
- Medications and treatments (e.g., antibiotics, steroids, chemotherapy)
- Nutritional deficiencies (e.g., iron, biotin, vitamin deficiencies)
- Demographics (age)
- Lifestyle factors:
  - Stress levels (Low, Moderate, High)
  - Smoking habits (Yes/No)
  - Weight loss (Yes/No)
  - Poor hair care habits (generalized indicator of potentially damaging practices)
- Genetic and hormonal influences

The target variable:
- Hair Loss (0 = No, 1 = Yes)

Stress levels are treated as ordinal categories to reflect increasing intensity, while binary variables represent the presence or absence of specific conditions or behaviors.

Objectives
- Identify key factors associated with hair loss
- Compare the impact of medical versus lifestyle variables
- Understand how multiple variables interact
- Validate findings using a machine learning model

---

Tools and Technologies
- Python
  - Pandas (data cleaning and transformation)
  - NumPy (numerical operations)
  - Scikit-learn (Random Forest model)
- Power BI
  - Dashboard creation
  - Interactive filtering and visualization

---

Analysis Approach

1. Data Cleaning
- Handled missing values ("No Data" converted to null)
- Standardized categorical fields
- Created derived features (e.g., Age Categories)

2. Exploratory Data Analysis
Used grouping and aggregation techniques to evaluate:

- Hair loss rate by medical condition
- Age and genetics interaction
- Lifestyle factors (stress, smoking, weight loss)
- Treatment and medication patterns

Focus was placed on rates (mean) rather than counts to ensure meaningful comparisons.

3. Feature Engineering
- Converted categorical variables into numerical format
- Encoded binary and ordinal features
- Applied one-hot encoding where necessary

4. Machine Learning (Feature Importance)
A Random Forest Classifier was used to:

- Evaluate feature importance
- Understand which variables contribute most when considered together

This complements exploratory analysis by providing a multi-variable perspective rather than isolated comparisons.



Key Insights
- Medical conditions show relatively stronger association with hair loss compared to most lifestyle factors  
- Age plays a consistent role across multiple analyses  
- Lifestyle variables such as stress and smoking show moderate or inconsistent influence  
- Weight loss and hormonal factors indicate some level of association  
- Feature importance analysis supports the relative importance of age and biological factors  



Dashboard
An interactive Power BI dashboard was created to visualize:

- Hair loss rate across different segments
- Medical condition comparisons
- Age and genetics interaction
- Lifestyle factor distributions
- Feature importance (from machine learning output)

Dashboard Link: https://app.powerbi.com/links/x6KrLFqEH2?ctid=bc88ed7e-984d-4728-939e-6ab8bfeaba1d&pbi_source=linkShare



Notes
- The dataset is suitable for exploratory and learning purposes  
- Observed relationships are associative, not causal  
- Results should not be interpreted as clinical conclusions  

---
 Future Improvements
- Use larger and more clinically validated datasets  
- Apply advanced models such as logistic regression or gradient boosting  
- Perform statistical testing for significance  
- Incorporate time-based or longitudinal data  


This project was built as part of a learning exercise to connect data analysis, visualization, and basic machine learning into a single workflow.

Feedback and suggestions are welcome.
