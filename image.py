import os
import requests
import argparse
from duckduckgo_search import DDGS
import time

# CLI
parser = argparse.ArgumentParser(description="Tìm và tải ảnh từ DuckDuckGo")
parser.add_argument("keyword", type=str, help="Từ khóa tìm kiếm ảnh")
parser.add_argument("num_images", type=int, nargs='?', default=1, help="Số lượng ảnh muốn tải (mặc định: 1)")
args = parser.parse_args()

keyword = args.keyword
num_images = args.num_images

# Tạo thư mục
save_dir = "static/assets/images"
os.makedirs(save_dir, exist_ok=True)

# Tải ảnh
def fetch_and_download(keyword: str, num_images: int, retries: int = 3):
    for attempt in range(1, retries + 1):
        print(f"🔍 Thử tìm ảnh lần {attempt} với từ khóa: {keyword}")
        with DDGS() as ddgs:
            results = list(ddgs.images(keywords=keyword, max_results=num_images))

        if results:
            for idx, result in enumerate(results, start=1):
                url = result.get("image")
                try:
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()

                    # Luôn luôn lưu đuôi .jpg
                    file_path = os.path.join(save_dir, f"{keyword.replace(' ', '_')}.jpg")
                    with open(file_path, 'wb') as f:
                        f.write(response.content)

                    print(f"✅ Đã tải: {file_path}")
                except Exception as e:
                    print(f"❌ Lỗi khi tải ảnh #{idx}: {e}")
            print("\n🎉 Hoàn tất tải ảnh!")
            return
        else:
            print("⚠️ Không tìm thấy ảnh. Đang thử lại...")
            time.sleep(2)

    print("❌ Không thể tìm thấy ảnh sau nhiều lần thử.")

# Gọi hàm chính
fetch_and_download(keyword, num_images)
