from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

app = FastAPI()

@app.get("/quiz_results")
async def quiz_results(min_weight: int, max_weight: int, shedding: int, barking: int, energy: int, protectiveness: int, trainability: int):
  params = {'min_weight': min_weight, 'max_weight': max_weight, 'shedding': shedding, 'barking': barking, 'energy': energy, 'protectiveness': protectiveness, 'trainability': trainability}
  breed = requests.get('https://api.api-ninjas.com/v1/dogs', params = params, headers = {"X-Api-Key": os.getenv("X-Api-Key")})
  results = breed.json()
  new_array = []
  if results:
    for dog in results:
      new_array.append({"name": dog["name"], "url": dog["image_link"]})
    return new_array
  else:
    return "You should get a cat"
  
