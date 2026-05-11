import requests
import re

def go(): # Đặt tên cực ngắn là 'go'
    headers = {'User-Agent': 'Mozilla/5.0'}
    m3u = '#EXTM3U\n'
    try:
        home = requests.get('https://bunchatv4.net/', headers=headers).text
        links = re.findall(r'href="([^"]*binh-luan-vien/[^"]*)"', home)
        links = list(set([l for l in links if "nha-dai" not in l.lower()]))
        for l in links:
            url = 'https://bunchatv4.net' + l if l.startswith('/') else l
            name = l.split('/')[-1].replace('-', ' ').title()
            det = requests.get(url, headers=headers).text
            str_link = re.findall(r'(https?://[\w\.-]+[:\d]*/[\w\.-/]+\.m3u8[^\s"\'<>]*)', det)
            if str_link:
                m3u += f'#EXTINF:-1, [Royx] {name}\n{str_link[0].replace("\\", "")}\n'
    except: pass
    with open('live.m3u', 'w', encoding='utf-8') as f:
        f.write(m3u)

if __name__ == "__main__":
    go() # Dòng này phải gọi đúng cái tên 'go' ở trên
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
    
