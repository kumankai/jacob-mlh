#!/bin/bash
cd jacob-mlh
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker rmi jacob-mlh-myportfolio:latest
docker compose -f docker-compose.prod.yml up -d