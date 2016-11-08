from django.core.files.storage import FileSystemStorage
from django.conf import settings

import os, logging
logger = logging.getLogger(__name__)

class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        
        logger.debug('handle uploaded file name ={0}', name)
        if self.exists(name):
            logger.debug('remove existing file, name ={0}', name)
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name