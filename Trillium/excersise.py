import boto3

AWS_ACCESS_KEY_ID = 'AKIAIBRW524UJ4NXJSZA'
AWS_SECRET_ACCEESS_KEY = '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'
s3 = boto3.client('s3',
                  aws_access_key_id = AWS_ACCESS_KEY_ID,
                  aws_secret_access_key = AWS_SECRET_ACCEESS_KEY
                  )



import botocore


print (s3.meta.client.head_bucket(Bucket='mybucket'))
