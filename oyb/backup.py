from os import listdir
from os.path import isfile, join
from . import storage
from .exceptions import UploadFailureException
import os

class BaseBackupService:

    def __init__(self, storage):
        self.storage = storage

    def backup(self, backup_src_path):
        try:
            current_file_path = None
            for root, dirs, files in os.walk(backup_src_path):
                for name in files:
                    current_file_path = os.path.join(root, name)
                    self.storage.store(current_file_path)
                    self.update_status(current_file_path, True)
        except (UploadFailureException) as e:
            self.update_status(current_file_path, False)
                
    def update_status(self, file_path, status):
        pass

    def init_MD_repository(backup_src_path):
        """Checks if the Metadata repository is there, 
        if not creates one"""
        pass

    def get_modified_files(self, backup_src_path):
        pass


class SimpleBackupService(BaseBackupService):
            
    def update_status(file_path, success):
        pass


if __name__ == "__main__":
    storage = storage.get_storage()
    bs = BaseBackupService(storage)
    bs.backup("/home/sankar/backup")
            

    
