# Overview
Context in a demo application centered around data processing to train on various DevOps tooling  
Its general purpose is to collect data from social media based on a given keyword and then store, process, analyze and visualize this data

# General architecture design principles 
- Any component of the application can be deployed either on-premise or in a public cloud
- Kubernetes will be the preferred way to deploy anywhere
- The general rule of deployment, based on costs limitaion will be that long-running processes requiring no performance will run on-premise while performance-bound processes, especially transient ones, will be primarily deployed on cloud

# Project log
Date|Action(s)
---|---
Dec 5 2020|Write twitter_collector.py to retrieve data from Twitter streaming API, dump as JSON within container<br/>prepare Dockerfile for multistage build
Dec 6 2020|Create git repo<br/>Add Docker volume so data is written on the host
Dec 7 2020|Install Docker on Rasperry Pi<br/>Build and run container on RPI to gather data for future performance tests
