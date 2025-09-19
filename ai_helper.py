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
        # Use a reliably available free model
        self.hf_model = os.environ.get("HF_MODEL", st.secrets.get("HF_MODEL", "google/flan-t5-base"))

    def _hf_generate(self, prompt: str, max_new_tokens: int = 200, temperature: float = 0.7) -> str:
        if not self.huggingface_token:
            return "AI not configured. Add HUGGINGFACE_TOKEN to secrets."
        headers = {
            "Authorization": f"Bearer {self.huggingface_token}",
            "Content-Type": "application/json",
        }
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_new_tokens,
                "temperature": temperature,
            },
            "options": {"wait_for_model": True}
        }
        url = f"https://api-inference.huggingface.co/models/{self.hf_model}"
        try:
            resp = requests.post(url, headers=headers, data=json.dumps(payload), timeout=60)
            if resp.status_code == 200:
                data = resp.json()
                # flan-t5 returns a list of dicts with 'generated_text'
                if isinstance(data, list) and data:
                    return data[0].get("generated_text", "") or "(empty response)"
                # some models return dict with 'generated_text'
                if isinstance(data, dict) and "generated_text" in data:
                    return data["generated_text"]
                return "(no text returned)"
            if resp.status_code in (503, 524):
                return "Model is loading. Please try again in a few seconds."
            if resp.status_code == 404:
                return f"Model not found or gated: {self.hf_model}. Try setting HF_MODEL to a public model like 'google/flan-t5-base'."
            return f"AI service error: {resp.status_code}"
        except Exception as e:
            return f"AI request failed: {e}"
    
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
            prompt = (
                "You are a helpful health assistant. Based on the following data, "
                "provide concise, practical insights (3-5 bullet points) covering calories, macros, "
                "activity, and a simple next step.\n\n" + data_summary
            )
            return self._hf_generate(prompt, max_new_tokens=220, temperature=0.6)
    
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
            return self._hf_generate(prompt, max_new_tokens=160, temperature=0.8)
    
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
            return self._hf_generate(prompt, max_new_tokens=200, temperature=0.7)
    
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
            prompt = (
                "Summarize this health progress in 3-5 encouraging bullet points and one next action: "
                + progress_summary
            )
            return self._hf_generate(prompt, max_new_tokens=240, temperature=0.75)
    
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
            return self._hf_generate(prompt, max_new_tokens=120, temperature=0.9)

# Initialize AI helper
health_ai = HealthAI()
