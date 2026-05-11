import requests
import re
import json

def get_rio_link():
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
        'Referer': 'https://bunchatv4.net/',
    }
    
    try:
        # 1. Truy cập trang chủ để tìm ID trận đấu có BLV Rio
        home_res = requests.get('https://bunchatv4.net/', headers=headers, timeout=10)
        # Tìm link trận đấu của Rio (Ví dụ: /truoc-tran/vietnam-u17-women-vs-australia-women-u17-...)
        match_path = re.findall(r'href="([^"]+Rio[^"]+)"', home_res.text)
        
        if not match_path:
            # Nếu không tìm thấy bằng tên, tìm link trận đấu diễn ra lúc 14:00
            match_path = re.findall(r'href="(/truoc-tran/[^"]+)"', home_res.text)

        if match_path:
            target_url = 'https://bunchatv4.net' + match_path[0]
            print(f"Dang vao tran: {target_url}")
            
            # 2. Vao trang tran dau de lay link iframe hoac link m3u8 truc tiep
            detail_res = requests.get(target_url, headers=headers, timeout=10)
            
            # Tim link m3u8 trong script hoac data-link
            m3u8_links = re.findall(r'(https?://[\w\.-]+[:\d]*/[\w\.-/]+\.m3u8[^\s"\'<>]*)', detail_res.text)
            
            if m3u8_links:
                final_link = m3u8_links[0].replace('\\', '')
                # Ghi vao file live.m3u
                with open('live.m3u', 'w', encoding='utf-8') as f:
                    f.write('#EXTM3U\n')
                    f.write(f'#EXTINF:-1, [Royx] BLV RIO - LIVE\n{final_link}')
                return f"Thanh cong: {final_link}"
                
        return "Chua tim thay link Live cua Rio"
    except Exception as e:
        return f"Loi roi: {e}"

if __name__ == "__main__":
    result = get_rio_link()
    print(result)
