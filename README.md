# Whisper API in Docker Container

The code in the repository creates a docker container for the transcription of an audio file using Whisper's base model.
This API is built using FastAPI inside a Docker container.

You can locally run the transcription endpoint using the following command : 
```
uvicorn transcribe_app:app --reload
```

You can also pull the transcription docker container from the following command : 
```
docker pull sanduaye/whisper-api
```

You can further refer to Whisper models using the repository of [OpenAI for Whisper](https://pages.github.com/)
