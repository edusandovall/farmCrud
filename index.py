from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
#React running on ip and port
# client_apps = ['http://localhost:3000'] 

app = FastAPI()

#Registering router
app.include_router(student_router)

# #Register app with cors middleware to allow reource sharing between different domains
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins= client_apps,
#     allow_credentials= True,
#     allow_methods= ["*"],
#     allow_headers= ["*"]
# )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")