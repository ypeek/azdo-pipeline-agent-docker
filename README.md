## Build Status
[![Build Status](https://dev.azure.com/yorampeek/UniversalExports/_apis/build/status/KPN_MB_Delen.BUILD?branchName=main)](https://dev.azure.com/yorampeek/UniversalExports/_build/latest?definitionId=6&branchName=main)

## Azure DevOps Pipeline Agent Docker Image
This repository can be used to create an Azure DevOps Pipeline Agent for Docker.

### BUILD
docker build -t dockeragent:latest .

### DEPLOY
#### Environment variables needed to start
See [.env](.env.example)
- AZP_URL
- AZP_TOKEN
- AZP_AGENT_NAME
- AZP_POOL (Default = Default. Create pool before creating the agents. [Create here](https://dev.azure.com/yorampeek/_settings/agentpools))

#### Start command
##### Create docker network for agents
docker network create azdo_agents_network

#### Start container
docker run -d -e AZP_URL=$AZP_URL -e AZP_TOKEN=$AZP_TOKEN -e AZP_AGENT_NAME=$AZP_AGENT_NAME -e AZP_POOL=$AZP_POOL --net azdo_agents_network --name $AZP_AGENT_NAME dockeragent:latest

#### Use docker-compose
docker-compose up -d
