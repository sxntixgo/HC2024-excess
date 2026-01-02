# EXCESS - XSS CTF Challenge Suite

> **Disclaimer:** This project contains intentionally vulnerable web applications designed for CTF purposes only. Do NOT deploy to public-facing servers without proper access controls. Do NOT use these techniques against systems you do not own or have explicit permission to test.

## Overview

EXCESS is a progressive Cross-Site Scripting (XSS) challenge series created for SAINTCON's HackersChallenge 2024. It contains 8 levels that progress from basic unfiltered input to advanced obfuscation bypasses:

| Level | Difficulty | Technique |
|-------|------------|-----------|
| 0 | Easy | Basic script injection |
| 1 | Easy | Event handler XSS |
| 2 | Medium | Blacklist bypass |
| 3 | Medium | Tag/event whitelist bypass |
| 4 | Medium | SVG/Base64 injection |
| 5 | Medium | Encoding manipulation |
| 6 | Hard | JSFuck obfuscation |
| 7 | Hard | Fragment-based redirect |

## Quick Start (Local)

> **Note:** These instructions are for running the challenges locally for development or personal use.

### Prerequisites

- Docker and Docker Compose
- A local network IP address (not `127.0.0.1` or `0.0.0.0`)

### 1. Configure Your Local IP

Find your local IP address:

```bash
# macOS
ipconfig getifaddr en0

# Linux
hostname -I | awk '{print $1}'
```

### 2. Start the XSS Server

1. Navigate to the xssserver directory and update the fixtures with your local IP:

   Edit `xssserver/xssserver/server/fixtures/targetservers-local.yaml` and replace the IP addresses with your local IP.

2. Start the Docker containers:

   ```bash
   cd xssserver
   docker compose -f docker-compose-local.yml up
   ```

3. Access the server at `http://127.0.0.1:8000`

### 3. Start a Challenge Level

Each level has its own Docker configuration. To run a specific level:

```bash
cd level0
docker compose -f docker-compose-local.yml up
```

The challenge will be available at `http://<your_local_IP>:5000`.

Repeat for other levels as needed (`level1`, `level2`, etc.).