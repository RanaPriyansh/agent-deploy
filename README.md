# Thielon Agent Deploy

Deploy AI agents to cloud/edge with one command. Supports Vercel, Railway, Fly.io, Kubernetes.

## Features

- **One-command deploy**: `thielon-agent deploy . --platform vercel`
- **Multi-platform**: Vercel, Railway, Fly.io, AWS Lambda, GCP Cloud Run
- **Configuration management**: Environment variables, secrets per environment
- **Rollback**: Quick rollback to previous version
- **Monitoring hook**: Auto-attach monitoring agents
- **Scaling**: Automatic scaling based on load

## Quick Start

```bash
# Install
pip install thielon-agent-deploy

# Deploy to Vercel
thielon-agent deploy ./my-agent --platform vercel --name my-agent-prod

# Deploy to Kubernetes
thielon-agent deploy ./my-agent --platform k8s --namespace agents
```

## Install

```bash
pip install thielon-agent-deploy
```

## Why

Deploying agents should be as easy as deploying a web app. This tool provides:
- Consistent deployment workflow across platforms
- Zero-config for common platforms (sensible defaults)
- Production-ready: secrets management, health checks, rollbacks
- Multi-cloud portability (avoid vendor lock-in)

## License

MIT
