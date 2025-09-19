import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title="Personal Health Manager",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced mobile-friendly CSS
st.markdown("""
<style>
    /* Main container adjustments */
    .main > div {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        .main > div {
            padding-top: 0.5rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }
        
        /* Hide sidebar on mobile */
        .css-1d391kg {
            display: none;
        }
        
        /* Full width on mobile */
        .block-container {
            max-width: 100% !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    }
    
    /* Enhanced tab design for mobile */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        flex-wrap: wrap;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: nowrap;
        background-color: #f0f2f6;
        border-radius: 8px 8px 0px 0px;
        gap: 2px;
        padding: 12px 16px;
        font-weight: 500;
        font-size: 14px;
        min-width: 80px;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #ff4b4b;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(255, 75, 75, 0.3);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e0e0e0;
        transform: translateY(-1px);
    }
    
    .stTabs [aria-selected="true"]:hover {
        background-color: #e63939;
    }
    
    /* Mobile-specific tab adjustments */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] {
            font-size: 12px;
            padding: 8px 12px;
            height: 50px;
            min-width: 70px;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
    }
    
    /* Mobile-friendly buttons */
    .stButton > button {
        width: 100%;
        height: 48px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Mobile-friendly input fields */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        height: 48px;
        font-size: 16px;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        transition: border-color 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #ff4b4b;
        box-shadow: 0 0 0 3px rgba(255, 75, 75, 0.1);
    }
    
    /* Mobile-friendly metrics */
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 16px;
        color: white;
        text-align: center;
        margin: 8px 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 4px;
    }
    
    .metric-label {
        font-size: 14px;
        opacity: 0.9;
    }
    
    /* Mobile-friendly charts */
    .plotly-graph-div {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Mobile-friendly dataframes */
    .dataframe {
        font-size: 14px;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Mobile-friendly progress bars */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #ff4b4b, #ff6b6b);
        border-radius: 10px;
        height: 12px;
    }
    
    /* Mobile-friendly alerts */
    .stAlert {
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Mobile-friendly columns */
    @media (max-width: 768px) {
        .stColumn {
            margin-bottom: 1rem;
        }
    }
    
    /* Touch-friendly spacing */
    .element-container {
        margin-bottom: 1.5rem;
    }
    
    /* Mobile-friendly headers */
    h1, h2, h3 {
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Mobile-friendly sidebar */
    @media (max-width: 768px) {
        .css-1d391kg {
            display: none !important;
        }
    }
    
    /* Mobile-friendly main content */
    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    }
    
    /* Mobile-friendly success/error messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    /* Mobile-friendly selectbox */
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 8px;
    }
    
    /* Mobile-friendly number input */
    .stNumberInput > div > div > input {
        -webkit-appearance: none;
        -moz-appearance: textfield;
    }
    
    .stNumberInput > div > div > input::-webkit-outer-spin-button,
    .stNumberInput > div > div > input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# Data storage functions
def load_data(filename):
    """Load data from CSV file"""
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame()

def save_data(data, filename):
    """Save data to CSV file"""
    data.to_csv(filename, index=False)

def init_data_files():
    """Initialize data files if they don't exist"""
    data_files = {
        'user_profile.csv': pd.DataFrame(columns=['date', 'weight', 'height', 'age', 'gender', 'activity_level']),
        'weight_log.csv': pd.DataFrame(columns=['date', 'weight']),
        'diet_log.csv': pd.DataFrame(columns=['date', 'meal_type', 'food_name', 'calories', 'protein', 'carbs', 'fat']),
        'workout_log.csv': pd.DataFrame(columns=['date', 'exercise_name', 'duration_minutes', 'calories_burned'])
    }
    
    for filename, default_df in data_files.items():
        if not os.path.exists(filename):
            save_data(default_df, filename)

# Initialize data files
init_data_files()

# Load data
user_profile = load_data('user_profile.csv')
weight_log = load_data('weight_log.csv')
diet_log = load_data('diet_log.csv')
workout_log = load_data('workout_log.csv')

# Helper functions
def calculate_bmi(weight, height):
    """Calculate BMI"""
    if height > 0:
        return round(weight / ((height / 100) ** 2), 1)
    return 0

def get_bmi_category(bmi):
    """Get BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_ideal_weight_range(height, gender):
    """Calculate ideal weight range based on height and gender"""
    # Using Devine formula
    if gender.lower() == 'male':
        ideal_weight = 50 + 2.3 * ((height / 2.54) - 60)
    else:
        ideal_weight = 45.5 + 2.3 * ((height / 2.54) - 60)
    
    # Convert back to kg
    ideal_weight_kg = ideal_weight * 0.453592
    return [round(ideal_weight_kg - 5, 1), round(ideal_weight_kg + 5, 1)]

def calculate_bmr(weight, height, age, gender):
    """Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation"""
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr, 0)

def calculate_tdee(bmr, activity_level):
    """Calculate Total Daily Energy Expenditure"""
    activity_multipliers = {
        'Sedentary': 1.2,
        'Lightly Active': 1.375,
        'Moderately Active': 1.55,
        'Very Active': 1.725,
        'Extremely Active': 1.9
    }
    return round(bmr * activity_multipliers.get(activity_level, 1.2), 0)

def get_vegetarian_food_recommendations():
    """Get vegetarian food recommendations with nutritional info"""
    return {
        'Proteins': {
            'Lentils (1 cup)': {'calories': 230, 'protein': 18, 'carbs': 40, 'fat': 1},
            'Chickpeas (1 cup)': {'calories': 269, 'protein': 15, 'carbs': 45, 'fat': 4},
            'Tofu (100g)': {'calories': 144, 'protein': 17, 'carbs': 3, 'fat': 9},
            'Quinoa (1 cup)': {'calories': 222, 'protein': 8, 'carbs': 40, 'fat': 4},
            'Greek Yogurt (1 cup)': {'calories': 100, 'protein': 17, 'carbs': 6, 'fat': 0},
            'Almonds (1 oz)': {'calories': 164, 'protein': 6, 'carbs': 6, 'fat': 14}
        },
        'Carbs': {
            'Brown Rice (1 cup)': {'calories': 216, 'protein': 5, 'carbs': 45, 'fat': 2},
            'Sweet Potato (1 medium)': {'calories': 103, 'protein': 2, 'carbs': 24, 'fat': 0},
            'Oats (1 cup)': {'calories': 154, 'protein': 6, 'carbs': 27, 'fat': 3},
            'Banana (1 medium)': {'calories': 105, 'protein': 1, 'carbs': 27, 'fat': 0}
        },
        'Fats': {
            'Avocado (1 medium)': {'calories': 234, 'protein': 3, 'carbs': 12, 'fat': 21},
            'Olive Oil (1 tbsp)': {'calories': 119, 'protein': 0, 'carbs': 0, 'fat': 14},
            'Nuts (1 oz)': {'calories': 160, 'protein': 6, 'carbs': 6, 'fat': 14}
        }
    }

# Main app
def main():
    st.title("💪 Personal Health Manager")
    st.markdown("Track your health journey with diet, exercise, and progress monitoring")
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["👤 Profile", "🍽️ Diet", "🏃 Workout", "📊 Dashboard"])
    
    with tab1:
        profile_tab()
    
    with tab2:
        diet_tab()
    
    with tab3:
        workout_tab()
    
    with tab4:
        dashboard_tab()

def profile_tab():
    st.header("👤 User Profile")
    
    # Load current data
    current_user_profile = load_data('user_profile.csv')
    current_weight_log = load_data('weight_log.csv')
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Personal Information")
        
        # Get current date
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Input fields
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=1.0)
        age = st.number_input("Age", min_value=10, max_value=100, value=25, step=1)
        gender = st.selectbox("Gender", ["Male", "Female"])
        activity_level = st.selectbox("Activity Level", 
                                    ["Sedentary", "Lightly Active", "Moderately Active", 
                                     "Very Active", "Extremely Active"])
        
        if st.button("Update Profile", type="primary"):
            # Save profile data
            new_profile = pd.DataFrame({
                'date': [current_date],
                'weight': [weight],
                'height': [height],
                'age': [age],
                'gender': [gender],
                'activity_level': [activity_level]
            })
            
            # Update user_profile
            if not current_user_profile.empty:
                current_user_profile.loc[0] = new_profile.iloc[0]
            else:
                current_user_profile = new_profile
            
            save_data(current_user_profile, 'user_profile.csv')
            
            # Update weight log
            new_weight_log = pd.DataFrame({
                'date': [current_date],
                'weight': [weight]
            })
            
            if not current_weight_log.empty and current_weight_log.iloc[-1]['date'] != current_date:
                current_weight_log = pd.concat([current_weight_log, new_weight_log], ignore_index=True)
            elif current_weight_log.empty:
                current_weight_log = new_weight_log
            else:
                current_weight_log.iloc[-1] = new_weight_log.iloc[0]
            
            save_data(current_weight_log, 'weight_log.csv')
            
            st.success("Profile updated successfully!")
            st.rerun()
    
    with col2:
        st.subheader("Health Metrics")
        
        if not current_user_profile.empty:
            current_profile = current_user_profile.iloc[-1]
            bmi = calculate_bmi(current_profile['weight'], current_profile['height'])
            bmi_category = get_bmi_category(bmi)
            ideal_range = calculate_ideal_weight_range(current_profile['height'], current_profile['gender'])
            bmr = calculate_bmr(current_profile['weight'], current_profile['height'], 
                              current_profile['age'], current_profile['gender'])
            tdee = calculate_tdee(bmr, current_profile['activity_level'])
            
            # Display metrics
            col2_1, col2_2 = st.columns(2)
            with col2_1:
                st.metric("BMI", f"{bmi}", f"{bmi_category}")
                st.metric("Ideal Weight Range", f"{ideal_range[0]} - {ideal_range[1]} kg")
            
            with col2_2:
                st.metric("BMR", f"{int(bmr)} cal/day")
                st.metric("TDEE", f"{int(tdee)} cal/day")
            
            # Weight progress chart
            if len(current_weight_log) > 1:
                st.subheader("Weight Progress")
                fig = px.line(current_weight_log, x='date', y='weight', 
                            title="Weight Over Time", markers=True)
                fig.update_layout(xaxis_title="Date", yaxis_title="Weight (kg)")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Please update your profile to see health metrics")

def diet_tab():
    st.header("🍽️ Diet Management")
    
    # Load current data
    current_user_profile = load_data('user_profile.csv')
    current_diet_log = load_data('diet_log.csv')
    
    # Load current profile for recommendations
    if not current_user_profile.empty:
        current_profile = current_user_profile.iloc[-1]
        tdee = calculate_tdee(
            calculate_bmr(current_profile['weight'], current_profile['height'], 
                         current_profile['age'], current_profile['gender']),
            current_profile['activity_level']
        )
    else:
        tdee = 2000  # Default value
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Log Meal")
        
        meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack"])
        food_name = st.text_input("Food Name")
        
        # Quick food selection
        st.write("**Quick Select (Vegetarian Foods):**")
        food_recommendations = get_vegetarian_food_recommendations()
        
        selected_food = st.selectbox("Choose from recommendations", 
                                   [""] + list(food_recommendations['Proteins'].keys()) + 
                                   list(food_recommendations['Carbs'].keys()) + 
                                   list(food_recommendations['Fats'].keys()))
        
        if selected_food:
            # Auto-fill nutritional info
            for category, foods in food_recommendations.items():
                if selected_food in foods:
                    food_info = foods[selected_food]
                    calories = st.number_input("Calories", value=food_info['calories'], min_value=0)
                    protein = st.number_input("Protein (g)", value=food_info['protein'], min_value=0.0, step=0.1)
                    carbs = st.number_input("Carbs (g)", value=food_info['carbs'], min_value=0.0, step=0.1)
                    fat = st.number_input("Fat (g)", value=food_info['fat'], min_value=0.0, step=0.1)
                    break
        else:
            calories = st.number_input("Calories", min_value=0)
            protein = st.number_input("Protein (g)", min_value=0.0, step=0.1)
            carbs = st.number_input("Carbs (g)", min_value=0.0, step=0.1)
            fat = st.number_input("Fat (g)", min_value=0.0, step=0.1)
        
        if st.button("Log Meal", type="primary"):
            current_date = datetime.now().strftime('%Y-%m-%d')
            new_meal = pd.DataFrame({
                'date': [current_date],
                'meal_type': [meal_type],
                'food_name': [food_name],
                'calories': [calories],
                'protein': [protein],
                'carbs': [carbs],
                'fat': [fat]
            })
            
            current_diet_log = pd.concat([current_diet_log, new_meal], ignore_index=True)
            save_data(current_diet_log, 'diet_log.csv')
            st.success("Meal logged successfully!")
            st.rerun()
    
    with col2:
        st.subheader("Today's Summary")
        
        today = datetime.now().strftime('%Y-%m-%d')
        today_meals = current_diet_log[current_diet_log['date'] == today] if not current_diet_log.empty else pd.DataFrame()
        
        if not today_meals.empty:
            total_calories = today_meals['calories'].sum()
            total_protein = today_meals['protein'].sum()
            total_carbs = today_meals['carbs'].sum()
            total_fat = today_meals['fat'].sum()
            
            col2_1, col2_2 = st.columns(2)
            with col2_1:
                st.metric("Total Calories", f"{int(total_calories)}", f"Target: {int(tdee)}")
                st.metric("Protein", f"{total_protein:.1f}g")
            
            with col2_2:
                st.metric("Carbs", f"{total_carbs:.1f}g")
                st.metric("Fat", f"{total_fat:.1f}g")
            
            # Calorie progress bar
            calorie_progress = min(total_calories / tdee, 1.0)
            st.progress(calorie_progress)
            st.caption(f"Calorie Goal Progress: {calorie_progress:.1%}")
            
            # Meal breakdown
            st.subheader("Meal Breakdown")
            st.dataframe(today_meals[['meal_type', 'food_name', 'calories']], use_container_width=True)
        else:
            st.info("No meals logged today")
        
        # Weekly summary
        st.subheader("Weekly Summary")
        week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        week_meals = current_diet_log[current_diet_log['date'] >= week_ago] if not current_diet_log.empty else pd.DataFrame()
        
        if not week_meals.empty:
            daily_calories = week_meals.groupby('date')['calories'].sum()
            avg_daily_calories = daily_calories.mean()
            
            fig = px.bar(x=daily_calories.index, y=daily_calories.values, 
                        title="Daily Calories (Last 7 Days)")
            fig.add_hline(y=tdee, line_dash="dash", line_color="red", 
                         annotation_text=f"Target: {int(tdee)} cal")
            st.plotly_chart(fig, use_container_width=True)

def workout_tab():
    st.header("🏃 Workout Management")
    
    # Load current data
    current_workout_log = load_data('workout_log.csv')
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Log Workout")
        
        exercise_name = st.text_input("Exercise Name")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, value=30)
        calories_burned = st.number_input("Calories Burned", min_value=0, value=200)
        
        # Exercise suggestions
        st.write("**Exercise Suggestions:**")
        exercise_suggestions = [
            "Walking", "Running", "Cycling", "Swimming", "Yoga", "Pilates",
            "Weight Training", "HIIT", "Dancing", "Hiking", "Tennis", "Basketball"
        ]
        
        selected_exercise = st.selectbox("Choose from suggestions", [""] + exercise_suggestions)
        if selected_exercise:
            exercise_name = selected_exercise
        
        if st.button("Log Workout", type="primary"):
            current_date = datetime.now().strftime('%Y-%m-%d')
            new_workout = pd.DataFrame({
                'date': [current_date],
                'exercise_name': [exercise_name],
                'duration_minutes': [duration],
                'calories_burned': [calories_burned]
            })
            
            current_workout_log = pd.concat([current_workout_log, new_workout], ignore_index=True)
            save_data(current_workout_log, 'workout_log.csv')
            st.success("Workout logged successfully!")
            st.rerun()
    
    with col2:
        st.subheader("Today's Workouts")
        
        today = datetime.now().strftime('%Y-%m-%d')
        today_workouts = current_workout_log[current_workout_log['date'] == today] if not current_workout_log.empty else pd.DataFrame()
        
        if not today_workouts.empty:
            total_duration = today_workouts['duration_minutes'].sum()
            total_calories = today_workouts['calories_burned'].sum()
            
            col2_1, col2_2 = st.columns(2)
            with col2_1:
                st.metric("Total Duration", f"{total_duration} min")
            with col2_2:
                st.metric("Calories Burned", f"{total_calories}")
            
            st.dataframe(today_workouts[['exercise_name', 'duration_minutes', 'calories_burned']], 
                        use_container_width=True)
        else:
            st.info("No workouts logged today")
        
        # Weekly activity summary
        st.subheader("Weekly Activity Summary")
        week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        week_workouts = current_workout_log[current_workout_log['date'] >= week_ago] if not current_workout_log.empty else pd.DataFrame()
        
        if not week_workouts.empty:
            daily_activity = week_workouts.groupby('date').agg({
                'duration_minutes': 'sum',
                'calories_burned': 'sum'
            }).reset_index()
            
            fig = px.bar(daily_activity, x='date', y='duration_minutes', 
                        title="Daily Workout Duration (Last 7 Days)")
            st.plotly_chart(fig, use_container_width=True)
            
            st.metric("Weekly Total", f"{daily_activity['duration_minutes'].sum()} min", 
                     f"{daily_activity['calories_burned'].sum()} cal burned")
        else:
            st.info("No workouts logged this week")

def dashboard_tab():
    st.header("📊 Personal Assistant Dashboard")
    
    # Load current data
    current_user_profile = load_data('user_profile.csv')
    current_diet_log = load_data('diet_log.csv')
    current_workout_log = load_data('workout_log.csv')
    current_weight_log = load_data('weight_log.csv')
    
    if current_user_profile.empty:
        st.warning("Please complete your profile first to see the dashboard")
        return
    
    current_profile = current_user_profile.iloc[-1]
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Calculate key metrics
    bmi = calculate_bmi(current_profile['weight'], current_profile['height'])
    bmr = calculate_bmr(current_profile['weight'], current_profile['height'], 
                       current_profile['age'], current_profile['gender'])
    tdee = calculate_tdee(bmr, current_profile['activity_level'])
    
    # Today's data
    today_meals = current_diet_log[current_diet_log['date'] == today] if not current_diet_log.empty else pd.DataFrame()
    today_workouts = current_workout_log[current_workout_log['date'] == today] if not current_workout_log.empty else pd.DataFrame()
    
    # Summary cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        calories_consumed = today_meals['calories'].sum() if not today_meals.empty else 0
        st.metric("Calories Consumed", f"{int(calories_consumed)}", f"Target: {int(tdee)}")
    
    with col2:
        calories_burned = today_workouts['calories_burned'].sum() if not today_workouts.empty else 0
        st.metric("Calories Burned", f"{int(calories_burned)}")
    
    with col3:
        net_calories = calories_consumed - calories_burned
        st.metric("Net Calories", f"{int(net_calories)}")
    
    with col4:
        workout_time = today_workouts['duration_minutes'].sum() if not today_workouts.empty else 0
        st.metric("Workout Time", f"{workout_time} min")
    
    # Progress tracking
    st.subheader("Progress Tracking")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Weight progress
        if len(current_weight_log) > 1:
            st.write("**Weight Progress**")
            fig = px.line(current_weight_log, x='date', y='weight', 
                         title="Weight Over Time", markers=True)
            fig.update_layout(xaxis_title="Date", yaxis_title="Weight (kg)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Log more weight data to see progress")
    
    with col2:
        # Calorie balance over time
        if not current_diet_log.empty and not current_workout_log.empty:
            st.write("**Calorie Balance Over Time**")
            
            # Get last 7 days
            week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            recent_diet = current_diet_log[current_diet_log['date'] >= week_ago]
            recent_workouts = current_workout_log[current_workout_log['date'] >= week_ago]
            
            if not recent_diet.empty and not recent_workouts.empty:
                daily_calories = recent_diet.groupby('date')['calories'].sum()
                daily_burned = recent_workouts.groupby('date')['calories_burned'].sum()
                
                # Combine data
                all_dates = set(daily_calories.index) | set(daily_burned.index)
                balance_data = []
                
                for date in sorted(all_dates):
                    consumed = daily_calories.get(date, 0)
                    burned = daily_burned.get(date, 0)
                    balance_data.append({
                        'date': date,
                        'consumed': consumed,
                        'burned': burned,
                        'net': consumed - burned
                    })
                
                balance_df = pd.DataFrame(balance_data)
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=balance_df['date'], y=balance_df['consumed'], 
                                       name='Calories Consumed', line=dict(color='blue')))
                fig.add_trace(go.Scatter(x=balance_df['date'], y=balance_df['burned'], 
                                       name='Calories Burned', line=dict(color='red')))
                fig.add_trace(go.Scatter(x=balance_df['date'], y=balance_df['net'], 
                                       name='Net Calories', line=dict(color='green')))
                
                fig.update_layout(title="Daily Calorie Balance", xaxis_title="Date", yaxis_title="Calories")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Log diet and workout data to see calorie balance")
    
    # Recommendations
    st.subheader("💡 Personalized Recommendations")
    
    # Calorie recommendations
    if calories_consumed > 0:
        if calories_consumed < tdee * 0.8:
            st.warning("⚠️ You're eating too few calories. Consider adding healthy snacks.")
        elif calories_consumed > tdee * 1.2:
            st.warning("⚠️ You're eating too many calories. Consider reducing portion sizes.")
        else:
            st.success("✅ Great job! Your calorie intake is on track.")
    
    # Workout recommendations
    if workout_time == 0:
        st.info("💪 Try to get at least 30 minutes of exercise today!")
    elif workout_time < 30:
        st.info("💪 Good start! Try to reach 30 minutes of exercise.")
    else:
        st.success("🏆 Excellent! You've met your daily exercise goal!")
    
    # BMI recommendations
    if bmi < 18.5:
        st.info("📈 Consider increasing your calorie intake to reach a healthy weight.")
    elif bmi > 25:
        st.info("📉 Focus on a calorie deficit to reach your ideal weight range.")
    else:
        st.success("🎯 Your BMI is in the healthy range! Keep up the good work!")

if __name__ == "__main__":
    main()
