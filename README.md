# Travel-Planner-Agent

The Solid Plan Travel Architect is an autonomous AI agent designed to solve the "fragmented planning" problem. Unlike traditional travel apps that provide static lists, this system uses an Agentic Workflow to check real-time weather, calculate precise budgets using Python logic, and generate structured, machine-readable itineraries.

🗺️ AI Travel Architect: The "Solid Plan" Planner

An autonomous AI agent that generates structured, cost-validated, and weather-aware travel itineraries. Unlike standard LLM prompts, this system uses agentic reasoning to browse the live web, check real-time weather, and execute Python logic for precise budget calculations.
🌟 Key Features

    7-Point Reasoning Logic: Every plan includes a Weather Safety Check, Top 5 Spots, Timing Breakdowns, Local Food suggestions, Hotel recommendations, and granular Costing.

    Deterministic Budgeting: Uses a custom Python tool for math to prevent LLM "hallucinations" in total cost calculations.

    Weather Gate: Validates the destination's weather before finalizing activities.

    Structured Output: Powered by Pydantic V2 to ensure data is always returned in a valid format for the Streamlit UI.

    Bangladesh-Centric: Optimized for travel within Bangladesh (Dhaka, Cox's Bazar, Sylhet, etc.), including local transportation insights.

🛠️ Tech Stack

    Core: LangChain 1.0.1 (Agentic Framework)

    Brain: OpenAI GPT-4o-mini

    Search: Tavily AI (Real-time web access)

    Weather: WeatherAPI.com / OpenWeatherMap

    UI: Streamlit

⚙️ Installation & Setup

    Clone the repository:
    Bash

    git clone https://github.com/Ahmed2797/Travel-Planner-Agent

    Install dependencies:
    Bash

    pip install -r requirements.txt

    Configure Environment Variables:
    Create a .env file in the root directory and add your API keys:
    Code snippet

    OPENAI_API_KEY=sk-your-key
    TAVILY_API_KEY=tvly-your-key
    WEATHERAPI_KEY=your-key

    Run the Application:
    Bash

    streamlit run app.py

🏗️ Project Structure
Plaintext

    ├── app.py              # Streamlit Frontend UI
    ├── agent.py            # LangChain Agent Definition & Logic
    ├── tools.py            # Custom Python Tools (Weather, Math, Search)
    ├── schema.py           # Pydantic Models for Structured Output
    ├── .env                # API Keys (Git ignored)
    └── requirements.txt    # Project Dependencies

📊 Logic Flow

    Input: User provides destination, budget, and duration.

    Analysis: The Agent calls check_weather_safety to verify the location.

    Execution: The Agent searches for top-rated hotels and spots via TavilySearchResults.

    Validation: All costs are passed through calculate_final_costs for accuracy.

    Formatting: The LLM maps the data to the FinalTravelPlan Pydantic class.

    Delivery: Streamlit renders the data into an interactive dashboard.
    