from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    
    "http://localhost",
    "http://localhost:8080",
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {'Alfred Nyangau Agwata': {'payment': 810.0,'date': '2023-09-08 13:29:01','transaction_cost': 0.0},
            'FRESH COLD LTD': {'payment': 200.0,'date': '2023-09-08 14:31:29', 'transaction_cost': 0.0},
            'KARISHMA  PATALIA': {'payment': 1045.0,'date': '2023-09-08 15:33:57','transaction_cost': 23.0}}
