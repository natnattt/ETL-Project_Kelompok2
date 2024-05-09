# Running Apache Airflow with Docker

## Setup Steps

Follow these steps to set up Apache Airflow with Docker:

1. **Create Docker Network**:
   Create a Docker network to allow communication between containers.

   ```bash
   docker network create my-network
   ```

2. **Create Docker Volume for PostgreSQL**:
   Create a Docker volume to persist PostgreSQL data.

   ```bash
   docker volume create postgres_airflow
   ```

3. **Download Docker Compose File**:
   Download the Docker Compose file provided in this repository.

4. **Modify Docker Compose File (Optional)**:
   If needed, modify the Docker Compose file to customize Airflow settings or credentials.

5. **Run Docker Compose**:
   Navigate to the directory containing the Docker Compose file and run the following command:

   ```bash
   docker-compose up -d
   ```

   This command will start Apache Airflow and PostgreSQL containers in detached mode.

6. **Access Airflow Web Interface**:
   Once the containers are up and running, you can access the Airflow web interface by navigating to `http://localhost:8080` in your web browser.

7. **Perform Additional Configuration** (Optional):
   - Customize Airflow configurations or settings as needed.
   - Set up connections and variables via the Airflow web interface.

8. **Start Building and Running Workflows**:
   With Apache Airflow set up, you can now define and run your workflows (DAGs) using the Airflow web interface.

## References

- [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
