# Week 1 — App Containerization
Week 1 — Docker and App Containerization

Docker installed
the pip3 requirements installed.
Finally opened the ports

Build container
docker build -t  backend-flask ./backend-flask

setup env variables
done

run another instance of a container 
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask

create another docker file in the frontend
install npm install

build the container in the frontend

Finally built a frontend by running the docker-compose.yml file
which opens the port for the frontend and the backend to communicate

Document notification Endpoint for the OpenAI document.
openAPI was installed successfully via the extension market
![openapi](https://user-images.githubusercontent.com/121178341/224060184-fe438ea2-1dad-43d8-a673-55c8a6f67fc3.PNG)



Postgres and DynamoDB vs Docker installaion
