# > pip install boto3 -q
# > pip install awscli -q
# > aws configure

import boto3
import awscli

s3 = boto3.resource("s3")

# PUT
# data = open("data_jungle.json", "rb")
# s3.Bucket("test-codi42-python").put_object(Key="test/data_jungle.json", Body=data)

# GET
s3.Bucket("test-codi42-python").download_file("test/data_jungle.json", "data_down.json")

# %%
