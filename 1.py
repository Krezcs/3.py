import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def process_folder(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            extension = os.path.splitext(filename)[1]
            move_file(file_path, extension)


def move_file(file_path, extension):
    destination_folder = os.path.join("Мотлох", extension.lstrip('.'))
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_path)
    print(f"Moved: {file_path} -> {destination_path}")


if __name__ == "__main__":
    folder_path = input("Введіть шлях до папки: ")
    num_threads = 4  # Кількість потоків для паралельної обробки

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.submit(process_folder, folder_path)