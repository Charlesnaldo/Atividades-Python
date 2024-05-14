import google.generativeai as genai



API_KEY = 'AIzaSyAa4v-itHm-wqx1xAj9XBxk-p3E6THLceo'

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(input("faça uma pergunta"))
print(response.text)