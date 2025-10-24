# HR Analytics

> A project from course Big Data & Cloud

This project focuses on a cloud deployment of a ETL pipeline to Azure using Terraform as infrastructure as code. The pipeline includes dlt script, dbt transformation presented in a Streamlit dashboard and orchestrated in Dagster.

## Architectural decisions in Azure and the costs it drives
To keep this service always available to users and update the data warehouse once per day, the Azure resources mentioned below is needed. Read the table to better understand the cost drivers. Below the table, a pricing example is found.

Following roles are used:
| Azure Resource | Description | Primary Cost Model | Fixed Cost Components (Charged 24/7) | Running Cost Components |
| -------- | ------- | ------- | ------- | ------- |
| App Service Plan  | The web app itself has no separate cost but its costs are included in the App Service Plan. We have selected the lowest pricing tier in a Linux based plan, Basic B1. Each tier comes with a fixed amount of allocated vCPU, RAM, and Storage. We pay for this allocation 24/7, even if the web app is stopped or idle. We have not enabled scaling and only have one running instances. | Fixed (Reserved Compute) | | |
| Container Registry | Stores, manages, and distributes container images (the static blueprint). Price per day based on service tier, which is the fixed base cost and includes a set amount of storage. | Fixed (Tier-Based) | Daily Fee for the selected tier (Basic in our case) which includes a base amount of storage. | Only if limits are exceeded |
| Storage Account | Azure File Shares. The storage account bills only for what we store, measured in GiB per month and what we do with it (transactions). Also depends on the redundancy of choice, copies and geographic spread. We have the cheapest LRS and no geographical spread, nor backups. Transactions (Operations) - The cost for every read, write, delete, or list operation (API call) you perform on the files in your share. As we are charged per a block of operations (e.g., per 10,000 transactions), we will not exceed to lowest limit.The transaction cost depends heavily on the chosen access tier. We have cool, lower storage costs and higher transaction and data retrieval costs | Running (Consumption based) | | Storage Capacity (price per GiB per month) based on the redundancy option LRS and access tier Cool. Transactions (cost per 10,000 operations) |
| Container Instances (ACI) | We pay for the resources allocated to the container group for the duration it is running, billed down to the second. Primary pricing components is vCPU Duration: The amount of virtual CPU cores requested for the container group, charged per second and Memory (GiB) Duration: The amount of memory (in gigabytes) requested for the container group, charged per second. | Consumption (Serverless Compute) | | vCPU and Memory Duration (Charged per second from deployment until stop/ |deletion). 

## Cost estimation - cloud deployment
### Assumptions
The duckdb data warehouse should be updated once per day
The deployed dashboard should be always available to users
Focusing on Pay as you go pricing plan. Other billing models exist, like provisioned models. They operate on a provisioned basis where you pay for reserved storage, and throughput, regardless of actual usage. These other plans are not covered here.
### Pricing example
Goes here....

### Data linegae in dbt 👇
![Data lineage!](dbt_job_ads/assets/dbt_lineage_graph.png "Lineage graph")

#### Data tests
**Generic data tests (dbt core)**
* All primary keys has unique tests. Checks for unique values in a column.
* All primary keys has not_null tests. Ensures no values in a column are null.
* Foreign key constraints is tested on all foreign keys. Referntial integrity ensured using relationship tests.

**dbt_expectations tests**
* expect_column_values_to_be_of_type, check specifc types of key columns

**Bespoke tests**
* See test_occupational_field_values.sql for accepted values test. Checks that all values in a occupational field contains the intended fields.