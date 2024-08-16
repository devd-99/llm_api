FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    nginx \
    python3-full \
    python3-pip \
    python3.12-venv \ 
    curl \ 
    wget

EXPOSE 80 11434

CMD ["nginx", "-g", "daemon off;"]