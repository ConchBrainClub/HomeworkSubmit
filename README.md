# HomeworkSubmit

### How to Contribute?

Install pre-requisites

- Python3
- Python3-pip
- Docker
- DockerCompose

##### On Windows

- Visit [Python official website](https://www.python.org/) to download Python ( Included pip )

- [Install Docker](https://docs.docker.com/get-docker/) 

- [Install DockerCompose](https://docs.docker.com/compose/install)

##### On Linux

- Install Python & Python-pip
    - Ubuntu
        ```bash
        apt install python3 python3-pip -y
        ```

    - CentOS
        ```bash
        dnf install python3 python3-pip -y
        ```
- [Install Docker](https://docs.docker.com/get-docker/) 

- [Install DockerCompose](https://docs.docker.com/compose/install)

### Restore dependencies

```bash
pip3 install -r requirements.txt
```

### Run

```bash
python3 src/main.py
```

### Build Docker Image

```base
docker build .
```

### Build Docker Image with FileBrowser

```bash
docker-compose up
```

### What is FileBrowser?

[FileBrowser Repository](https://github.com/filebrowser/filebrowser)
