# GitHub Popularity #
Displays popularity of a given github repository

# Install #
Creates a fresh virtual environment (called .venv) and installs requirements
```commandline
make setup
```

# Run #
Run a single instance of the uvicorn server for local development

Install pip requirements
```commandline
make pip_sync
```

Run server
```commandline
make runserver
```

# Docker #
To run the application using docker
```commandline
docker-compose up
```

To rebuild the image, then run the application
```commandline
docker-compose up --build
```

# Documentation #
Interactive API documentation available at the following endpoints:
```commandline
/docs
/redoc
```
