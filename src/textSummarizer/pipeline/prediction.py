import os
from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text: str) -> str:
        if not text or not text.strip():
            return "Please enter text to summarize."

        # Check if local trained model exists; fallback to pre-trained model if not trained yet
        if os.path.exists(self.config.model_path) and os.path.exists(self.config.tokenizer_path):
            model_name = self.config.model_path
            tokenizer_name = self.config.tokenizer_path
        else:
            model_name = "sshleifer/distilbart-cnn-12-6"
            tokenizer_name = "sshleifer/distilbart-cnn-12-6"

        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

        input_length = len(inputs["input_ids"][0])
        max_len = max(10, min(128, int(input_length * 0.8)))
        min_len = max(5, min(max_len - 1, 10))

        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=max_len,
            min_length=min_len,
            length_penalty=1.0,
            num_beams=2,
            early_stopping=True
        )

        output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return output
