import os
import openai
from config import api_key

openai.api_key = api_key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "write a email to my boss for my rejoin "
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
 {
  "id": "chatcmpl-7o3LmphY5tjHlili4UbInMYm5cWRR",
  "object": "chat.completion",
  "created": 1692163634,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Request for Rejoining the Team\n\nDear [Boss's Name],\n\nI hope this email finds you in good health and high spirits. I am writing to express my sincere desire to rejoin the team at [Company Name]. \n\nAs you are aware, I had taken a leave of absence from my position due to [reason]. During this time, I had the opportunity to reflect on my career path and personal goals. I have come to the realization that my true passion lies within the work we do at [Company Name] and the valuable contributions I can make to our team.\n\nI have thoroughly enjoyed my time working with you and the rest of the team, and I truly believe that I can continue to contribute to the success of the company. I have always been dedicated and committed to my work, and I assure you that the current break has only reinforced my enthusiasm for the role.\n\nI would be grateful if you would consider my request for rejoining the team. I understand that there may be certain factors and availability of positions to be taken into account, and I am ready to discuss any necessary adjustments to my responsibilities or work schedule.\n\nPlease let me know if there are any further steps that need to be 
taken in order to start the process of rejoining the team. I"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 22,
    "completion_tokens": 256,
    "total_tokens": 278
  }
}
'''