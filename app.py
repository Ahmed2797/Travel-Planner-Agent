import streamlit as st
from agent import travel_agent

# 1. Page Configuration
st.set_page_config(page_title="AI Travel Architect", page_icon="🏖️", layout="wide")

st.title("🗺️ AI-Powered 'Solid Plan' Travel Architect")
st.markdown("---")

# 2. Sidebar for Inputs
with st.sidebar:
    st.header("Trip Settings")
    destination = st.text_input("Destination", value="Cox's Bazar, Bangladesh")
    budget = st.number_input("Budget ($)", min_value=100, value=300)
    days = st.slider("Number of Days", 1, 10, 5)
    
    generate_btn = st.button("Generate My Solid Plan", type="primary")

# 3. Execution Logic
if generate_btn:
    with st.spinner("Searching for hotels, checking weather, and calculating costs..."):
        # Invoke your agent
        prompt = f"Plan a {days}-day trip to {destination} with a ${budget} budget."
        response = travel_agent.invoke({"messages": [("user", prompt)]})
        plan = response["structured_response"]

    # 4. Top-Level Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Destination", plan.destination)
    col2.metric("Total Budget", f"${plan.total_estimated_budget}")
    col3.metric("Weather Status", plan.weather_status)

    st.markdown("### 📅 Day-by-Day Itinerary")

    # 5. Display Daily Plans in Expanders
    for day in plan.daily_plans:
        with st.expander(f"Day {day.day_number}: {day.tourist_attraction}", expanded=True):
            c1, c2 = st.columns([2, 1])
            
            with c1:
                st.write(f"**🕒 Schedule:** {day.activity_timing}")
                st.write(f"**📍 Spots to Visit:** {', '.join(day.spots)}")
                st.write(f"**🍱 Food Suggestions:** {', '.join(day.local_food_suggestions)}")
                st.write(f"**🍽️ Recommended Restaurant:** {', '.join(day.restaurant_suggestions)}")
            
            with c2:
                st.info(f"**🏨 Hotel:**\n{day.Hotel_suggestion}\n\n**💰 Daily Cost:**\n${day.estimated_daily_cost}")

    st.success("Solid Plan Generated Successfully!")

## streamlit run app.py