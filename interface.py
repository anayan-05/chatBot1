from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def main():
    print("Chatbot ready (flan-t5-large). Type /exit to quit.")

    model_name = "google/flan-t5-large"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        prompt = f"Answer the following question: {user_input}"

        inputs = tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=100,
                do_sample=False,     # Greedy decoding for accuracy
                num_beams=1          # No randomness
            )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
