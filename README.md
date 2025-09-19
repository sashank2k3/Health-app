# Personal Health Manager 💪

A comprehensive personal health management app built with Streamlit, designed for tracking diet, exercise, and health progress. Perfect for personal use and mobile access via Streamlit Community Cloud.

## Features

### 👤 User Profile Management
- Input and store personal information (weight, height, age, gender, activity level)
- Automatic BMI calculation and categorization
- Ideal weight range calculation
- BMR (Basal Metabolic Rate) and TDEE (Total Daily Energy Expenditure) calculation
- Weight progress tracking over time

### 🍽️ Diet Management
- Vegetarian-focused food recommendations
- Daily meal logging with nutritional information
- Calorie tracking vs. daily targets
- Weekly diet summaries and trends
- Quick food selection from vegetarian database

### 🏃 Workout Management
- Exercise logging with duration and calories burned
- Workout suggestions and recommendations
- Daily and weekly activity summaries
- Progress visualization

### 📊 Personal Assistant Dashboard
- Comprehensive overview of daily health metrics
- Calorie balance tracking (consumed vs. burned)
- Progress visualization and trend analysis
- Personalized recommendations based on your data
- Goal tracking and achievement monitoring

## Mobile-Friendly Design
- Responsive layout optimized for mobile devices
- Clean, intuitive interface with tabbed navigation
- Touch-friendly controls and inputs

## Installation & Usage

### Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser to `http://localhost:8501`

### Streamlit Community Cloud Deployment

1. **Prepare your repository:**
   - Push your code to GitHub
   - Ensure `requirements.txt` is in the root directory
   - Make sure `app.py` is the main file

2. **Deploy on Streamlit Community Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and branch
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Access your app:**
   - Your app will be available at `https://your-app-name.streamlit.app`
   - Bookmark this URL for easy mobile access

## Data Storage

The app uses CSV files for data persistence:
- `user_profile.csv` - Personal information and profile data
- `weight_log.csv` - Historical weight tracking
- `diet_log.csv` - Meal and nutrition logging
- `workout_log.csv` - Exercise and workout records

## Usage Tips

1. **Start with Profile:** Complete your user profile first to get personalized recommendations
2. **Daily Logging:** Log your meals and workouts daily for accurate tracking
3. **Mobile Access:** Use the Streamlit Community Cloud URL for easy mobile access
4. **Progress Tracking:** Check the Dashboard tab regularly to monitor your progress
5. **Vegetarian Focus:** The app includes a comprehensive vegetarian food database

## Features Overview

### Profile Tab
- Update personal information
- View health metrics (BMI, ideal weight, BMR, TDEE)
- Track weight progress over time

### Diet Tab
- Log daily meals with nutritional information
- Quick selection from vegetarian food database
- View daily and weekly calorie summaries
- Track macro nutrients (protein, carbs, fat)

### Workout Tab
- Log exercises with duration and calories burned
- Access exercise suggestions
- View daily and weekly activity summaries
- Track workout trends

### Dashboard Tab
- Comprehensive health overview
- Calorie balance tracking
- Progress visualization
- Personalized recommendations
- Goal achievement monitoring

## Privacy & Security

- All data is stored locally in CSV files
- No external data sharing or cloud storage
- Personal health data remains private
- Perfect for individual use

## Support

This app is designed for personal use. For questions or issues, refer to the Streamlit documentation or create an issue in your repository.

---

**Happy Health Tracking! 🎯**
