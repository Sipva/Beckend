from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.presentation.controllers import tarefas_controller


app = FastAPI()

origins = ['http://localhost:5500',
           'http://127.0.0.1:5500',
           ]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

# Rotas e Controllers
app.include_router(tarefas_controller.routes,
                   prefix=tarefas_controller.prefix)