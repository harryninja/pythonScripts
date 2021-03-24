import wolframalpha
import wikipedia

while True:
    input = input("Question: ")
    
    try:
        #wolframalpha
        app_id = "WPWPJU-AR2K2RGYYU"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print(answer)
    except:
        print(wikipedia.summary(input))    
        