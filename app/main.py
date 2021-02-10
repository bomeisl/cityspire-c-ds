#app/main.py



#Imports

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz
from app.api import locations, location


#Edit your app's title and description. See [https://fastapi.tiangolo.com/tutorial/metadata/](https://fastapi.tiangolo.com/tutorial/metadata/)

description = """
To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
"""

# App

app = FastAPI(
    title='cityspire-c-ds API',
    description=description,
    docs_url='/',
)


# Include routers

app.include_router(db.router, tags=['Database'])
app.include_router(ml.router, tags=['Machine Learning'])
app.include_router(viz.router, tags=['Visualization'])

app.include_router(locations.router, tags=['Locations'])
app.include_router(location.router, tags =['Data by Location'])


# Add CORSMiddleware for interoperability

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# For running the app with uvicorn, "if name = main"

if __name__ == '__main__':
    uvicorn.run(app)
    # Use this command in CLI to run on different port locally: uvicorn app.main:app --reload --port 8080
