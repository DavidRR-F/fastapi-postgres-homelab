# Use the official Python image as the base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory within the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the poetry.lock and pyproject.toml files to the working directory
COPY poetry.lock pyproject.toml ./

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the FastAPI application will run
EXPOSE 8000

# Set the command to run the FastAPI application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]