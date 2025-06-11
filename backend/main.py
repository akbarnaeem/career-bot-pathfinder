
from fastapi import FastAPI
from pydantic import BaseModel
from model_inference import predict_interests
from database import get_career_suggestions

app = FastAPI()

class QuizInput(BaseModel):
    q1: int
    q2: int
    q3: int
    q4: int
    q5: int

class InterestInput(BaseModel):
    interest: str

@app.post("/predict")
def predict_quiz(quiz: QuizInput):
    interests = predict_interests(quiz.dict())
    suggestions = get_career_suggestions(interests)
    return {"predicted_domains": interests, "suggestions": suggestions}

@app.post("/suggest")
def suggest_interest(user: InterestInput):
    suggestions = get_career_suggestions([user.interest])
    return {"suggestions": suggestions}
