import requests
import json
import streamlit as st
from typing import Optional, Dict, Any, List
import os

class HealthAI:
    """AI helper for health management app using free APIs"""
    
    def __init__(self):
        self.huggingface_token = st.secrets.get("HUGGINGFACE_TOKEN", os.environ.get("HUGGINGFACE_TOKEN"))
        self.openai_key = st.secrets.get("OPENAI_API_KEY", os.environ.get("OPENAI_API_KEY"))
        self.groq_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY"))
    
    def get_health_insights(self, user_data: Dict[str, Any]) -> str:
        """Get personalized health insights using Hugging Face"""
        if not self.huggingface_token:
            return "AI insights not available. Please configure Hugging Face token."
        
        try:
            # Prepare user data summary
            data_summary = f"""
            User Profile:
            - Weight: {user_data.get('weight', 'N/A')} kg
            - Height: {user_data.get('height', 'N/A')} cm
            - Age: {user_data.get('age', 'N/A')} years
            - Gender: {user_data.get('gender', 'N/A')}
            - Activity Level: {user_data.get('activity_level', 'N/A')}
            - BMI: {user_data.get('bmi', 'N/A')}
            - Daily Calories: {user_data.get('daily_calories', 'N/A')}
            - Workout Time: {user_data.get('workout_time', 'N/A')} minutes
            """
            
            # Use Hugging Face Inference API
            headers = {"Authorization": f"Bearer {self.huggingface_token}"}
            payload = {
                "inputs": f"Analyze this health data and provide personalized insights: {data_summary}",
                "parameters": {"max_length": 200, "temperature": 0.7}
            }
            
            response = requests.post(
                "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'AI analysis completed.')
                return "Health insights generated successfully."
            else:
                return f"AI service temporarily unavailable. Status: {response.status_code}"
                
        except Exception as e:
            return f"AI analysis error: {str(e)}"
    
    def get_meal_recommendations(self, user_profile: Dict[str, Any], meal_type: str) -> str:
        """Get AI-powered meal recommendations"""
        if not self.huggingface_token:
            return "AI recommendations not available. Please configure Hugging Face token."
        
        try:
            prompt = f"""
            Suggest a healthy {meal_type} for a {user_profile.get('age', 'adult')} year old {user_profile.get('gender', 'person')} 
            who is {user_profile.get('activity_level', 'moderately active')}. 
            Weight: {user_profile.get('weight', 'N/A')} kg, Height: {user_profile.get('height', 'N/A')} cm.
            Focus on vegetarian options with balanced nutrition.
            """
            
            headers = {"Authorization": f"Bearer {self.huggingface_token}"}
            payload = {
                "inputs": prompt,
                "parameters": {"max_length": 150, "temperature": 0.8}
            }
            
            response = requests.post(
                "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'Meal recommendations generated.')
                return "AI meal recommendations ready."
            else:
                return f"AI service unavailable. Status: {response.status_code}"
                
        except Exception as e:
            return f"AI recommendation error: {str(e)}"
    
    def get_workout_suggestions(self, user_profile: Dict[str, Any], available_time: int) -> str:
        """Get AI-powered workout suggestions"""
        if not self.huggingface_token:
            return "AI workout suggestions not available. Please configure Hugging Face token."
        
        try:
            prompt = f"""
            Suggest a {available_time}-minute workout for a {user_profile.get('age', 'adult')} year old 
            {user_profile.get('gender', 'person')} who is {user_profile.get('activity_level', 'moderately active')}.
            Weight: {user_profile.get('weight', 'N/A')} kg, Height: {user_profile.get('height', 'N/A')} cm.
            Include exercises that can be done at home or gym.
            """
            
            headers = {"Authorization": f"Bearer {self.huggingface_token}"}
            payload = {
                "inputs": prompt,
                "parameters": {"max_length": 200, "temperature": 0.7}
            }
            
            response = requests.post(
                "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'Workout suggestions generated.')
                return "AI workout suggestions ready."
            else:
                return f"AI service unavailable. Status: {response.status_code}"
                
        except Exception as e:
            return f"AI workout error: {str(e)}"
    
    def analyze_progress(self, weight_history: List[Dict], diet_history: List[Dict], workout_history: List[Dict]) -> str:
        """Analyze user's health progress using AI"""
        if not self.huggingface_token:
            return "AI progress analysis not available. Please configure Hugging Face token."
        
        try:
            # Prepare progress summary
            progress_summary = f"""
            Health Progress Analysis:
            - Weight entries: {len(weight_history)}
            - Diet entries: {len(diet_history)}
            - Workout entries: {len(workout_history)}
            - Recent weight trend: {'Improving' if len(weight_history) > 1 else 'Starting journey'}
            - Activity consistency: {'Good' if len(workout_history) > 3 else 'Needs improvement'}
            """
            
            headers = {"Authorization": f"Bearer {self.huggingface_token}"}
            payload = {
                "inputs": f"Analyze this health progress data and provide motivational insights: {progress_summary}",
                "parameters": {"max_length": 250, "temperature": 0.8}
            }
            
            response = requests.post(
                "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'Progress analysis completed.')
                return "AI progress analysis ready."
            else:
                return f"AI service unavailable. Status: {response.status_code}"
                
        except Exception as e:
            return f"AI analysis error: {str(e)}"
    
    def get_motivational_message(self, user_goals: str, recent_activity: str) -> str:
        """Get AI-powered motivational messages"""
        if not self.huggingface_token:
            return "AI motivation not available. Please configure Hugging Face token."
        
        try:
            prompt = f"""
            Provide a motivational health message for someone with goals: {user_goals}
            Recent activity: {recent_activity}
            Make it encouraging and specific to their health journey.
            """
            
            headers = {"Authorization": f"Bearer {self.huggingface_token}"}
            payload = {
                "inputs": prompt,
                "parameters": {"max_length": 100, "temperature": 0.9}
            }
            
            response = requests.post(
                "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'Motivational message generated.')
                return "AI motivation ready."
            else:
                return f"AI service unavailable. Status: {response.status_code}"
                
        except Exception as e:
            return f"AI motivation error: {str(e)}"

# Initialize AI helper
health_ai = HealthAI()
