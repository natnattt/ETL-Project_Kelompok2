# AssignmentDay35-Docker Introduction

## ETL (Extract, Transform, Load) Project

The setup is orchestrated using Docker Compose, ensuring seamless deployment and management of Postgres containers across different environments. This project is a demonstration of an ETL process using Python and PostgreSQL. The purpose of this project is to extract data from a source PostgreSQL database, perform some basic transformations, and load the transformed data into another PostgreSQL database.

## Features:
- Efficient ETL process from source to target Postgres tables.
- Docker Compose integration for easy setup and deployment.
- Utilization of a .env file for storing sensitive data securely.
- Flexibility to mount necessary data volumes as required.

## Minimum Requirements:
- Postgres version: 15
- Python version: 3.9

## Dataset Overview:
The project includes a synthetic dummy dataset for demonstration purposes. The dataset used in this project is a synthetic dataset generated for testing purposes. This dataset serves as a sample for testing purposes and is conveniently included within the repository. For more extensive testing scenarios, users are encouraged to explore publicly available datasets. For this project, we are using a sample dataset obtained from Kaggle. The dataset contains historical sales data for a fictional retail company. The dataset includes the following tables:
- customers: Information about the company's customers, including customer ID, name, email, and address.
- products: Details about the products sold by the company, including product ID, name, description, and price.
- orders: Records of sales transactions, including order ID, customer ID, product ID, quantity, and total amount.

## Usage Instructions:
1. Clone this repository to your local environment.
2. Customize the .env file with your Postgres credentials and any other sensitive information.
3. Ensure Docker and Docker Compose are installed on your system.
4. Run docker-compose up command to initiate the containers.
5. Execute the provided Python script to commence ETL operations seamlessly.

## Repository Structure:
- etl.py: Python script responsible for orchestrating ETL processes.
- docker-compose.yml: Configuration file defining the Docker Compose setup.
- .env: File containing environment variables for securing sensitive information.
- README.md: Comprehensive documentation detailing project setup, usage, and dataset information.

## Contributions and Feedback:
Contributions to this project are welcomed through pull requests or by reporting issues. Your feedback is invaluable and helps improve the quality of the project.

## License Information:
This project is licensed under the MIT License. Refer to the LICENSE file for detailed licensing information and terms.
