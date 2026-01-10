"""
Классы для обработки медиа-файлов.
"""
from .media_file import MediaFile


class MediaProcessor:
    """Процессор для операций с медиа-файлами."""

    def __init__(self):
        self.operations_log = []

    def convert(self,
                file: MediaFile,
                target_format: str
                ):
        """
        Конвертировать файл в другой формат.

        Args:
            file: Исходный файл
            target_format: Целевой формат

        Returns:
            Новый объект файла или None в случае ошибки
        """
        print(f" Конвертация: {file.name} -> {target_format}")
        print(f"  Исходный тип: {file.__class__.__name__}")

        # Логируем операцию
        self.operations_log.append({
            'operation': 'convert',
            'file': file.name,
            'from': file.extension,
            'to': target_format,
            'timestamp': file.created_at
        })

        # Возвращаем новый файл (заглушка)
        # В реальности здесь была бы логика конвертации
        return file

    def compress(self,
                 file: MediaFile,
                 quality: int = 80
                 ):
        """
        Сжать медиа-файл.

        Args:
            file: Файл для сжатия
            quality: Качество (0-100)
        """
        print(f" Сжатие файла: {file.name}")
        print(f"  Качество: {quality}%")

        old_size = file.size
        # Симуляция сжатия
        new_size = int(old_size * (quality / 100))

        self.operations_log.append({
            'operation': 'compress',
            'file': file.name,
            'old_size': old_size,
            'new_size': new_size,
            'quality': quality
        })

        return new_size

    def extract_metadata(self, file: MediaFile) -> dict:
        """
        Извлечь метаданные из файла.

        Args:
            file: Файл для анализа

        Returns:
            Словарь с метаданными
        """
        print(f" Извлечение метаданных: {file.name}")

        metadata = file.get_info()

        # Добавляем специфичные метаданные в зависимости от типа
        if hasattr(file, 'get_audio_info'):
            metadata.update(file.get_audio_info())
        elif hasattr(file, 'get_video_info'):
            metadata.update(file.get_video_info())
        elif hasattr(file, 'get_image_info'):
            metadata.update(file.get_image_info())

        self.operations_log.append({
            'operation': 'extract_metadata',
            'file': file.name,
            'metadata_keys': list(metadata.keys())
        })

        return metadata

    def get_operations_log(self):
        """Получить журнал операций."""
        return self.operations_log

    def clear_log(self):
        """Очистить журнал операций."""
        self.operations_log = []
        print(" Журнал операций очищен")