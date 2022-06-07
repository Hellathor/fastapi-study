import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    result = {'code':200,'message':'请求成功！'}
    return result

if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)