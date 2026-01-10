# Медиа-библиотека: иерархия классов для работы с файлами

## Описание проекта

Библиотека для работы с медиа-файлами (аудио, видео, изображения) и различными хранилищами. Реализована в рамках задания по продвинутому ООП.

## Архитектура классов

### 1. **Иерархия медиа-файлов (`media_file.py`)**

```text
MediaFile (абстрактный базовый класс)
├── AudioFile (аудиофайлы: MP3, WAV, FLAC)
├── VideoFile (видеофайлы: MP4, AVI, MKV)
└── ImageFile (изображения: JPEG, PNG, GIF)
```

**Общие атрибуты (наследуются от MediaFile):**
- `name` - имя файла
- `size` - размер в байтах  
- `owner` - владелец
- `created_at` - дата создания
- `modified_at` - дата изменения

**Специфичные атрибуты:**
- **AudioFile**: `duration`, `bitrate`, `artist`
- **VideoFile**: `duration`, `resolution`, `fps`
- **ImageFile**: `width`, `height`, `format`

### 2. **Иерархия хранилищ (`storage.py`)**

```text
Storage (абстрактный базовый класс)
├── LocalStorage (локальная файловая система)
├── CloudStorage (облачные хранилища: S3, Google Cloud)
└── RemoteStorage (удалённые серверы: FTP, SFTP)
```

**Общий интерфейс (методы Storage):**
- `save(file)` - сохранить файл
- `delete(file)` - удалить файл  
- `list_files()` - получить список файлов

### 3. **Обработчик файлов (`processor.py`)**

**MediaProcessor** - класс для операций с медиа-файлами:
- `convert(file, target_format)` - конвертация форматов
- `compress(file, quality)` - сжатие файлов
- `extract_metadata(file)` - извлечение метаданных
- `get_operations_log()` - получение журнала операций

## Структура проекта

```text
homework_04/
├── init.py         # Инициализация пакета
├── media_file.py   # Классы медиа-файлов
├── storage.py      # Классы хранилищ
├── processor.py    # Класс обработчика
└── README.md       # Документация
```

## Примеры использования

### Создание файлов

```python
from media_file import AudioFile, VideoFile, ImageFile

# Аудиофайл
audio = AudioFile(
    name="song.mp3",
    size=5242880,  # 5 MB
    owner="user123",
    duration=180.5,
    bitrate=320,
    artist="Cool Artist"
)

# Видеофайл
video = VideoFile(
    name="movie.mp4", 
    size=104857600,  # 100 MB
    owner="user123",
    duration=120.0,
    resolution="1920x1080",
    fps=30
)

# Изображение
image = ImageFile(
    name="photo.jpg",
    size=2097152,  # 2 MB
    owner="user123",
    width=1920,
    height=1080,
    format="JPEG"
)
```

### Работа с хранилищами

```python
from storage import LocalStorage, CloudStorage

# Локальное хранилище
local = LocalStorage(path="./media/")
local.save(audio)

# Облачное хранилище  
cloud = CloudStorage(bucket_name="my-bucket", region="eu-west-1")
cloud.save(video)

# Получение списка файлов
files = local.list_files()
```

### Обработка файлов

```python
from processor import MediaProcessor

processor = MediaProcessor()
processor.convert(audio, "wav")
processor.compress(video, quality=75)
metadata = processor.extract_metadata(image)
```

### Расширение библиотеки

**1. Добавление нового типа файла**
- Создать класс, унаследованный от MediaFile
- Реализовать абстрактный метод play()
- Добавить специфичные атрибуты и методы

```python
class DocumentFile(MediaFile):
    def __init__(self, name, size, owner, pages, author):
        super().__init__(name, size, owner)
        self.pages = pages
        self.author = author
    
    def play(self):
        print(f" Открытие документа: {self.name}")
```

**2. Добавление нового хранилища**
- Создать класс, унаследованный от Storage
- Реализовать методы save(), delete(), list_files()

```python
class DatabaseStorage(Storage):
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def save(self, file):
        # Логика сохранения в базу данных
        print(f"💾 Сохранение в БД: {file.name}")
```
## Ответы на вопросы
**1. Сколько кода нужно изменить при добавлении новых типов файлов?**
- **Ответ:** Существующий код менять НЕ НУЖНО.
- **Действия:** Создать 1 новый класс, унаследованный от MediaFile.
- **Пример:** Для добавления DocumentFile создаем 1 файл/класс, не трогая существующую архитектуру.

**2. Сколько кода нужно изменить при добавлении новых способов хранения?**
- **Ответ:** Существующий код менять НЕ НУЖНО.
- **Действия:** Создать 1 новый класс, унаследованный от Storage.
- **Пример:** Для добавления DatabaseStorage создаем 1 файл/класс, не изменяя существующие хранилища.

**3. Принципы ООП, реализованные в архитектуре:**
- **Наследование** - все файлы наследуются от MediaFile, все хранилища от Storage
- **Инкапсуляция** - данные и методы сгруппированы в классах
- **Полиморфизм** - общий интерфейс play() для всех файлов, общие методы для всех хранилищ
- **Абстракция** - абстрактные классы MediaFile и Storage определяют контракты

## Преимущества архитектуры
- **Открытость/закрытость** - система открыта для расширения, но закрыта для изменений
- **Низкая связанность** - классы файлов не зависят от классов хранилищ
- **Высокая связность** - каждый класс решает одну задачу
- **Легкость тестирования** - можно тестировать компоненты изолированно
- **Масштабируемость** - легко добавлять новые типы файлов и хранилищ