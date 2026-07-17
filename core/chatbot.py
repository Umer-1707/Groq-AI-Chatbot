from api.groq_client import get_response

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def process_query(query):
    chat_history.append({"role": "user", "content": query})

    response = get_response(chat_history)

    chat_history.append({"role": "assistant", "content": response})

    return response