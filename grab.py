import requests
import re

def grab_all():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    m3u_content = '#EXTM3U\n'
    found = False
    
    try:
        home = requests.get('https://bunchatv4.net/', headers=headers, timeout=10).text
        # Tìm tất cả link m3u8 có trong trang chủ
        links = re.findall(r'https?://[\w\.-]+[:\d]*/[\w\.-/]+\.m3u8[^\s"\'<>]*', home)
        
        if links:
            for i, link in enumerate(links[:5]): # Lấy tạm 5 link đầu tiên thấy được
                m3u_content += f'#EXTINF:-1, [Royx] Kenh Live {i+1}\n{link.replace("\\", "")}\n'
            found = True
        
        # Nếu vẫn không thấy, ép nó tạo file trắng để Workflow không lỗi
        if not found:
            m3u_content += '#EXTINF:-1, Dang cho BLV Rio len song...\nhttps://google.com'
            
        with open('live.m3u', 'w', encoding='utf-8') as f:
            f.write(m3u_content)
            
    except Exception as e:
        with open('live.m3u', 'w') as f:
            f.write('#EXTM3U\n#EXTINF:-1, Loi Script\nhttps://google.com')

if __name__ == "__main__":
    grab_all()
                return f"Thanh cong: {final_link}"
                
        return "Chua tim thay link Live cua Rio"
    except Exception as e:
        return f"Loi roi: {e}"

if __name__ == "__main__":
    result = get_rio_link()
    print(result)
