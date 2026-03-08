📊 Google Play Store Data Analysis
📌 Project Overview

This project performs data cleaning, preprocessing, and exploratory data analysis (EDA) on the Google Play Store Apps Dataset.
The goal is to transform raw app store data into a clean and analyzable dataset and generate insights about app categories, ratings, installs, pricing, and user engagement.

The project demonstrates a complete data analytics workflow including data extraction, cleaning, feature preparation, visualization, and automated reporting.

🛠 Technologies Used

Python

Pandas

NumPy

Seaborn

Matplotlib

ydata-profiling


File	Description

googleplaystore.csv	        Raw dataset
cleaned_google_playstore.csv	Cleaned dataset
cleaned_data_report.html	Automated EDA report
day.py	                Data processing and visualization code

📥 Dataset

The dataset contains information about apps available on the Google Play Store.

Key Features

Column	        Description
App	        App name
Category	App category
Rating	        User rating
Reviews	        Number of reviews
Size	        App size
Installs	Number of installs
Type	        Free or Paid
Price	        App price
Content Rating	Age rating
Last Updated	Last update date
Android Ver	Minimum Android version

⚙️ Data Processing Pipeline

1️⃣ Data Extraction : The dataset was extracted from a compressed ZIP archive using Python's zipfile library.

2️⃣ Data Loading

The dataset was loaded into a pandas DataFrame.

Initial exploration included:

.head()

.info()

.describe()

Missing value detection

3️⃣ Data Cleaning

Data Type Conversion : Several columns contained string-formatted numeric data and were converted to numeric types.

Examples:

Reviews → numeric

Price → remove $

Installs → remove + and ,

Size → convert K and M units


4️⃣ Missing Value Handling

Different strategies were applied depending on the column type.

Column	   		Strategy
Rating	   		Mean
Reviews	   		Mean
Installs	   		Median
Price    	   	Median
Size	       		Median
Android Version	Median
Content Rating		Mode
Type				Mode


5️⃣ Duplicate Removal : Duplicate rows were removed to ensure data consistency.

Duplicate apps were also removed by keeping the entry with the highest number of reviews.

6️⃣ Data Quality Fixes : An invalid category entry (1.9) was detected and removed.

📊 Exploratory Data Analysis : Several visualizations were created to explore patterns in the dataset.

Reviews vs Installs

Insight : Apps with higher numbers of reviews tend to have more installs, indicating a positive relationship between popularity and engagement.

Average Rating by Category

Insight : Some categories consistently receive higher user ratings than others.

Free vs Paid Apps

Insight : Paid apps often show slightly higher average ratings, possibly due to better quality control.

Installs by Category

Insight : Categories like Games, Communication, and Social dominate in terms of installs.

📈 Automated Data Report : An automated profiling report was generated using ydata-profiling.

The report includes:

Dataset overview

Missing value analysis

Feature correlations

Variable distributions

Data quality warnings

📦 Output Files

File				Description

cleaned_google_playstore.csv	Cleaned dataset
cleaned_data_report.html	Interactive EDA report

🚀 How to Run the Project

1️⃣ Clone Repository
git clone https://github.com/yourusername/google-playstore-analysis.git

2️⃣ Install Dependencies
pip install pandas seaborn matplotlib ydata-profiling

3️⃣ Run the Script
day.py

📊 Key Insights

Free apps dominate the Play Store.

Paid apps often have slightly higher ratings.

Popular categories generate the highest installs.

Apps with more reviews tend to have more installs.

📌 Future Improvements

Feature engineering

Machine learning model for rating prediction

Interactive dashboard using Plotly or Power BI
