import socket
import os
import time
import torch
import argparse
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from transformers import AutoTokenizer, LlamaForCausalLM

# Set up Llama model
def load_model(ckpt_dir: str, tokenizer_path: str): 
    
    start_time = time.time()
    generator = LlamaForCausalLM.from_pretrained(ckpt_dir).half()
    generator = generator.to("cuda:1")
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    
    print("Model loaded.")
    print(f"Loaded in {time.time() - start_time:.2f} seconds")
    return generator, tokenizer

# Function to generate a response using Llama
def generate_response(message,
                      generator, 
                      tokenizer,                      
                      temperature: float = 0.8,
                      top_p: float = 0.95,
                      max_seq_len: int = 128,
                      max_batch_size: int = 32
                      ):
    
    with torch.no_grad():
        # tokenize
        inputs = tokenizer(message, return_tensors="pt")
        # Generate
        inputs = torch.as_tensor(inputs.input_ids, device = torch.device('cuda:1'))
        generate_ids = generator.generate(inputs, max_length=max_seq_len, temperature=temperature, top_p = top_p)
        response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return response


if __name__ == "__main__":
    # load model
    generator, tokenizer = load_model(
        ckpt_dir="/home/guangran/decapoda-research/llama-7b-hf",
        tokenizer_path="/home/guangran/decapoda-research/llama-7b-hf")
    
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(1)
    print("Server started. Listening for connections...")
    
    # Accept new connections and handle them
    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address}")

    # Receive messages from the client and generate responses
    while True:
        message = client_socket.recv(1024).decode().strip()
        print("Received message:", message)

        # Check for termination command
        if message.lower() == "exit":
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}")

        # Generate a response using Llama
        response = generate_response(message,
                                     generator,
                                     tokenizer
                                     )
        print("Generated response:", response)

        # Send the response back to the client
        client_socket.sendall(response.encode())

    # Clean up
    client_socket.close()
    server_socket.close()
