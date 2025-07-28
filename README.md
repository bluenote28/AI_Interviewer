AI Interviewer

This is my entry to the boot.dev hackathon

This is a Python Flask application that uses Google Gemini to simulate a job interview.

Right now the app can only be run locally. I wanted to get this hosted but ran out of time before the hackathon deadline.

The easiest way to install is to use docker. Docker install: https://www.docker.com/products/docker-desktop/

After docker is installed run "docker pull bluenote28/ai-interview:v1.0"

You will need to get a Gemini API key at https://aistudio.google.com

Once the API key is obtained run "docker run -e GEMINI_API_KEY=<your-api-key> -p 5001:5001 ai-interview:v1.0"

Open a web browser and go to localhost:5001 and you should see the app running
