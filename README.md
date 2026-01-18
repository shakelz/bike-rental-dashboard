Washington D.C. Bike Rental Analysis Dashboard 🚲
Project Objective

The goal of this project is to analyze the hourly bike rental numbers in Washington D.C. for the years 2011 and 2012. This dashboard explores how different weather conditions and temporal factors (like hours, months, and seasons) affect the total number of bikes rented.

Dataset Information

The analysis is based on the Capital Bikeshare dataset. Key features include:

    Datetime: Hourly date + timestamp.

Weather: Categorized from Clear (1) to Heavy Rain/Snow (4).

Temp/ATemp: Temperature and "feels like" temperature in Celsius.

Humidity & Windspeed: Relative humidity and wind speed.

Count: Total number of rentals (Casual + Registered).

Features (Interactive Dashboard)

As per the requirements for Assignment III:

    Interactive Widgets: Includes a Year selector, Season multi-select filter, and a Temperature range slider.

Visualizations: Contains 5 detailed plots summarizing findings from Exploratory Data Analysis (Assignment I) and Data Visualization (Assignment II).

Deployment: Hosted live on the Streamlit Community Cloud.

Key Insights Summary

Based on the analysis from Assignments I and II:

    Seasonal Trends: The mean of hourly total rentals is highest during the Fall season.

Temporal Patterns: Peak rental counts are observed during morning and evening commute hours (around 8 AM and 5-6 PM).

Weather Impact: Clear and partly cloudy weather (Category 1) leads to the highest rental mean, while heavy rain/snow (Category 4) results in the lowest.

Correlations: Temperature (temp) shows a high correlation with the total rental count.

How to Run Locally

    Clone this repository:
    Bash

git clone https://github.com/your-username/bike-rental-dashboard.git

Navigate to the project folder:
Bash

cd bike-rental-dashboard

Install the required libraries:
Bash

pip install -r requirements.txt

Run the Streamlit app:
Bash

    streamlit run app.py

Technologies Used

    Python: Core programming language.

    Pandas: For data manipulation and cleaning.

Matplotlib & Seaborn: For static data visualizations.

Streamlit: For building the interactive web dashboard.
