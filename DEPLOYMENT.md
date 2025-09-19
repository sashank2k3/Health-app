# Deployment Guide for Personal Health Manager

## Quick Start

### Local Testing
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
3. Open your browser to `http://localhost:8501`

### Streamlit Community Cloud Deployment

#### Step 1: Prepare Your Repository
1. Create a new repository on GitHub
2. Upload all files (`app.py`, `requirements.txt`, `README.md`)
3. Make sure the main file is named `app.py`

#### Step 2: Deploy on Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and branch (usually `main`)
5. Set the main file path to `app.py`
6. Click "Deploy"

#### Step 3: Access Your App
- Your app will be available at `https://your-app-name.streamlit.app`
- Bookmark this URL for easy mobile access
- The app will automatically update when you push changes to GitHub

## Mobile Access Tips

1. **Bookmark the URL** on your mobile browser for quick access
2. **Add to Home Screen** (iOS/Android) for app-like experience
3. **Use in Landscape Mode** for better viewing of charts and data
4. **Enable Notifications** if you want to be reminded to log meals/workouts

## Data Persistence

- All data is stored locally in CSV files
- Data persists between sessions
- No external database required
- Perfect for personal use

## Troubleshooting

### Common Issues:
1. **App won't start**: Check that all dependencies are installed
2. **Data not saving**: Ensure the app has write permissions in the directory
3. **Mobile layout issues**: Try refreshing the page or clearing browser cache

### Support:
- Check the Streamlit documentation for technical issues
- The app is designed to work offline once loaded
- All data remains private and local to your device

## Features Overview

✅ **Profile Management** - BMI, ideal weight, BMR/TDEE calculations
✅ **Diet Tracking** - Vegetarian food database, calorie counting
✅ **Workout Logging** - Exercise tracking, calorie burn estimation
✅ **Progress Dashboard** - Visual charts, goal tracking, recommendations
✅ **Mobile Optimized** - Responsive design for mobile devices

---

**Your personal health journey starts here! 🎯**
