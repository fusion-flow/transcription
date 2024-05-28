# Whisper API for transcription

The code in the repository creates a docker container for the transcription of an audio file using Whisper's base model.
This API is built using FastAPI inside a Docker container.

## How to Run

You can locally run the transcription endpoint using the following command : 
```
uvicorn transcribe_app:app --reload
```

You can also pull the transcription docker container from the following command : 
```
docker pull sanduaye/whisper-api
```

Then you can call use the following CURL command to send an audio file for transcription.
```
curl -X 'POST' \
  'http://localhost:PORT/whisper/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@audio_file_name.mp3;type=audio/mpeg'
```

Note: The PORT should be the port that you are running the transcription service.

## Acknowledgement

You can further refer to Whisper models using the repository of [OpenAI for Whisper](https://pages.github.com/)
