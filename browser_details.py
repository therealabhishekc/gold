from streamlit_js_eval import get_user_agent
from user_agents import parse

def get_browser():
    # Retrieve the user agent
    user_agent_str = get_user_agent()

    # Parse the user agent string
    user_agent = parse(user_agent_str)

    # Extract browser information
    browser_name = user_agent.browser.family

    # return details
    return browser_name