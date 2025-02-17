from ragas.metrics import faithfulness, answer_relevancy, context_recall, context_precision
from ragas import evaluate
from datasets import Dataset

class Evaluator:
    def evaluate_responses(self, questions, answer, references):
        # Prepare dataset for RAGAS evaluation
        dataset = Dataset.from_dict({
            "question": [questions],
            "answer": [answer],
            "contexts": [[references]],
            "reference": [references],
        })

        # Evaluate using RAGAS metrics
        result = evaluate(
            dataset,
            metrics=[faithfulness, answer_relevancy, context_recall, context_precision],
        )
        
        return result