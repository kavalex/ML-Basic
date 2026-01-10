"""
Примеры использования классов медиа-библиотеки.
Этот файл не является частью библиотеки, только демонстрация.
"""

from project.media_file import AudioFile, VideoFile, ImageFile
from project.storage import LocalStorage, CloudStorage
from project.processor import MediaProcessor

# Пример 1: Создание файлов
print("=== Пример 1: Создание файлов ===")
audio = AudioFile("song.mp3", 5242880, "alice", 180, 320, "Artist")
video = VideoFile("movie.mp4", 104857600, "bob", 120, "1920x1080", 30)
image = ImageFile("photo.png", 2097152, "charlie", 1920, 1080, "PNG")

print(f"Аудио: {audio.name}, размер: {audio.size} байт")
print(f"Видео: {video.name}, разрешение: {video.resolution}")
print(f"Изображение: {image.name}, формат: {image.format}")

# Пример 2: Работа с хранилищами
print("\n=== Пример 2: Работа с хранилищами ===")
local = LocalStorage("./my_media/")
cloud = CloudStorage("media-bucket-123", "us-east-1")

local.save(audio)
cloud.save(video)

# Пример 3: Обработка файлов
print("\n=== Пример 3: Обработка файлов ===")
processor = MediaProcessor()
processor.convert(audio, "wav")
processor.compress(image, 50)

print("Готово!")