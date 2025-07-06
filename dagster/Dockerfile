FROM python:3.12-slim

ENV DAGSTER_HOME=/opt/dagster/app/

WORKDIR $DAGSTER_HOME
# Install Dagster and dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Create the dagster home directory
RUN mkdir -p $DAGSTER_HOME

# Copy configuration files
COPY dagster.yaml workspace.yaml $DAGSTER_HOME

# Copy the rest of the code
COPY . .

# Optional: expose Dagster UI port
EXPOSE 3000

# Command: start Dagster webserver in dev mode
CMD ["dagster", "dev"]
