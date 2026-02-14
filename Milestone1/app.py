import streamlit as st
import random

st.set_page_config(
    page_title="FitPlan AI",
    page_icon="🏋️‍♂️",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    font-family: 'Segoe UI', sans-serif;
}
.main-container {
    background: none;  /* Remove rectangle */
    padding: 40px;
    border-radius: 0px;
    backdrop-filter: none;
    box-shadow: none;
    margin-top: 0px;
}
.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 10px;
    color: #ffd166;
}
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #ffd166, #ff9f1c);
    color: #1f1c2c;
    font-weight: 700;
    padding: 14px;
    border-radius: 12px;
    border: none;
    transition: 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)


st.markdown("<h1 style='text-align:center; color:white;'>🏋️‍♂️ FitPlan AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>Personalized Fitness Plan Generator</p>", unsafe_allow_html=True)

# 👤 PROFILE
st.markdown('<div class="section-title">👤 Personal Profile</div>', unsafe_allow_html=True)
name = st.text_input("Full Name")
age = st.number_input("Age", min_value=10, max_value=80, step=1)
height_cm = st.number_input("Height (cm)", min_value=0.0, step=0.1)
weight_kg = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

# 🎯 GOAL
st.markdown('<div class="section-title">🎯 Fitness Objective</div>', unsafe_allow_html=True)
goal = st.selectbox(
    "Choose your main goal",
    ["Fat Loss", "Muscle Gain", "Strength Boost", "General Fitness", "Core Definition"]
)

# 📊 FITNESS LEVEL
st.markdown('<div class="section-title">📊 Fitness Level</div>', unsafe_allow_html=True)
fitness_level = st.radio(
    "",
    ["Beginner", "Intermediate", "Advanced"],
    horizontal=True
)

# 🔧 Available Equipment
st.markdown('<div class="section-title">Available Equipment</div>', unsafe_allow_html=True)
equipment = st.multiselect(
    "Select equipment you have",
    [
        "Dumbbells",
        "Barbell",
        "Resistance Bands",
        "Treadmill",
        "Skipping Rope",
        "Pull-up Bar",
        "Yoga Mat",
        "None"
    ]
)

# 🚀 Generate Personalised Plan
generate = st.button("🚀 Generate Personalised Plan")

# =====================================================
# GENERATE SECTION
# =====================================================
if generate:

    if not name.strip():
        st.error("Please enter your name.")
    elif height_cm <= 0 or weight_kg <= 0:
        st.error("Height and weight must be valid.")
    elif not equipment:
        st.error("Select at least one equipment option.")
    else:
        height_m = height_cm / 100
        bmi = round(weight_kg / (height_m ** 2), 2)

        # BMI Category & Advice
        if bmi < 18.5:
            category = "Underweight"
            advice = "Focus on strength training and calorie surplus."
            motivations = [
                "Every step forward counts, keep going!",
                "Fuel your body and build strength daily!",
                "Small gains today lead to big results tomorrow!",
                "Consistency is your superpower!",
                "Your journey to a stronger self starts now!"
            ]
        elif 18.5 <= bmi < 24.9:
            category = "Healthy"
            advice = "Maintain balance of cardio and resistance training."
            motivations = [
                "Stay consistent, your health is your wealth!",
                "Challenge yourself to become even stronger!",
                "Healthy habits build a lifetime of results!",
                "Push a little further every day!",
                "Celebrate progress, not perfection!"
            ]
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            advice = "Combine calorie control with consistent cardio."
            motivations = [
                "You are capable of more than you know!",
                "Every workout is a step closer to your goal!",
                "Small changes make a big difference!",
                "Keep moving, results will follow!",
                "Dedication today leads to transformation tomorrow!"
            ]
        else:
            category = "Obese"
            advice = "Start with low-impact cardio and progressive training."
            motivations = [
                "Your journey starts now, take the first step!",
                "One day at a time, one workout at a time!",
                "Believe in yourself and keep pushing forward!",
                "Every effort counts, stay committed!",
                "Progress is progress, no matter how small!"
            ]

        # Water Recommendation
        water = round(weight_kg * 0.033, 2)

        # Workout Suggestion
        if goal == "Fat Loss":
            workout = "4–5 days cardio + 3 days resistance training"
        elif goal == "Muscle Gain":
            workout = "5–6 days split training (Push/Pull/Legs)"
        elif goal == "Strength Boost":
            workout = "4 days compound lifting (Squat, Bench, Deadlift)"
        elif goal == "Core Definition":
            workout = "3 days core + 3 days HIIT"
        else:
            workout = "3–4 balanced training days weekly"

        # Select random motivation
        motivation_msg = random.choice(motivations)

        st.success("Your Personalised Fitness Plan is Ready!")

        # Main heading
        st.markdown(
            "<h1 style='text-align:center; margin-top:25px; color:white;'>Your Fitness Summary</h1>",
            unsafe_allow_html=True
        )

        # Display summary
        st.markdown(f"""
        <div style="margin-top:25px; padding:30px; border-radius:20px; 
        background: rgba(255,255,255,0.12); box-shadow:0 10px 30px rgba(0,0,0,0.3);">
        <h3>📊 Body Analysis</h3>
        <p><b>Name:</b> {name}</p>
        <p><b>BMI:</b> {bmi}</p>
        <p><b>Category:</b> {category}</p>
        <p><b>Insight:</b> {advice}</p>
        <hr>
        <h3>🏋️ Training Recommendation</h3>
        <p><b>Suggested Split:</b> {workout}</p>
        <p><b>Fitness Level:</b> {fitness_level}</p>
        <hr>
        <h3>🥗 Nutrition Direction</h3>
        <p>✔ Protein: {round(weight_kg * 1.6)}g – {round(weight_kg * 2)}g daily</p>
        <p>✔ Balanced carbs & healthy fats</p>
        <p>✔ Avoid processed sugar</p>
        <hr>
        <h3>💬 Motivation</h3>
        <p>{motivation_msg}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
