#import Ollama
# modelp = "C:/Users/Ramu/Deskto/project_1/mixtral_8x7b.bin"
# from ollama import Client
# client = ollama.Client(model=modelp)
# def generate_response(prompt):
#     response = Client.generate(prompt=prompt, stream=True)
#     output = ""
#     for chunk in response:
#         if chunk["choices"][0]["delta"].get("content"):
#             output += chunk["choices"][0]["delta"]["content"]
#             print(output, end="", flush=True)
#             time.sleep(0.01) 
#     return output
# while True:
#     user_input = input("\nYou: ")
#     if user_input.lower() == "exit":
#         break

#     print("Mistral:")
#     response = generate_response(user_input)
#     print("\n")
