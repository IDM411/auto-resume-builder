import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="AIzaSyCwXqoJj5YndqlMn0VgIn6SXW2X4vV1FbA")

print("Available models for your key:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)