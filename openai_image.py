import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.Image.create(
  prompt="chinese girl,on bed,looking at me",
  n=2,
  size="1024x1024"
)

print(completion)
