"""
Медиа-библиотека для работы с файлами и хранилищами.
"""

from .media_file import MediaFile, AudioFile, VideoFile, ImageFile
from .storage import Storage, LocalStorage, CloudStorage, RemoteStorage
from .processor import MediaProcessor

__all__ = [
    'MediaFile', 'AudioFile', 'VideoFile', 'ImageFile',
    'Storage', 'LocalStorage', 'CloudStorage', 'RemoteStorage',
    'MediaProcessor'
]