import boto3
import json


AWS_ACCESS_KEY_ID = 'AKIAIBRW524UJ4NXJSZA'
AWS_SECRET_ACCEESS_KEY = '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'




def s3_client():
    ''' creates s3 connection using boto3'''
    return boto3.client('s3',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCEESS_KEY
                        )



