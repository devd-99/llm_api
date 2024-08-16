from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3.1:8b", base_url="http://192.168.65.254:11434",request_timeout=60.0)

response = llm.complete("What is the capital of France?")
print(response)