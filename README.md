# Create a Serverless project

Work inside your AWS Cloud9 environment.

## Configure local environment

Configure Confirm that you are using the local credentials, and set the region name to **`us-east-1`** and the output format to **`json`**. 

``` bash
aws configure
```

## Install dependencies

``` bash
npm install -g serverless
```

## Create a Serverless project

``` bash
serverless create --template aws-python --path serverless-s3-dynamodb
```

Replace your **handler.py** with the following file [handler.py](handler.py).
Replace your **serverless.yml** with the following file [serverless.yml](serverless.yml).

## Deploy your Serverless project

``` bash
serverless deploy
```
