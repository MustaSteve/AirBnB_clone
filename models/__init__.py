"""Module for FileStorage autoinit."""

from models.engine.file_storage import FileStorage
'''FileStorage module'''

storage = FileStorage()
storage.reload()
