from openai import OpenAI
import time

client = OpenAI(
    api_key = "", 
)

end = False
systeminput = "You are a code interpreter. Interpret the give code and explain its overall objective. Explain what each part of the code does in 200 words."
while not end:
    userinput = input("Code to be interpreted: \n")
    if not (userinput):
        break
    
    print("Loading...")

    completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": systeminput},
        {"role": "user", "content": userinput}
            ]
        )
    
    print("__________________________________________")
    print("Assistant: \n")
    print(dict(completion.choices[0].message)['content'] + '\n')

    if not input():
        break
