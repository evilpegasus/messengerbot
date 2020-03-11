import json

with open('message.json') as f:
  messages = json.load(f)

print(json.dumps(messages, indent = 4, sort_keys = True))