# this is a script linked to wolframAPI

import wolframalpha

input = input("Pergunta: ")
app_id = "WPWPJU-AR2K2RGYYU"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)