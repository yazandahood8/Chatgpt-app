import openai  # Import OpenAI's library for making API requests
from config import Config  # Import configuration to access the OpenAI API key

def get_answer_from_openai(question):
    """
    Sends the user's question to OpenAI and retrieves the assistant's response.
    
    Parameters:
    question (str): The user's question that needs to be answered by OpenAI.

    Returns:
    str: The answer returned by the OpenAI model.
    
    Raises:
    openai.error.RateLimitError: If the OpenAI API quota is exceeded.
    Exception: For any other errors that occur during API interaction.
    """
    try:
        # Create a response using OpenAI's ChatCompletion API with the GPT-3.5-turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the OpenAI model to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Define the assistant's role
                {"role": "user", "content": question}  # Pass the user's question
            ]
        )
        # Extract the assistant's response (answer) from the API's response data
        answer = response['choices'][0]['message']['content'].strip()
        return answer

    # Handle rate limit errors from the OpenAI API
    except openai.error.RateLimitError as e:
        raise e  # Propagate the rate limit error to be handled in higher layers

    # Handle any other errors during the interaction with the API
    except Exception as e:
        raise Exception('Error fetching data from OpenAI')  # Raise a generic error for debugging
