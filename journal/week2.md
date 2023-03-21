# Week 2 — Distributed Tracing
Week required installation of Honeycomb with Open telemetry
The installation was successful. API keys were successfully exported.

installing packages to instrument a Flask app with open telemetry
pip install opentelemetry-api \
    opentelemetry-sdk \
    opentelemetry-exporter-otlp-proto-http \
    opentelemetry-instrumentation-flask \
    opentelemetry-instrumentation-requests
    
    
    
    
    
    
    
    Data gotten via honeycomb
    ![data](https://user-images.githubusercontent.com/121178341/225679684-5cb49e30-c669-44c0-9bca-1e6e295c00e7.PNG)

##ADDING THE SPAM conf to the home page.
from opentelemetry import trace
tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("http-handler"):
    with tracer.start_as_current_span("my-cool-function"):
![open telemetry spam conf](https://user-images.githubusercontent.com/121178341/225688422-3d572a3d-d64b-41dd-bd55-4bdd55f02207.PNG)

SPAM ACTIVITIES WAS ALSO COLLECTED From the picture below
![spam activites](https://user-images.githubusercontent.com/121178341/225688587-3a6ccf63-f206-4d71-b06e-2cf9fb6f28dc.PNG)

##Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API

At the end of the configuration, Data traces was found from the honeycomb platform where a query was run using the count, API NOW AND Trac ID option
![query from honeycomb](https://user-images.githubusercontent.com/121178341/225694266-9b41a85b-25f0-43f6-aa06-62e73185bbaf.PNG)


##HOMEWORK CHALLENGE
RUN A CUSTOM QUERIES IN HONEYCOMB AND SAVE THEM.

I run a custom query WITH MAX(DURATION_MS) 
WHERE INCLUDES ALL EVENTS
GROUP BY: DURATIONS_MS

Results shown below pieces of data.
![custom](https://user-images.githubusercontent.com/121178341/225706922-2d17cc05-d985-4af3-ab6b-b13a6eb6e161.PNG)


A link of the save custom tracing
https://ui.honeycomb.io/mbonu.mike-gettingstarted/environments/mikebootcamp/datasets/backend-flask/result/bsYm59g65Qf/a/CrZvEfTKUiD/Custom-tracing-from-the-crudddar-project.

After successfully adding the X-Ray file on the app. a group was created successfully.

![X-ray](https://user-images.githubusercontent.com/121178341/226382923-979ef0ee-f602-4e39-8b13-208ba226e4d0.PNG)

During the process of installing X-ray, i encountered a problem with opening the backend and frontend port. i manually run the Npm i TO GET THE frontend running
and i resolved the app.py error following Andrews direction resovlved the backend 
all ports are running
![containers running](https://user-images.githubusercontent.com/121178341/226598193-c44fbc89-c004-475b-b498-a0b7bdf55a9f.PNG)

After a successfully configureing of the frontend and backend with the AWS X-ray. i was able to get logs from the AWS platform
![finally getting trace of the site from AWS](https://user-images.githubusercontent.com/121178341/226599242-104f2c0c-35c2-43ac-a794-c7aa0117d491.PNG)


