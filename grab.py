import requests
import re

def grab_all_blv():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://bunchatv4.net/'
    }
    m3u_content = '#EXTM3U\n'
    try:
        # Quét trang chủ
        home = requests.get('https://bunchatv4.net/', headers=headers, timeout=15).text
        # Tìm link BLV, bỏ qua nhà đài
        paths = re.findall(r'href="([^"]*binh-luan-vien/[^"]*)"', home)
        paths = list(set([p for p in paths if "nha-dai" not in p.lower()]))

        if not paths:
            m3u_content += '#EXTINF:-1, Dang cho cac BLV len song...\nhttps://127.0.0.1/wait.m3u8'
        else:
            for p in paths:
                url = 'https://bunchatv4.net' + p if p.startswith('/') else p
                name = p.split('/')[-1].replace('-', ' ').title()
                detail = requests.get(url, headers=headers, timeout=10).text
                streams = re.findall(r'(https?://[\w\.-]+[:\d]*/[\w\.-/]+\.m3u8[^\s"\'<>]*)', detail)
                if streams:
                    m3u_content += f'#EXTINF:-1, [Royx] {name}\n{streams[0].replace("\\", "")}\n'

        with open('live.m3u', 'w', encoding='utf-8') as f:
            f.write(m3u_content)
    except:
        with open('live.m3u', 'w') as f:
            f.write('#EXTM3U\n#EXTINF:-1, Dang ket noi...\nhttps://127.0.0.1/err.m3u8')

if __name__ == "__main__":
    grab_all_blv() # Nhớ là tên này phải giống tên hàm ở trên
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
    
