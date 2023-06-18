import os
import time
import torch
import json
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from transformers import AutoTokenizer, LlamaForCausalLM
from flask import Flask, request, jsonify

app = Flask(__name__)
device = "cuda:1"

# Set up Llama model
def load_model(ckpt_dir: str, tokenizer_path: str): 
    
    start_time = time.time()
    generator = LlamaForCausalLM.from_pretrained(ckpt_dir).half()
    generator = generator.to(device)
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    
    print("Model loaded.")
    print(f"Loaded in {time.time() - start_time:.2f} seconds")
    return generator, tokenizer

# Function to generate a response using Llama
def generate_response(
    message, generator, tokenizer, 
    temperature, top_p, max_seq_len, max_batch_size):
    
    with torch.no_grad():
        # Tokenize
        inputs = tokenizer(message, return_tensors="pt")
        # Generate
        inputs = torch.as_tensor(inputs.input_ids, device = torch.device(device))
        generate_ids = generator.generate(inputs, max_length=max_seq_len, temperature=temperature, top_p=top_p)
        response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return response

@app.route('/api/completion', methods=['POST'])
def call_model():
    content = request.json
    message = content["messages"][-1]["content"]

    temperature = float(content.get("temperature", 0.7))
    top_p = float(content.get("top_p", 0.9))
    max_seq_len = int(content.get("max_seq_len", 128))
    max_batch_size = int(content.get("max_batch_size", 32))

    print(max_seq_len)
    
    response = generate_response(message, generator, tokenizer, temperature, top_p, max_seq_len, max_batch_size)
    response = {"choices": [{"message": {"role": "assistant", "content": response}}]}
    return jsonify(response)

if __name__ == "__main__":

    # Load model
    generator, tokenizer = load_model(
        ckpt_dir="/home/guangran/decapoda-research/llama-7b-hf",
        tokenizer_path="/home/guangran/decapoda-research/llama-7b-hf")

    # Start server
    app.run(host='0.0.0.0', port=5331)