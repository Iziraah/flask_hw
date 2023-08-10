import os
import asyncio
import aiohttp
import aiofiles
import time
import argparse

async def download_image(session, url, output_folder):
    try:
        start_time = time.time()
        
        async with session.get(url) as response:
            if response.status == 200:
                image_name = url.split("/")[-1]
                image_path = os.path.join(output_folder, image_name)
                
                async with aiofiles.open(image_path, "wb") as image_file:
                    await image_file.write(await response.read())
                end_time = time.time()
                download_time = end_time - start_time
                print(f"Изображение {image_name} успешно сохранено. Время загрузки: {download_time:.2f} сек.")
            else:
                print(f"Ошибка при загрузке изображения с URL: {url}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

async def download_images(image_urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, output_folder) for url in image_urls]
        await asyncio.gather(*tasks)

def get_urls_from_input():
    urls = []
    print("Введите URL-адреса изображений (для завершения введите 'done'):")
    while True:
        url = input()
        if url.lower() == "done":
            break
        urls.append(url)
    return urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скачивание изображений по ссылкам")
    parser.add_argument("--output", default="downloaded_images", help="Папка для сохранения изображений")
    parser.add_argument("--interactive", action="store_true", help="Выбор ссылок интерактивно")
    
    args = parser.parse_args()
    
    if args.interactive:
        urls = get_urls_from_input()
    else:
        urls = [
           "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Acacia_verticillata0.jpg/330px-Acacia_verticillata0.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Javor-Dab.JPG/330px-Javor-Dab.JPG",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Rotklee_Trifolium_pratense.jpg/300px-Rotklee_Trifolium_pratense.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/deLepomis_gibbosus_U_S_Fish_and_Wildlife_Service.jpg/413px-Lepomis_gibbosus_U_S_Fish_and_Wildlife_Service.jpg"
        ]
    
    start_total_time = time.time()
    asyncio.run(download_images(urls, args.output))
    end_total_time = time.time()
    total_time = end_total_time - start_total_time
    print(f"Общее время выполнения программы: {total_time:.2f} сек.")