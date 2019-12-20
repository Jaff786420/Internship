import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('dust.jpg')
s3.Bucket('trashbin2').put_object(Key='dust.jpg', Body=data)
