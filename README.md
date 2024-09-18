# Real-Time Weather Data Processing using Kinesis and Redshift

## Description
The idea is to build a real-time data pipeline that ingests data via Kinesis, processes it with Lambda, stores it in Redshift for analytical querying, and optionally uses Glue for data cataloging and ETL (Extract, Transform, Load) transformations if needed.

The OpenWeather API will be used for real-time streaming of weather data to mimic IoT sensor data from weather stations.
https://openweathermap.org/api

## Technologies used and project architecture
* Amazon Kinesis
* AWS Lambda
* Amazon Redshift
* PowerBI
* AWS Glue (if needed)

The project uses the following architecture:
![Project architecture diagram](/project-architecture-diagram.png "Project architecture diagram")


