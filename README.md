# GitHub Popularity #

Description: Tells if a given github repository is popular or not!

### Assumptions
- The service is being accessed through a browser

### Tech Stack
Built using the FastAPI framework. libraries are kept as minimal as possible. Key libraries
include: Uvicorn, httpx, jinja2 and pytest

Runtime: Python 3.10.0 (can be found in `.python-version` file)

### Possible Improvements
- Allow for json requests
- Improve the UI on the front end
- Improve the error reporting
- Add functionality to compare two or more repositories


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

Run tests
```commandline
make runtest
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

# Available Endpoints #
```json lines
/         : Main application endpoint
/status   : Healthcheck endpoint
/docs     : Documentation
/redoc    : Documentation
```
