**Overview**

This project focuses on analyzing flight prices for the route from New York (NY) to Hyderabad (HYD). It involves extracting data from the Skyscraper API using Python, loading the extracted data into Cloud Storage, and then transferring it to BigQuery using Google Cloud Dataflow. Looker Studio is used on top of BigQuery for reporting and visualization of flight prices for the NY to HYD route. Future work will include automating the extraction of API data to Cloud Storage and automating the Dataflow job.

**Architecture**

![Architecture](https://github.com/Ravali-Satla/Flight-GCP-Data-Engineering-Project/assets/160687099/d6098532-ed2f-4593-8273-8263231b3a1c)





**Features**

Extract flight data from the Skyscraper API for the NY to HYD route using Python.
Load extracted data into Cloud Storage.
Transfer data from Cloud Storage to BigQuery using Google Cloud Dataflow.
Utilize Looker Studio for reporting and visualization on top of BigQuery.
Future work: Automate API data extraction and Dataflow job.
Setup

**Usage**

**Extract Data**: Run the extract_data_push.py script to extract flight data from the Skyscraper API for the NY to HYD route and save it to Cloud Storage.
**Data Processing**: Execute the Dataflow pipeline  to process the data from Cloud Storage and load it into BigQuery.
**Reporting and Visualization**: Utilize Looker Studio to create reports and dashboards for visualizing flight price trends for the NY to HYD route.

**Future Work**

Automate the extraction of API data to Cloud Storage by creating dag.
Automate the Dataflow job by setting up triggers or scheduling using Cloud Scheduler or Cloud Functions.

**Author**

Ravali Satla


