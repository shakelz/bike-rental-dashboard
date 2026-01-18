import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="D.C. Bike Rental Dashboard", layout="wide")

# --- DATA LOADING & PRE-PROCESSING ---
@st.cache_data
def load_data():
    # Dataset downloaded from Kaggle as per objective
    df = pd.read_csv('train.csv')
    
    # Task 3.1.1: Convert to datetime
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    # Task 3.1.3: Extract time features
    df['year'] = df['datetime'].dt.year
    df['month'] = df['datetime'].dt.month
    df['hour'] = df['datetime'].dt.hour
    df['day_of_week'] = df['datetime'].dt.day_name()
    
    # Task 3.1.4: Rename season values
    season_dict = {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'}
    df['season'] = df['season'].map(season_dict)
    
    # Task 3.1.11: Create day_period column
    def get_period(h):
        if 0 <= h < 6: return 'night'
        elif 6 <= h < 12: return 'morning'
        elif 12 <= h < 18: return 'afternoon'
        else: return 'evening'
    df['day_period'] = df['hour'].apply(get_period)
    
    return df

df = load_data()

# --- SIDEBAR: INTERACTIVE WIDGETS ---
st.sidebar.header("🔧 Dashboard Filters")

# Widget 1: Year Selector
year_choice = st.sidebar.selectbox("Saal chunno (Year):", [2011, 2012, "Both"])

# Widget 2: Season Multi-select
all_seasons = ['spring', 'summer', 'fall', 'winter']
selected_seasons = st.sidebar.multiselect("Seasons filter karo:", all_seasons, default=all_seasons)

# Widget 3: Temperature Range Slider
temp_range = st.sidebar.slider("Temperature Range (°C):", 
                               float(df['temp'].min()), float(df['temp'].max()), 
                               (float(df['temp'].min()), float(df['temp'].max())))

# --- FILTERING LOGIC ---
mask = (df['season'].isin(selected_seasons)) & \
       (df['temp'].between(temp_range[0], temp_range[1]))

if year_choice != "Both":
    mask = mask & (df['year'] == year_choice)

filtered_df = df[mask]

# --- MAIN DASHBOARD: HEADER ---
st.title("🚲 Washington D.C. Bike Rental Interactive Dashboard")
# Ye hai line 66 ka sahi version:
st.markdown("**Objective:** Analyze and explore the effect of weather and temporal factors on bike rentals.")

# --- SUMMARY OF FINDINGS ---
with st.expander("📖 View Key Insights from Assignment 1 & 2"):
    st.write("""
    * **Peak Demand:** Rentals peak during commute hours (8 AM and 5-6 PM) on working days.
    * **Seasonality:** Fall shows the highest mean of hourly rentals.
    * **Weather Impact:** Clear weather boosts rentals; Heavy Rain/Snow causes a sharp decline.
    * **Correlation:** Temperature has the strongest positive correlation with rentals.
    """)

# --- DASHBOARD PLOTS ---

# Row 1: Metrics & Monthly Trends
col1, col2 = st.columns([1, 2])
with col1:
    st.metric("Total Rentals", f"{filtered_df['count'].sum():,}")
    st.metric("Average Temperature", f"{filtered_df['temp'].mean():.1f}°C")
    st.metric("Avg Registered Users", f"{filtered_df['registered'].mean():.1f}")

with col2:
    st.subheader("Monthly Mean Rentals")
    fig_month, ax_month = plt.subplots()
    sns.barplot(data=filtered_df, x='month', y='count', palette='viridis', ax=ax_month)
    st.pyplot(fig_month)

# Row 2: Hourly Trends & Weather Impact
col3, col4 = st.columns(2)
with col3:
    st.subheader("Hourly Peak Patterns")
    fig_hour, ax_hour = plt.subplots()
    sns.lineplot(data=filtered_df, x='hour', y='count', hue='workingday', ax=ax_hour)
    st.pyplot(fig_hour)

with col4:
    st.subheader("Weather Category vs Rentals (95% CI)")
    fig_weather, ax_weather = plt.subplots()
    sns.pointplot(data=filtered_df, x='weather', y='count', ax=ax_weather)
    st.pyplot(fig_weather)

# Row 3: Day Period & Correlation
col5, col6 = st.columns(2)
with col5:
    st.subheader("Rentals by Day Period")
    fig_period, ax_period = plt.subplots()
    sns.barplot(data=filtered_df, x='day_period', y='count', order=['morning', 'afternoon', 'evening', 'night'], ax=ax_period)
    st.pyplot(fig_period)

with col6:
    st.subheader("Correlation Matrix Heatmap")
    fig_corr, ax_corr = plt.subplots()
    sns.heatmap(filtered_df[['temp', 'atemp', 'humidity', 'windspeed', 'count']].corr(), annot=True, cmap='coolwarm', ax=ax_corr)
    st.pyplot(fig_corr)

st.sidebar.markdown("---")
st.sidebar.write("Developed by Abdul")
