import streamlit as st
import ollama

# Configuration

MODEL = "llama3.2:latest"

# Page Configuration

st.set_page_config(
    page_title="AI Smart Travel Planner",
    page_icon="✈️",
    layout="centered"
)

# Title

st.title("✈️ AI-Powered Smart Travel Planner")

st.write(
    "Create a personalized travel itinerary using a local AI model."
)

# User Inputs

destination = st.text_input(
    "📍 Destination",
    placeholder="Example: Hyderabad"
)

days = st.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=15,
    value=3
)

budget = st.number_input(
    "💰 Total Budget (₹)",
    min_value=1000,
    max_value=1000000,
    value=10000,
    step=1000
)

travelers = st.number_input(
    "👥 Number of Travelers",
    min_value=1,
    max_value=20,
    value=2
)

preference = st.selectbox(
    "🎯 Travel Preference",
    [
        "General",
        "Historical",
        "Adventure",
        "Nature",
        "Food",
        "Shopping",
        "Relaxation"
    ]
)

travel_style = st.selectbox(
    "🧳 Travel Style",
    [
        "Budget",
        "Balanced",
        "Comfortable"
    ]
)

# Generate Travel Plan

if st.button("✈️ Generate Travel Plan"):

    if not destination.strip():

        st.warning("Please enter a destination.")

    else:
        # Prompt for AI

        prompt = f"""
You are an AI-powered smart travel planner.

Create a practical {days}-day travel itinerary
for {destination}.

Travel details:
- Number of travelers: {travelers}
- Total budget: ₹{budget}
- Travel preference: {preference}
- Travel style: {travel_style}

Create a clear and easy-to-follow travel plan.

For each day include:

1. Morning activities
2. Afternoon activities
3. Evening activities
4. Food suggestions
5. Approximate spending

Also include:

- Important travel tips
- Suggested local food
- Places that match the travel preference
- A simple estimated budget breakdown

Important:
- Keep the plan suitable for the given budget.
- Do not invent flight or hotel booking confirmations.
- Clearly mention that prices are approximate.
- Use simple language.
"""

        # Show Loading Message

        with st.spinner("🤖 AI is creating your travel plan..."):

            try:

                response = ollama.chat(
                    model=MODEL,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                travel_plan = response["message"]["content"]

                # Display Result

                st.success("Travel plan generated successfully!")

                st.subheader("🗺️ Your Personalized Travel Plan")

                st.markdown(travel_plan)

            except Exception as e:

                st.error(
                    "Unable to connect to Ollama. "
                    "Please check that Ollama is installed "
                    "and the selected model is available."
                )

                st.code(str(e))