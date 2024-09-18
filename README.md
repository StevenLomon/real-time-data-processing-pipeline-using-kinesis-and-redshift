# Real-Time Weather Data Processing using Kinesis and Redshift

## Description
The idea is to build a real-time data pipeline that ingests data via Kinesis, processes it with Lambda, stores it in Redshift for analytical querying, and optionally uses Glue for data cataloging and additional ETL jobs if needed.

The OpenWeather API will be used for real-time streaming of weather data to mimic IoT sensor data from weather stations.
https://openweathermap.org/api

## Technologies used and project architecture
* Amazon Kinesis
* AWS Lambda
* Amazon Redshift
* PowerBI
* AWS Glue (if needed)
* Terraform (will be integrated in retrospect after the entire project is done)

The project uses the following architecture:
![Project architecture diagram](/project-architecture-diagram.png "Project architecture diagram")

## Project journal

### IAM Role set up
To follow best practices, an IAM Role is to be used instead of an IAM User since the services in this specific architecture are interacting without the need for human intervention. This is also for security reasons (as credentials can be long-lived and thus a potential security risk).  
Since the project architecture diagram was done as one of the very first things in the process of the project, it was very clear that an IAM Role needed to be created and assigned to Lambda to temporarily get access to Kinesis and Redshift, and Glue can assume a role to grant access to Redshift for ETL jobs.

The following Role was created:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:GetRecords",
                "kinesis:GetShardIterator",
                "kinesis:DescribeStream",
                "kinesis:ListStreams"
            ],
            "Resource": "arn:aws:kinesis:REGION:ACCOUNT_ID:stream/YOUR_STREAM_NAME"
        },
        {
            "Effect": "Allow",
            "Action": [
                "redshift:CopyFromS3",
                "redshift:GetClusterCredentials",
                "redshift:ExecuteQuery"
            ],
            "Resource": "*"
        }
    ]
}
```

### API Access
An account was created on the openweathermap site and an API access key was created. 

### Kinesis

### Lambda

### Redshift

### PowerBI

### Terraform integration


