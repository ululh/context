# Twitter collector

Simple service running in a Docker container, collecting tweets through Twitter's streaming API and writing these tweets as newline-delimited JSON files in a Docker volume  
Depends on twython

# Parameters
keyword : the keyword to poll the Twitter Streaming API

# docker memo
docker build -t context/twitter_collector .
docker volume create tweets-vol   
docker run -d \
  --restart=always \
  --name twitter_collector \
  --mount source=tweets-vol,target=/app \
  context/twitter_collector:latest

