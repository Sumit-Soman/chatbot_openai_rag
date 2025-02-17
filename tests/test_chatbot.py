import pytest
import json
from chatbot.chatbot_init import Chatbot
from chatbot.chatbot_evaluator import Evaluator

# Fixture to initialize the chatbot and evaluator
@pytest.fixture
def setup_chatbot():
    chatbot = Chatbot()
    evaluator = Evaluator()
    return chatbot, evaluator



def load_test_cases(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


@pytest.mark.parametrize("test_case", load_test_cases(file_path="tests/test_data.json"))
def test_ragas_evaluation(setup_chatbot, test_case, request):
    chatbot, evaluator = setup_chatbot
    
    question = test_case['question'];
    # Initialize results storage
    evaluation_results = []

    # Iterate through each question and generate response
    response, context = chatbot.generate_response(question)  # Generate response for the question
    reference = test_case['reference']  # Get the corresponding reference answer

    # Evaluate response
    evaluation_result = evaluator.evaluate_responses(question, response, context)

    print(evaluation_result)
    # Validate thresholds
    assert evaluation_result["faithfulness"][0] > 0.9, f"Faithfulness score too low: {evaluation_result['faithfulness']}"
    assert evaluation_result["answer_relevancy"][0] > 0.9, f"Answer Relevance score too low: {evaluation_result['answer_relevancy']}"
    assert evaluation_result["context_precision"][0] > 0.8, f"Context Precision score too low: {evaluation_result['context_precision']}"
    assert evaluation_result["context_recall"][0] > 0.8, f"Context Recall score too low: {evaluation_result['context_recall']}"