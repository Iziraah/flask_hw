import os
import threading
import requests
import time
import argparse

def download_image(url, output_folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_name = url.split("/")[-1]
            image_path = os.path.join(output_folder, image_name)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
            print(f"Изображение {image_name} успешно сохранено.")
        else:
            print(f"Ошибка при загрузке изображения с URL: {url}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

def download_images(image_urls, output_folder, thread_id):
    start_time = time.time()
    for url in image_urls:
        download_image(url, output_folder)
        print(f"Поток {thread_id}: Загрузка изображения по URL {url}")
    end_time = time.time()
    thread_time = end_time - start_time
    print(f"Поток {thread_id}: Время выполнения: {thread_time:.2f} сек")

def thread_worker(image_urls, output_folder, thread_id):
    download_images(image_urls, output_folder, thread_id)

def main():
    parser = argparse.ArgumentParser(description="Скачивание изображений по ссылкам с использованием threading")
    parser.add_argument("--output", default="downloaded_images", help="Папка для сохранения изображений")
    parser.add_argument("--num_threads", type=int, default=4, help="Количество потоков")
    
    args = parser.parse_args()
    
    start_total_time = time.time()
    
    urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Acacia_verticillata0.jpg/330px-Acacia_verticillata0.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Javor-Dab.JPG/330px-Javor-Dab.JPG",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Rotklee_Trifolium_pratense.jpg/300px-Rotklee_Trifolium_pratense.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Lepomis_gibbosus_U_S_Fish_and_Wildlife_Service.jpg/413px-Lepomis_gibbosus_U_S_Fish_and_Wildlife_Service.jpg"
    ]
    
    chunk_size = len(urls) // args.num_threads
    threads = []
    
    for i in range(args.num_threads):
        chunk = urls[i * chunk_size : (i + 1) * chunk_size]
        thread = threading.Thread(target=thread_worker, args=(chunk, args.output, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_total_time = time.time()
    total_time = end_total_time - start_total_time
    print(f"Общее время выполнения программы: {total_time:.2f} сек.")

if __name__ == "__main__":
    main()