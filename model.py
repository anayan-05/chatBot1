from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def load_model():
    print("Loading flan-t5-small...")
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    print("Model loaded.")
    return model, tokenizer
