from transformers import pipeline

generator = pipeline("text-generation", model="openai-gpt")

prompt = "Natural Language Processing is"

result = generator(
    prompt,
    max_length=50,
    num_return_sequences=1
)

print("Generated Text:")
print(result[0]["generated_text"])
