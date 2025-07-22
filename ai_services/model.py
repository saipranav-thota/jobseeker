from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_community.llms import HuggingFacePipeline

model_name = "google/gemma-2b"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype="auto")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)
llm = HuggingFacePipeline(pipeline=pipe)

if __name__ == "__main__":
    print(llm)