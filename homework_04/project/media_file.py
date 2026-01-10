"""
Базовые классы для медиа-файлов.
"""
from datetime import datetime
from abc import ABC, abstractmethod


class MediaFile(ABC):
    """Абстрактный базовый класс для всех медиа-файлов."""

    def __init__(self, name: str, size: int, owner: str):
        """
        Инициализация медиа-файла.

        Args:
            name: Имя файла
            size: Размер в байтах
            owner: Владелец файла
        """
        self.name = name
        self.size = size
        self.owner = owner
        self.created_at = datetime.now()
        self.modified_at = datetime.now()

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} ({self.size} bytes)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', size={self.size})"

    @property
    def extension(self):
        """Возвращает расширение файла."""
        return self.name.split('.')[-1] if '.' in self.name else ''

    def get_info(self) -> dict:
        """Возвращает основную информацию о файле."""
        return {
            'name': self.name,
            'size': self.size,
            'owner': self.owner,
            'type': self.__class__.__name__,
            'created': self.created_at,
            'modified': self.modified_at
        }

    def rename(self, new_name: str):
        """Переименовывает файл."""
        old_name = self.name
        self.name = new_name
        self.modified_at = datetime.now()
        print(f"Файл переименован: {old_name} -> {new_name}")

    @abstractmethod
    def play(self):
        """Воспроизвести файл (абстрактный метод)."""
        pass


class AudioFile(MediaFile):
    """Класс для аудио-файлов."""

    def __init__(self,
                 name: str,
                 size: int,
                 owner: str,
                 duration: float,
                 bitrate: int,
                 artist: str = None
                 ):
        """
        Инициализация аудио-файла.

        Args:
            duration: Длительность в секундах
            bitrate: Битрейт в кбит/с
            artist: Исполнитель (опционально)
        """
        super().__init__(name, size, owner)
        self.duration = duration
        self.bitrate = bitrate
        self.artist = artist

    def play(self):
        """Воспроизвести аудио."""
        print(f" Воспроизведение аудио: {self.name}")
        if self.artist:
            print(f"  Исполнитель: {self.artist}")
        print(f"  Длительность: {self.duration} сек")

    def get_audio_info(self) -> dict:
        """Возвращает специфичную для аудио информацию."""
        info = self.get_info()
        info.update({
            'duration': self.duration,
            'bitrate': self.bitrate,
            'artist': self.artist
        })
        return info


class VideoFile(MediaFile):
    """Класс для видео-файлов."""

    def __init__(self,
                 name: str,
                 size: int,
                 owner: str,
                 duration: float,
                 resolution: str,
                 fps: int
                 ):
        """
        Инициализация видео-файла.

        Args:
            duration: Длительность в секундах
            resolution: Разрешение (например, '1920x1080')
            fps: Кадров в секунду
        """
        super().__init__(name, size, owner)
        self.duration = duration
        self.resolution = resolution
        self.fps = fps

    def play(self):
        """Воспроизвести видео."""
        print(f" Воспроизведение видео: {self.name}")
        print(f"  Разрешение: {self.resolution}")
        print(f"  FPS: {self.fps}")
        print(f"  Длительность: {self.duration} сек")

    def get_video_info(self) -> dict:
        """Возвращает специфичную для видео информацию."""
        info = self.get_info()
        info.update({
            'duration': self.duration,
            'resolution': self.resolution,
            'fps': self.fps
        })
        return info


class ImageFile(MediaFile):
    """Класс для изображений."""

    def __init__(self,
                 name: str,
                 size: int,
                 owner: str,
                 width: int,
                 height: int,
                 format: str
                 ):
        """
        Инициализация изображения.

        Args:
            width: Ширина в пикселях
            height: Высота в пикселях
            format: Формат ('JPEG', 'PNG', etc.)
        """
        super().__init__(name, size, owner)
        self.width = width
        self.height = height
        self.format = format

    def play(self):
        """Отобразить изображение."""
        print(f" Отображение изображения: {self.name}")
        print(f"  Размер: {self.width}x{self.height}")
        print(f"  Формат: {self.format}")

    def get_image_info(self) -> dict:
        """Возвращает специфичную для изображения информацию."""
        info = self.get_info()
        info.update({
            'width': self.width,
            'height': self.height,
            'format': self.format
        })
        return info
