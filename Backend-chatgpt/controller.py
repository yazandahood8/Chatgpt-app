from services import get_answer_from_openai  # Import function to get answer from OpenAI API
from models import QA, db  # Import the QA model and the database session from models

def handle_question(question):
    """
    Handles the logic for processing a question, getting an answer from OpenAI,
    and saving the question and answer to the database.
    
    Args:
        question (str): The user's question.

    Returns:
        dict: A dictionary containing the original question and the generated answer.
    """
    # Call the OpenAI API to get the answer to the question
    answer = get_answer_from_openai(question)
    
    # Create a new QA entry for the question and answer
    new_qa = QA(question=question, answer=answer)
    
    # Add the new entry to the database session
    db.session.add(new_qa)
    
    # Commit the session to save the new entry to the database
    db.session.commit()
    
    # Return the question and answer in a dictionary format
    return {'question': question, 'answer': answer}
