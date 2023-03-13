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
Postgres and DynamoDB vs Docker installaion

 to install postgres client into gitpod. run the code
  - name: postgres
    init: |
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev

After installing, the port 5430 was opened
![gitpod port](https://user-images.githubusercontent.com/121178341/224736237-06d3ee06-df19-4f25-a252-9f2434e01bbc.PNG)
to install the postgres server, a postgres extensionn was added to the gitpod.connection was successfully made. Authentication was 
also checked and Postgres services was running 
![running postgres](https://user-images.githubusercontent.com/121178341/224741042-9a061caf-6805-492f-a079-c7186fd2fe9d.PNG)



