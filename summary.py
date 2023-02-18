import os
import openai

##Use your own openai.api_key
openai.api_key = '<openai.api_key>'

default = "Summarize this as short as possible:"
actualText = "Life is full of ups and downs, and we all experience our fair share of challenges and setbacks. Sometimes it can feel like the world is against us, and it can be tempting to give up or lose hope. But it is important to remember that every experience, whether positive or negative, is an opportunity to learn and grow. Each obstacle we face can help us become stronger and more resilient, and each success we achieve can give us the confidence and motivation we need to keep moving forward. It is also important to surround ourselves with people who support us and believe in us, and to seek out the resources and tools we need to overcome our challenges. By staying positive, staying focused on our goals, and never giving up, we can overcome any obstacle and achieve anything we set our minds to. So the next time life throws you a curveball, remember that it is an opportunity to learn, grow, and become the best version of yourself."

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= default + "\n\n" + actualText,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

answer = response["choices"][0]["text"]

print(answer)
print(len(answer) / len(actualText))