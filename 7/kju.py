
from PIL import Image, ImageFilter
import os

# Указываем путь к папке с исходными изображениями
input_folder = "\Users\Компьютер\PycharmProjects\pythonProject2\7\pets0"

# Указываем путь к папке для сохранения обработанных изображений
output_folder = "\Users\Компьютер\PycharmProjects\pythonProject2\7\Pets"

# Выбираем фильтр
filter_name = "SHARPEN"  # Замените на нужный фильтр из списка
filter_object = filters[filter_name]

# Проходим по всем файлам в папке с исходными изображениями
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Открываем изображение
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        # Применяем фильтр
        filtered_image = image.filter(filter_object)

        # Формируем новое имя файла и путь для сохранения
        base_name, extension = os.path.splitext(filename)
        new_filename = f"{base_name}_filtered{extension}"
        output_path = os.path.join(output_folder, new_filename)

        # Сохраняем обработанное изображение
        filtered_image.save(output_path)

print("Обработка завершена!")