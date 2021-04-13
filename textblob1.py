
#!pip install fastapi nest-asyncio pyngrok uvicorn

#pip install python-multipart

from fastapi import FastAPI
#import nest_asyncio
#from pyngrok import ngrok
import uvicorn
from fastapi import FastAPI, Form
from starlette.responses import HTMLResponse
from textblob import TextBlob

def sentiment(text):
  edu = TextBlob(text)
  x = edu.sentiment.polarity
  if x<0:
	  print("Negative sentence ")
  elif x==0:
	  print("Neutral sentence ")
  elif x>0 and x<=1:
	  print("Positive sentence ")
  return x

app = FastAPI()

@app.get('/')
def basic_view():
    return {"WELCOME": "GO TO /docs route, or /post or send post request to /predict "}

@app.get('/predict', response_class=HTMLResponse)
def take_inp():
    return '''<form method="post"> 
    <input type="text" maxlength="50" name="text" placeholder="Text Emotion to be tested"/>  
    <input type="submit"/> 
    </form>'''


@app.post('/predict')
def predict(text:str = Form(...)):
  x = sentiment(text)
  if x<0:
    output="Negative sentence "
  elif x==0:
    output = "Neutral sentence"
  elif x>0 and x <= 1:
    output = "Positive sentence"

  return{      
      "ACTUALL SENTENCE": text,
      "PREDICTED SENTIMENT": output,
      "Probability": x
     
  }

