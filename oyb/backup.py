class BaseBackupService:

    def init(self, storage):
        self.storage = storage

    def backup(self, files):
        for file in files:
            try:
                self.storage.store(file)
                update_status(file, True)
            except UploadFailureException, e:
                update_status(file, False)                


class SimpleBackupService(BaseBackupService):

            
    def update_status(file_path, success):
        pass

    
