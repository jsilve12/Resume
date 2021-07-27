""" Core Website Pages """
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os


app = APIRouter()
templates = Jinja2Templates(directory='Resume/templates')


@app.get('/', response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/cards/development')
async def development(request: Request):
    return {
        'Title': 'Development',
        'Cards': [
            {
                'Title': 'Fullstack Web Development',
                'Subtitle': '3 years',
                'Body': '''Experience constructing backends in FastAPI, Flask, PHP, and NodeJS, integrated with Postgres, redis, and MySQL.
                        Understanding of principles of frontend web development and practice building them with React, Angular, Bootstrap, and Material UI.'''
            },
            {
                'Title': 'Machine Learning',
                'Subtitle': '2 years',
                'Body': '''Familiarity with the strength and weakenesses of neural networks, decision trees/forests, clustering methods, and regressions.
                        Practical working knowledge of building ETL, ML, or NLP pipelines in Python or R.'''
            },
            {
                'Title': 'Devops',
                'Subtitle': '2 years',
                'Body': '''Managing production websites using a kubernetes cluster, CI/CD pipelines, with unit and integration tests.
                        AWS Certified Solutions Architect (Associate), with experience using a wide range of services in AWS and GCP.'''
            }
        ]
    }


@app.get('/cards/education')
async def education(request: Request):
    return {
        'Title': 'Education',
        'Cards': [
            {
                'Title': 'University of Michigan',
                'Subtitle': 'September 2017 - December 2019',
                'Body': 'Graduated Magna Cum Laude with a BSE, in Data Science.'
            },
            {
                'Title': 'Ben Gurion University',
                'Subtitle': 'July 2019 - August 2019',
                'Body': 'Studied Cyber Security and Machine Learning.'
            }
        ]
    }


@app.get('/cards/projects')
async def projects(request: Request):
    return {
        'Title': 'Projects',
        'Cards': [
            {
                'Title': 'University of Michigan Chess Website',
                'Subtitle': 'http://umich.chess.jonathansilverstein.us',
                'Body': 'Built and maintained the website for the chess club at the University of Michigan using FastAPI, React and Bootstrap, on top of a kubernetes cluster.'
            },
            {
                'Title': 'Chess Endgame Trainer',
                'Subtitle': 'http://endgame.chess.jonathansilverstein.us',
                'Body': 'Built and maintained a website for training endgame play in chess.'
            }
        ]
    }


@app.get('/cards/work')
async def work(request: Request):
    return {
        'Title': 'Work',
        'Cards': [
            {
                'Title': 'ISS (formerly owned by FICO)',
                'Subtitle': 'January 2020 - Present',
                'Body': 'Constructed the API for client data access as well as a CI/CD pipeline and a number of daemons to support it. Worked to expand and debug critical ETL pipelines.'
            },
            {
                'Title': 'Academix.Bio',
                'Subtitle': 'May 2019 - July 2019',
                'Body': 'Implemented a number of natural language processing pipelines, most notably a similar keyword suggestion, with search engine capabilities.'
            },
            {
                'Title': 'United State District Court IT',
                'Subtitle': 'May 2018 - August 2018',
                'Body': 'Gained valuable time management skills through balancing website upgrades with technology repairs. Assisted with existing equipment catalogues as well as the mass rollout of new equipment.'
            },
        ]
    }
