import boto3
from shutil import copy2
from .exceptions import UploadFailureException
import os

def get_storage():
    return TestStorage("/tmp")

class BasicStorage:
    pass

class TestStorage(BasicStorage):
    def __init__(self, storage_dest_path):
        self.storage_dest_path = storage_dest_path

    def store(self, file_path):
        try:
            print("inside store")
            print(file_path.strip("/"))
            self._create_bkp_path_folders(file_path)
            copy2(file_path, os.path.join(self.storage_dest_path, file_path.strip("/")))
        except (Exception) as  e:
            print (e)
            raise UploadFailureException()

    def _create_bkp_path_folders(self, file_path):
        print("insdide create dir")
        dir_path = os.path.join(self.storage_dest_path, os.path.dirname(file_path).strip("/"))
        print ("dirpath {0}",dir_path)
        os.makedirs(dir_path, exist_ok=True)
                
    

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
        except Exception as e:
            raise UploadFailureException()

    def list_buckets(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)


if __name__ == '__main__':
    storage = S3Storage()
    storage.list_buckets()
        
        
