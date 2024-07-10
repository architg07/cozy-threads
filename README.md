# cozy-threads

## Environment Variables


## Docker compose

`docker compose up --build`

## Manual setup
client terminal:
cd client
npm run build
npm run serve
(starts frontend on 8000)

server terminal:

cd server
python3 -m venv env
source env/bin/activate
pip install Flask==2.2.3 Flask-Cors==3.0.10 (or just install requierments.txt)
flask run --port=5001 --debug  


go to chrome and the app should run on localhost:8000/