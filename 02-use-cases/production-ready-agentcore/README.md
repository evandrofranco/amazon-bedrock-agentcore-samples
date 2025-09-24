# Production-Ready Amazon Bedrock AgentCore

## Overview

This use case demonstrates how to deploy Amazon Bedrock AgentCore in a production-ready environment with enterprise-grade security, networking, and operational best practices.

We'll walk through a complete step-by-step process to set up a secure, scalable infrastructure and deploy AI agents that meet enterprise requirements.

### Use Case Details

| Information         | Details                                                                          |
|:--------------------|:---------------------------------------------------------------------------------|
| Use case type       | Production Infrastructure                                                        |
| Agent type          | Single & Multi-agent                                                            |
| Agentic Framework   | Strands Agents                                                                   |
| LLM model           | Anthropic Claude Sonnet 3.7                                                     |
| Components          | Private VPC, Security Groups, VPC Endpoints, AgentCore Runtime                  |
| Vertical            | Enterprise Infrastructure                                                        |
| Complexity          | Advanced                                                                         |
| SDK used            | Amazon BedrockAgentCore Python SDK, boto3, AWS CDK                              |

### Architecture Overview

This production-ready setup includes:

1. **Secure Network Infrastructure**: Private VPC with isolated subnets
2. **Enterprise Security**: Security Groups, NACLs, and VPC Endpoints
3. **Scalable Agent Deployment**: AgentCore Runtime with production configurations
4. **Monitoring & Observability**: CloudWatch, X-Ray tracing, and custom metrics

<div style="text-align:left">
    <img src="images/production_architecture.png" width="100%"/>
</div>

## Step-by-Step Implementation

### Step 1: Create Private VPC Infrastructure
**Notebook**: `01-create-private-vpc.ipynb`

Set up the foundational network infrastructure with:
- Private VPC with multiple availability zones
- Private and public subnets
- Internet Gateway and NAT Gateways
- VPC Endpoints for AWS services
- Security Groups and Network ACLs

### Step 2: Deploy Production Agent
**Notebook**: `02-deploy-production-agent.ipynb`

Deploy a Strands agent within the secure VPC:
- Configure AgentCore Runtime in private subnets
- Set up secure communication channels
- Implement enterprise authentication
- Configure monitoring and logging

## Key Features

* **Enterprise Security**: Complete network isolation and secure communication
* **Scalability**: Auto-scaling configurations for production workloads
* **Monitoring**: Comprehensive observability and alerting
* **High Availability**: Multi-AZ deployment with failover capabilities
* **Cost Optimization**: Resource tagging and cost monitoring

## Prerequisites

- AWS CLI configured with appropriate permissions
- Python 3.10+ with Jupyter notebook support
- Docker installed (for local testing)
- AWS CDK v2 installed
- Required AWS service quotas for VPC and AgentCore

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the notebooks in sequence:
   - Start with `01-create-private-vpc.ipynb`
   - Then proceed to `02-deploy-production-agent.ipynb`

## Security Considerations

- All traffic flows through private subnets
- VPC Endpoints eliminate internet traffic for AWS services
- Security Groups implement least-privilege access
- All data encrypted in transit and at rest
- IAM roles follow principle of least privilege

## Cost Optimization

- Use Spot instances where appropriate
- Implement auto-scaling policies
- Monitor and optimize VPC Endpoint usage
- Regular cost reviews and resource cleanup

## Troubleshooting

Common issues and solutions are documented in each notebook. For additional support, refer to the AWS documentation or contact your AWS support team.
