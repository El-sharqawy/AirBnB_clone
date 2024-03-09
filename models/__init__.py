#!/usr/bin/python3
"""init method, the heart of the engine"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
