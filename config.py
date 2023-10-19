apikey = "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"


# responce = {
#   "id": "chatcmpl-7a7pEQBc0os9vSXjjjF0qSTWAG6G8",
#   "object": "chat.completion",
#   "created": 1688844244,
#   "model": "gpt-3.5-turbo-0613",
#   "choices": [
#     {
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": ", and positivity. It is disheartening to work in an environment where my contributions and ideas are consistently dismissed or belittled. As an employee, I deserve to be treated with respect and professionalism, and I believe that everyone on the team should be held to the same standard.\n\nAfter careful consideration and reflection, I have come to the conclusion that it is in my best interest to pursue other opportunities where I can thrive in a healthier and more supportive work environment. I have accepted an offer at another company, where I believe my skills and contributions will be valued and appreciated.\n\nI want to express my gratitude to all my colleagues who have offered me their support, guidance, and friendship throughout my time here. I have learned a lot from working with such talented individuals, and I will always cherish the positive relationships I have formed during my tenure at [Company Name].\n\nIn accordance with company policy, I will ensure a smooth transition of my responsibilities. I am willing to assist with training or any necessary handover documentation to ensure a seamless transfer of my duties. Please let me know how I can be of assistance during this transition period.\n\nI kindly request that my last paycheck, accrued vacation days, and any other necessary paperwork be prepared and provided to me on my last working day. \n\nI"
#       },
#       "finish_reason": "length"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 295,
#     "completion_tokens": 256,
#     "total_tokens": 551
#   }
# }

# print(responce["choices"][0]["message"]["content"])

import random

with open(f"Openai_files/prompt- {random.randint(100,5000)}.txt","w") as f:
        f.write("Hello how are you")   