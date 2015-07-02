import boto3

class BasicStorage:
    pass

class S3Storage(BasicStorage):

    def __init__(self, aws_key=None, aws_secret=None, bucket_name=None):
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        self.bucket_name = bucket_name
        self.s3 = boto3.resource('s3')


    def store(self, file_path):
        try:
            data = open(file_path, 'rb')
            self.s3.Bucket(self.bucket_name).put_object(Key=file_path, Body=data)
        except Exception, e:
            raise UploadFailureException()

    def list_buckets(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)


if __name__ == '__main__':
    storage = S3Storage()
    storage.list_buckets()
        
        
