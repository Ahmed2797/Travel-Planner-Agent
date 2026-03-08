import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_classic.agents import AgentExecutor, create_openai_functions_agent

load_dotenv()



# 1. Configuration (Phase 2)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7,api_key=os.getenv("OPENAI_API_KEY"))
trvily_api_key = os.getenv("TAVILY_API_KEY")

# 2. Tools - The "Travel Planner" logic (Phase 4)
# This allows the AI to search for real flights/hotels
search_tool = TavilySearchResults(k=3, api_key=trvily_api_key) 
tools = [search_tool]

# 3. Itinerary Chain Logic (Phase 3)
# We define a system prompt that guides the AI's behavior
system_prompt = """
You are an expert Travel Planner. 
Your goal is to create a structured, realistic itinerary based on user input.
1. Use the search tool to find current events or hotel recommendations.
2. Provide a day-by-day breakdown.
3. Include estimated costs and travel tips.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 4. Construct the Agent
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5. Execution
def generate_travel_plan(destination, duration, budget):
    user_query = f"Plan a {duration} trip to {destination} with a {budget} budget."
    response = agent_executor.invoke({"input": user_query})
    return response["output"]


# Example Usage:
if __name__ == "__main__":
    plan = generate_travel_plan("Bangladesh", "5 days", "CoxsBazar")
    print("\n--- YOUR TRAVEL PLAN ---")
    print(plan)