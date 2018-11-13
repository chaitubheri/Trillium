import boto3


bucket_list = [
    'data-athena-rslt-dbcc-dev',
    'data-config-dbcc-dev',
    'data-inbound-dbcc-dev',
    'data-lake-dbcc-dev',
    'data-logs-dbcc-dev',
    'data-raw-dbcc-dev',
    'data-services-dbcc-dev',
    'data-sub-dbcc-dev']



for item in bucket_list:
    print(item)



