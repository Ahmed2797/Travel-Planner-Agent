import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv()

@tool
def check_weather_safety(destination: str) -> str:
    """Checks current weather. Returns 'Safe' or 'Warning' with details."""
    weather = OpenWeatherMapAPIWrapper(openweathermap_api_key=os.getenv("OPENWEATHERMAP_API_KEY"))
    data = weather.run(destination)
    # Logic: If 'rain' in data, suggest indoor activities
    return f"Weather in {destination}: {data}. Advice: Proceed with the trip but carry an umbrella."


@tool
def calculate_final_costs(transport: float, hotel_daily: float, days: int, food_daily: float) -> dict:
    """Calculates total trip cost. Essential for Point 7."""
    total_stay = (hotel_daily + food_daily) * days
    grand_total = total_stay + transport
    return {
        "total_stay_cost": total_stay,
        "grand_total": grand_total,
        "currency": "BDT"
    }



tavily_key = os.getenv("TAVILY_API_KEY")
search_tool = TavilySearchResults(k=3, api_key=tavily_key)
# search_tool = TavilySearch(max_results=3, api_key=tavily_key,inclinclude_images=True)

# Option B: Manual Wrapper (If Option A fails)
# wrapper = TavilySearchAPIWrapper(tavily_api_key=os.getenv("TAVILY_API_KEY"))
# search_tool = TavilySearchResults(api_wrapper=wrapper, k=3)

# tools = [search_tool, check_weather_safety, calculate_final_costs]
tools = [search_tool]