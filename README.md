# Getting Unstuck Curriculum Site

This repository contains sources for the Getting Unstuck curriculum site. 

See the included Dockerfile for exact setup requirements. But generally speaking, 
the following tools must be installed on the development host: 
* python 3
* pip
* npm 
* dart sass compiler 

The following steps are required on a development host after checking out the repository: 
1. Run 'npm install' (initializes any node.js packages, i.e., Bootstrap).
1. Run make (performs any compilation steps required after code changes, i.e., sass files).
1. Create python virtual environment (e.g., 'python3 -m venv venv'). 
1. Switch into virtual environment (e.g., 'source venv/bin/activate')
1. Install pip requirements ('pip install -r requirements.txt').
1. Change into app directory. 
1. Launch gunicorn (gunicorn --bind 0.0.0.0:8080 wsgi:app)
