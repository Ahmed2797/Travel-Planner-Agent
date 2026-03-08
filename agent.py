import os

from langchain.agents import create_agent
from tools import tools
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from typing import List

load_dotenv()

class DayItinerary(BaseModel):
    day_number: int = Field(description="The sequential day number of the trip")
    Time_of_day: str = Field(description="Specific period: Morning, Afternoon, or Evening")
    activity_timing: str = Field(description="Point 6: Breakdown of time spent in area and local enjoyment")
    tourist_attraction: str = Field(description="Point 2: The primary specific tourist attraction to visit")
    spots: List[str] = Field(description="Point 5: Top 5 specific spots/locations to visit for this day")
    local_food_suggestions: List[str] = Field(description="Point 4: Specific local food items to try")
    restaurant_suggestions: List[str] = Field(description="Point 5: Specific restaurant names to visit")
    Hotel_suggestion: str = Field(description="Point 3: Specific hotel recommendation for the day")
    Hotel_cost: float = Field(description="Point 3 & 7: Estimated cost for the hotel stay in USD/BDT")
    estimated_daily_cost: float = Field(description="Point 7: Total sum of transport, food, and attractions for this day")

class FinalTravelPlan(BaseModel):
    destination: str
    weather_status: str = Field(description="Point 2: Current weather condition and safety advice")
    daily_plans: List[DayItinerary]
    total_estimated_budget: float = Field(description="Point 7: The absolute final solid total cost for the entire trip")


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7,api_key=os.getenv("OPENAI_API_KEY"))



travel_agent = create_agent(
    model=llm,
    tools=tools,
    response_format=FinalTravelPlan,
    system_prompt=(
    "You are a realistic Travel Planner. "
    "IMPORTANT: Daily costs must be realistic and vary day-by-day. "
    "Do not simply divide the total budget by the number of days. "
    "For example, a day with a Safari Park visit should cost more than a day at the beach."

    )
)

# # Assuming 'response' is the output from travel_agent.invoke(...)

# plan = response["structured_response"]

# print(f"==========================================")
# print(f"🗺️ TRIP PLAN TO: {plan.destination.upper()}")
# print(f"🌦️ WEATHER STATUS: {plan.weather_status}")
# print(f"==========================================\n")

# for day in plan.daily_plans:
#     print(f"📅 DAY {day.day_number}: {day.Time_of_day}")
#     print(f"------------------------------------------")
#     print(f"📍 MAIN ATTRACTION: {day.tourist_attraction}")
#     print(f"🏨 HOTEL: {day.Hotel_suggestion} (Cost: ${day.Hotel_cost})")
#     print(f"✨ TOP SPOTS: {', '.join(day.spots)}")
#     print(f"🍱 LOCAL FOOD: {', '.join(day.local_food_suggestions)}")
#     print(f"🍽️ RESTAURANT: {', '.join(day.restaurant_suggestions)}")
#     print(f"🕒 SCHEDULE: {day.activity_timing}")
#     print(f"💰 ESTIMATED DAILY COST: ${day.estimated_daily_cost}")
#     print(f"------------------------------------------\n")

# print(f"✅ TOTAL SOLID BUDGET: ${plan.total_estimated_budget}")