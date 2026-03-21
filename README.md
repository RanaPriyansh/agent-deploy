# Agent Deploy

[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github)](https://github.com/RanaPriyansh/agent-deploy)
[![License](https://img.shields.io/github/license/RanaPriyansh/agent-deploy)](https://github.com/RanaPriyansh/agent-deploy/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/RanaPriyansh/agent-deploy)](https://github.com/RanaPriyansh/agent-deploy/commits/main)

Deploy AI agents to cloud/edge with one command. Supports Vercel, Railway, Fly.io, Kubernetes.

## Features

- **One-command deploy**: `agent-deploy deploy . --platform vercel`
- **Multi-platform**: Vercel, Railway, Fly.io, AWS Lambda, GCP Cloud Run
- **Configuration management**: Environment variables, secrets per environment
- **Rollback**: Quick rollback to previous version
- **Monitoring hook**: Auto-attach monitoring agents
- **Scaling**: Automatic scaling based on load

## Quick Start

```bash
# Install
pip install agent-deploy

# Deploy to Vercel
agent-deploy deploy ./my-agent --platform vercel --name my-agent-prod

# Deploy to Kubernetes
agent-deploy deploy ./my-agent --platform k8s --namespace agents
```

## Install

```bash
pip install agent-deploy
```

## Why

Deploying agents should be as easy as deploying a web app. This tool provides:
- Consistent deployment workflow across platforms
- Zero-config for common platforms (sensible defaults)
- Production-ready: secrets management, health checks, rollbacks
- Multi-cloud portability (avoid vendor lock-in)

## License

MIT
