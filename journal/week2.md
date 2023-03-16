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

At the end of the configuration, Data traces was found from the honeycomb platform where a query was run using the count, API NOW AND Trac ID option
![query from honeycomb](https://user-images.githubusercontent.com/121178341/225694266-9b41a85b-25f0-43f6-aa06-62e73185bbaf.PNG)


