import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Initializing FastAPI app
app = FastAPI()

api_key = "Your API key here"
openai.api_key = api_key

# request model
class ChatRequest(BaseModel):
    user_input: str

# response model
class ChatResponse(BaseModel):
    bot_reply: str

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# chatbot endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat_handler(request: ChatRequest):
    try:
        # Generate chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {
                    "role": "user",
                    "content": request.user_input
                }
            ]
        )
        bot_reply = response.choices[0].message["content"]
        return {"bot_reply": bot_reply}
    except Exception as e:
        # Handling exceptions
        error_msg = f"Error generating chat completion: {e}"
        print(error_msg)
        raise HTTPException(status_code=500, detail="Error processing request.")

# Running the app with uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
