"""
Классы для работы с различными хранилищами.
"""
from abc import ABC, abstractmethod
from .media_file import MediaFile


class Storage(ABC):
    """Абстрактный базовый класс для хранилищ."""

    @abstractmethod
    def save(self, file: MediaFile):
        """Сохранить файл в хранилище."""
        pass

    @abstractmethod
    def delete(self, file: MediaFile):
        """Удалить файл из хранилища."""
        pass

    @abstractmethod
    def list_files(self):
        """Получить список файлов в хранилище."""
        pass

    def get_storage_type(self):
        """Возвращает тип хранилища."""
        return self.__class__.__name__


class LocalStorage(Storage):
    """Локальное хранилище (файловая система)."""

    def __init__(self, path: str = "./"):
        """
        Инициализация локального хранилища.

        Args:
            path: Путь к директории хранилища
        """
        self.path = path
        self.files = []  # Список для хранения информации о файлах

    def save(self, file: MediaFile):
        """Сохранить файл локально."""
        print(f" Сохранение локально: {file.name}")
        print(f"  Путь: {self.path}")
        print(f"  Размер: {file.size} байт")

        # Здесь была бы реальная логика сохранения файла

        self.files.append(file.name)
        return True

    def delete(self, file: MediaFile):
        """Удалить локальный файл."""
        print(f" Удаление локального файла: {file.name}")
        if file.name in self.files:
            self.files.remove(file.name)
            return True
        return False

    def list_files(self):
        """Получить список локальных файлов."""
        print(f" Файлы в локальном хранилище ({self.path}):")
        for file in self.files:
            print(f"   - {file}")
        return self.files


class CloudStorage(Storage):
    """Облачное хранилище (например, Amazon S3, Google Cloud)."""

    def __init__(self, bucket_name: str, region: str = "us-east-1"):
        """
        Инициализация облачного хранилища.

        Args:
            bucket_name: Имя бакета (контейнера)
            region: Регион хранения
        """
        self.bucket_name = bucket_name
        self.region = region
        self.stored_files = {}  # Словарь для хранения файлов

    def save(self, file: MediaFile):
        """Загрузить файл в облако."""
        print(f" Загрузка в облако: {file.name}")
        print(f"  Бакет: {self.bucket_name}")
        print(f"  Регион: {self.region}")
        print(f"  URL: https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{file.name}")

        # Сохраняем информацию о файле
        self.stored_files[file.name] = {
            'size': file.size,
            'owner': file.owner,
            'uploaded_at': file.created_at
        }
        return True

    def delete(self, file: MediaFile):
        """Удалить файл из облака."""
        print(f" Удаление из облака: {file.name}")
        if file.name in self.stored_files:
            del self.stored_files[file.name]
            return True
        return False

    def list_files(self):
        """Получить список файлов в облаке."""
        print(f" Файлы в облачном хранилище ({self.bucket_name}):")
        for filename, info in self.stored_files.items():
            print(f"   - {filename} ({info['size']} bytes)")
        return list(self.stored_files.keys())


class RemoteStorage(Storage):
    """Удаленное хранилище (FTP, SFTP, WebDAV)."""

    def __init__(self,
                 host: str,
                 port: int = 21,
                 username: str = None
                 ):
        """
        Инициализация удаленного хранилища.

        Args:
            host: Адрес сервера
            port: Порт подключения
            username: Имя пользователя
        """
        self.host = host
        self.port = port
        self.username = username
        self.connected = False
        self.remote_files = []

    def connect(self):
        """Подключиться к удаленному хранилищу."""
        print(f" Подключение к {self.host}:{self.port}")
        self.connected = True
        return True

    def save(self, file: MediaFile):
        """Загрузить файл на удаленный сервер."""
        if not self.connected:
            self.connect()

        print(f" Загрузка на удаленный сервер: {file.name}")
        print(f"  Сервер: {self.host}:{self.port}")
        print(f"  Пользователь: {self.username}")

        self.remote_files.append(file.name)
        return True

    def delete(self, file: MediaFile):
        """Удалить файл с удаленного сервера."""
        print(f" Удаление с удаленного сервера: {file.name}")
        if file.name in self.remote_files:
            self.remote_files.remove(file.name)
            return True
        return False

    def list_files(self):
        """Получить список файлов на удаленном сервере."""
        print(f" Файлы на удаленном сервере ({self.host}):")
        for file in self.remote_files:
            print(f"   - {file}")
        return self.remote_files
