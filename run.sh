#!/bin/bash

case "$1" in
  build)
    echo "Building Docker container..."
    docker-compose build
    ;;
  chaindata)
    echo "Running chainData.py to collect exchange data..."
    docker-compose up
    ;;
  arbitrage)
    echo "Running arbitrage.py to execute trades..."
    docker-compose exec conciliate run-with-reload arbitrage.py
    ;;
  shell)
    echo "Opening shell in the container..."
    docker-compose exec conciliate bash
    ;;
  down)
    echo "Stopping all containers..."
    docker-compose down
    ;;
  logs)
    echo "Showing logs..."
    docker-compose logs -f
    ;;
  *)
    echo "Usage: $0 {build|chaindata|arbitrage|shell|down|logs}"
    echo ""
    echo "Commands:"
    echo "  build      - Build the Docker container"
    echo "  chaindata  - Run chainData.py to collect exchange data"
    echo "  arbitrage  - Run arbitrage.py to find and execute trades" 
    echo "  shell      - Open a shell in the container"
    echo "  down       - Stop all containers"
    echo "  logs       - Show container logs"
    ;;
esac