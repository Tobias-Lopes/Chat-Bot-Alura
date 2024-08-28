import google.generativeai as genai
import textwrap

GOOGLE_API_KEY="AIzaSyDpmDss_0U5j34sI5m6fCa-IqLG8mP5rJI"
genai.configure(api_key=GOOGLE_API_KEY)

#Listar os modelos disponíveis

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5, 
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS":  "BLOCK_NONE",
}

#INICIALIZANDO O MODELO

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                               generation_config=generation_config,
                               safety_settings=safety_settings)

response = model.generate_content("Vamos aprender sobre IA. Me dê sugestões")
print(response.text)

chat = model.start_chat(history=[])

prompt = input("Esperando o prompt: ")

while prompt != "fim":
  response = chat.send_message(prompt)
  print("resposta: ", response.text, "\n")
  prompt = input("Esperando o prompt: ")
