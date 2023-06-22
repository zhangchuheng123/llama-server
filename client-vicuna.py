import openai
openai.api_key = "EMPTY" # Not support yet
openai.api_base = "http://localhost:8000/v1"


with open('full_message.txt', 'r') as f:
   full_message = f.read()

with open('short_message.txt', 'r') as f:
   short_message = f.read()

model = "vicuna-7b-v1.3"
prompt = short_message

# create a completion
completion = openai.Completion.create(model=model, prompt=prompt, max_tokens=200)
# print the completion
print(prompt + completion.choices[0].text)

# # create a chat completion
# completion = openai.ChatCompletion.create(
#   model=model,
#   messages=[{"role": "user", "content": "Hello! What is your name?"}]
# )
# # print the completion
# print(completion.choices[0].message.content)

