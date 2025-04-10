# Docker Setup for Web3ArbitrageBot

This document explains how to run the Web3ArbitrageBot project using Docker with hot reload functionality.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuration

Before running the container, make sure to update the following configuration in `const/config.py`:

```python
network = "vlx"  # Choose between "vlx" (VELAS), "matic" (POLYGON), "bnb" (BINANCE)
private_key = "{YOUR WALLET PRIVATE KEY HERE}"
wallet_address = "{THE WALLET ADDRESS THAT YOU WANT TO EXECUTE TRANSACTIONS HERE}"
trade_volume_limiter = 1
base_token = "{THE TOKEN YOU WANT TO TRADE}"
```

## Running the Bot

### 1. Build and Start the Container

```bash
docker-compose up --build
```

This will:
- Build the Docker image
- Start the container with hot reload enabled
- Run the `chainData.py` script to collect initial data

### 2. Running the Arbitrage Bot

You can either:

1. Modify the `docker-compose.yml` file to run `arbitrage.py` instead of `chainData.py`:

```yaml
command: run-with-reload arbitrage.py
```

2. Or open a new terminal and execute:

```bash
docker-compose exec arbitrage-bot run-with-reload arbitrage.py
```

## Hot Reload Feature

The container uses `watchdog` to monitor file changes. When you modify any Python file in the project, the running script will automatically restart, applying your changes instantly.

## Data Persistence

The container mounts the current directory as a volume, so any data files generated (like `data.vlx.json`) will persist on your host machine.

## Stopping the Bot

```bash
docker-compose down
```

## Viewing Logs

```bash
docker-compose logs -f
```

## Troubleshooting

### Issue: The bot isn't finding or creating trading pairs

Solution: Make sure you've run `chainData.py` first to collect exchange data before running `arbitrage.py`.

### Issue: Hot reload isn't working

Solution: Ensure you're making changes to files in the project directory on your host machine, not inside the container.