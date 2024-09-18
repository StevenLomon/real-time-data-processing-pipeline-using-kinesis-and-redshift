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

(My very first instinct was to create an IAM User but for this specific project, it's best practice to instead use an IAM Role. And when trying to create the IAM Role and the policy needed, I encountered this error:
`Failed to create policy LambdaAccessToKinesisAndRedshift. The policy failed legacy parsing`
since I didn't have the ARN of the Kinesis stream. So the first step in this project is not within the IAM Console but in creating the Kinesis stream haha!)

### Creating the Kinesis stream
Since the Kinesis stream ARN will be needed to create the policy for the IAM Role that Lambda will use, the very first step is to create the Kinesis stream. Kinesis Data Streams is chosen over Managed Apache Flink (which is an advanced option that would be fun to dive into in the future!) and weather-data-stream is chosen as the name. 

Since the workload for this project is predictable and low (I will stick to under 1,000 API calls a day in order to keep it free haha), Provisioned Capacity is chosen for the Capacity Mode for cost-efficiency and since 1 shard is enough. The usage will likely be well within the capacity limits of a single shard (1 MB/sec input and 2 MB/sec output)

This can always scaled up later to handle more data, but this provides a good starting point that’s both cost-effective and sufficient for this educational project. The ARN is grabbed in order to be used in the creation of the policy to be used for the Lambda Role:

### IAM Role set up
To follow best practices, an IAM Role is to be used instead of an IAM User since the services in this specific architecture are interacting without the need for human intervention. This is also for security reasons (as credentials can be long-lived and thus a potential security risk).  
Since the project architecture diagram was done as one of the very first things in the process of the project, it was very clear that an IAM Role needed to be created and assigned to Lambda to temporarily get access to Kinesis and Redshift, and Glue can assume a role to grant access to Redshift for ETL jobs. A custom policy (LambdaAccessToKinesisAndRedshift) is created and attached to the Role rather than simply attaching the `AmazonKinesisFullAccess` policy in order to once again adhere to the Principle of Least Privilege.

The following policy was created and attached to the Role:
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

### Lambda

### Redshift

### PowerBI

### Terraform integration


