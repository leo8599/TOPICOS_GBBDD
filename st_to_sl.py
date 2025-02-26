import streamlit as st
import requests
import json

# --- Slack Webhook URL ---   https://hooks.slack.com/services/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
webhook_url = "https://hooks.slack.com/services/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"

def send_slack_message(message_text):
    """Sends a message to Slack via the webhook, ensuring proper JSON formatting.

    Args:
        message_text: The text of the message to send.

    Returns:
        None
    """
    try:
        # Explicitly create the JSON payload
        message = {
            "text": message_text
        }
        payload = json.dumps(message)  # Convert to JSON string

    except TypeError as e:  # Catch JSON encoding errors
        st.error(f"Error creating JSON payload: {e}.  Make sure your message is valid text.")
        return  # Stop execution if JSON is invalid

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.post(webhook_url, headers=headers, data=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        st.success("Message sent to Slack successfully!")

    except requests.exceptions.RequestException as e:  # Catch any request-related errors
        st.error(f"Error sending message to Slack: {e}")
    except Exception as e: #Catch all the rest of the exceptions
        st.error(f"An error occurred {e}")



# --- Streamlit App ---
st.title("Slack Message Sender")

message_input = st.text_area("Enter your message:", "Hola para todos")

if st.button("Send to Slack"):
    if message_input:
        send_slack_message(message_input)
    else:
        st.warning("Please enter a message to send.")

st.sidebar.header("About")
st.sidebar.markdown("This app sends messages to a Slack channel using a webhook.  It ensures the message is properly formatted as JSON.")