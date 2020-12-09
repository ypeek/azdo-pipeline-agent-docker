## Azure DevOps Pipeline Agent Docker Image
This repository can be used to create an Azure DevOps Pipeline Agent for Docker.

### BUILD
docker build -t dockeragent:latest .

### DEPLOY
#### Environment variables needed to start
See [.env](.env)
- AZP_URL
- AZP_TOKEN
- AZP_AGENT_NAME
- AZP_POOL (Default = Default. Create pool before creating the agents. [Create here](https://dev.azure.com/<organization>/<project>/_settings/agentqueues))

#### Start command
docker run -d 

#### Use docker-compose
