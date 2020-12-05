# Overview
Context in a demo application centered around data processing to train on various DevOps tooling  
Its general purpose is to collect data from social media based on a given keyword and then store, process, analyze and visualize this data

# General architecture design principles 
- Any component of the application can be deployed either on-premise or in a public cloud
- Kubernetes will be the preferred way to deploy anywhere
- The general rule of deployment, based on costs limitaion will be that long-running processes requiring no performance will run on-premise while performance-bound processes, especially transient ones, will be primarily deployed on cloud
