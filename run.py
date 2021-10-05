#!/usr/bin/env python3

import argparse
import subprocess
import os

# Pass command line arguments to script
parser = argparse.ArgumentParser()
parser.add_argument("--numberagents","-a", required=False,
        help="Number of Azure DevOps agents wanted (Default: 1)") 
args = parser.parse_args()

if args.numberagents:
    numberagents = int(args.numberagents)
else:
    numberagents = 1

# Start containers
env_vars = {}
with open(".env") as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        if 'export' not in line:
             continue
        key, value = line.replace('export ', '', 1).strip().split('=', 1)
        if value.startswith('$'):
            cmd = f"echo {value}"
            try:
                process = subprocess.Popen(cmd, env={value.replace('$', ''):env_vars[value.replace('$', '')]}, shell=True, universal_newlines=True, stdout=subprocess.PIPE)
                variableValue = process.communicate()[0].strip()
            except:
                process = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE)
                variableValue = process.communicate()[0].strip()
        else:
            variableValue = value
        os.environ[key] = variableValue  # Load to local environ
        env_vars[key] = variableValue # Save to a dict

for agent_no in range(1, numberagents+1):
    print("========================")
    AZP_AGENT_NAME = f"{env_vars['AZP_AGENT_NAME']}_{agent_no}"
    print(f"Starting {AZP_AGENT_NAME}...")
    cmd = f"docker run --restart  always -d -e AZP_URL=$AZP_URL -e AZP_TOKEN=$AZP_TOKEN -e AZP_AGENT_NAME={AZP_AGENT_NAME} -e AZP_POOL=$AZP_POOL --net azdo_agents_network --name {AZP_AGENT_NAME} dockeragent:latest"
    os.system(cmd)

