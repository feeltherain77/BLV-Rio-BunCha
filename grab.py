import requests
import re

def grab_all_blv():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://bunchatv4.net/'
    }
    
    m3u_content = '#EXTM3U\n'
    try:
        # 1. Lấy danh sách tất cả các trận và BLV từ trang chủ
        home_res = requests.get('https://bunchatv4.net/', headers=headers, timeout=15)
        home_text = home_res.text
        
        # 2. Tìm tất cả các link có chứa "binh-luan-vien" (Đây là nơi chứa link stream của từng BLV)
        # Loại bỏ các link có chữ "nha-dai" theo yêu cầu của ông
        blv_matches = re.findall(r'href="([^"]*binh-luan-vien/[^"]*)"', home_text)
        
        # Loại bỏ trùng lặp và lọc bỏ "nhà đài"
        final_blv_paths = list(set([p for p in blv_matches if "nha-dai" not in p.lower()]))
        
        if not final_blv_paths:
            # Nếu không quét được link cụ thể, thử tìm theo cấu trúc tên BLV chung
            # (Phòng trường hợp web đổi cấu trúc link)
            final_blv_paths = re.findall(r'href="([^"]*(?:blv|binh-luan)[^"]*)"', home_text)
            final_blv_paths = list(set([p for p in final_blv_paths if "nha-dai" not in p.lower()]))

        for path in final_blv_paths:
            url = 'https://bunchatv4.net' + path if path.startswith('/') else path
            # Lấy tên BLV từ đường dẫn để đặt tên kênh
            blv_name = path.split('/')[-1].replace('-', ' ').title()
            
            try:
                detail_res = requests.get(url, headers=headers, timeout=10)
                # Tìm link .m3u8 trong trang chi tiết
                stream_links = re.findall(r'(https?://[\w\.-]+[:\d]*/[\w\.-/]+\.m3u8[^\s"\'<>]*)', detail_res.text)
                
                if stream_links:
                    final_link = stream_links[0].replace('\\', '')
                    m3u_content += f'#EXTINF:-1, [Royx] {blv_name}\n{final_link}\n'
            except:
                continue

        # Luôn tạo file kể cả khi trống để tránh lỗi 128
        if m3u_content == '#EXTM3U\n':
            m3u_content += '#EXTINF:-1, Dang cho cac BLV len song...\nhttps://127.0.0.1/wait.m3u8'
            
        with open('live.m3u', 'w', encoding='utf-8') as f:
            f.write(m3u_content)
            
    except Exception as e:
        with open('live.m3u', 'w', encoding='utf-8') as f:
            f.write(f'#EXTM3U\n#EXTINF:-1, Loi ket noi: {str(e)}\nhttps://127.0.0.1/error.m3u8')

if __name__ == "__main__":
    grab_all_blv() # Phải gọi đúng tên hàm đã đặt ở trên đầu file
    
