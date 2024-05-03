#Tool View
import os
try:
    import requests,colorama,prettytable,terminaltables
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")
    os.system("pip install terminaltables")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import random
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from prettytable import PrettyTable
from colorama import Fore, Style
from terminaltables import SingleTable
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
import shutil
from string import ascii_letters, digits
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
os.system("cls" if os.name == "nt" else "clear")
ToolView_RVO = r'''

     ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗              
     ██║   ██║██║██╔══██╗██║   ██║██╔════╝              
     ██║   ██║██║██████╔╝██║   ██║███████╗              
     ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║              
      ╚████╔╝ ██║██║  ██║╚██████╔╝███████║              
       ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝              
           Tool By: Ra Tool View   

  '''
class ToolView:
    def __init__(self):
        self.base_url = 'https://zefoy.com/'
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        self.session = requests.Session()
        self.captcha_1 = None
        self.captcha_ = {}
        self.service = 'Views'
        self.video_key = None
        self.services = {}
        self.services_ids = {}
        self.services_status = {}
        self.url = 'None'
        self.text = 'VIEWTIKTOK'
        print("\n\033[36m Vui Lòng Lấy Url Link Video Tik Tok Từ \033[31mChrome\033[36m\n Ví Dụ:\n\033[32m    https://www.tiktok.com/@(video_id)/video/(video_id)\n    https://www.tiktok.com/@kietminh18/video/7363268553245609223?_t=8lzENn3f6Yq&_r=1\033[0m\n")
        url1=input(Colorate.Horizontal(Colors.green_to_white, f" Vui Lòng Nhập URL LINK Video Của Bạn Cần Buff View: "))
        self.url=url1
        os.system("cls" if os.name == "nt" else "clear")
    def _videoInfo(self):
        headers = {
            "authority": "tiktok.livecounts.io",
            "Origin": "https://livecounts.io",
            "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }

        r = self.session.get(f'https://tiktok.livecounts.io/video/stats/{self.url.rsplit("/", 1)[-1]}', headers=headers)
        if r.json()['success']:
            return r.json()['viewCount'], r.json()['likeCount'], r.json()['commentCount'], r.json()['shareCount']
        else:
            self._videoInfo()

    def info_video(self):
        video_info = self._videoInfo()
        if video_info:
            print(Colorate.Horizontal(Colors.green_to_white, f"""
📊THÔNG TIN VIDEO
    | Video Total Views: {video_info[0]}
    | Video Total Likes: {video_info[1]}
    | Video Total Comments: {video_info[2]}
    | Video Total Shares: {video_info[3]}
"""))
    def view_vd(self):
        video_info = self._videoInfo()
        if video_info:
            print(Colorate.Horizontal(Colors.green_to_white, f""" 
 Video Total Views: {video_info[0]}
"""))
    def get_captcha(self):
        if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com')
        request = self.session.get(self.base_url, headers=self.headers)
        if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

        try:
            for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

            self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
            captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
            request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
            open('captcha.png', 'wb').write(request.content)
            print(Colorate.Horizontal(Colors.blue_to_red, f' Đang Check Capcha View'))
            return False
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_blue, f" Check Capcha View Thất Bại: {e}"))
            time.sleep(2)
            self.get_captcha()

    def send_captcha(self, new_session = False):
        if new_session: self.session = requests.Session(); os.remove('session'); time.sleep(2)
        if self.get_captcha(): print(Colorate.Horizontal(Colors.red_to_blue, f' Đang Kêt Nối Đến Session Ra Official Virus'));return (True, 'The session already exists')
        captcha_solve = self.solve_captcha('captcha.png')[1]
        self.captcha_[self.captcha_1] = captcha_solve
        request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

        if 'Enter Video URL' in request.text: 
            print(Colorate.Horizontal(Colors.green_to_white, f' Session Ra Official Virus Đã Được Tạo'))
            open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
            print(Colorate.Horizontal(Colors.green_to_white, f" Check Capcha View Thành Công: {captcha_solve}"))
            self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
            return (True,captcha_solve)
        else: return (False,captcha_solve)

    def solve_captcha(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
        if path_to_file: task = path_to_file
        else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
        request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,'rb')}).json()
        solved_text = request['ParsedResults'][0]['ParsedText']
        for x in delete_tag: solved_text = solved_text.replace(x,'')
        return (True, solved_text)

    def get_status_services(self):
        request = self.session.get(self.base_url, headers=self.headers).text
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
        for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
        return (self.services, self.services_status)
        
    def get_table(self, i=1):
        table_data = [["ID", "DỊCH VỤ", "Status"]]
        while True:
            if len(self.get_status_services()[0]) > 1:
                break
            else:
                print('Cant get services, retrying...')
                self.send_captcha()
                time.sleep(2)

        for service in self.services:
            status = self.services[service]
            if 'ago updated' in status:
                status_color = Fore.GREEN
            else:
                status_color = Fore.RED

            table_data.append([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{status_color}{status}{Fore.RESET}"])
            i += 1

        active_services = sum(1 for status in self.services.values() if 'ago updated' in status)
        table_data[0][0] = f"{Fore.YELLOW}{table_data[0][0]}{Fore.RESET}"
        table_data[0][1] = f"{Fore.YELLOW}{table_data[0][1]}{Fore.RESET}"
        table_data[0][2] = f"{Fore.YELLOW}{table_data[0][2]}{Fore.RESET}"
        table = SingleTable(table_data, title=f"{Fore.YELLOW}{Fore.RESET}")
        table.inner_row_border = True
        table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
        print(table.table)
    def find_video(self):
        if self.service is None: return (False, "You didn't choose the service")
        while True:
            if self.service not in self.services_ids: self.get_status_services(); time.sleep(1)
            request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
            try: self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
            except: time.sleep(3); continue
            if 'Session expired. Please re-login' in self.video_info:
                print('Phiên hết hạn. Đang đăng nhập lại...')
                self.send_captcha()
                return
            elif 'service is currently not working' in self.video_info:
                return (True, 'Dịch vụ hiện không hoạt động, hãy thử lại sau.')
            elif """onsubmit="showHideElements""" in self.video_info:
                self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
                return (True, request.text)
            elif 'Checking Timer...' in self.video_info:
                try: 
                    t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                    zyfoy = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                except: 
                    return (False,)
                if zyfoy==0:self.find_video()
                elif zyfoy >= 1000:
                    print(Colorate.Horizontal(Colors.red_to_white, f' THÔNG BÁO!!! IP CỦA BẠN ĐÃ BỊ BLOCK!'))
                _=time.time()
                _=time.time()
                while time.time()-2<_+zyfoy:
                    t-=1
                    print(Colorate.Horizontal(Colors.red_to_blue, f" Vui Lòng Chờ: {t} Giây ....."), end="\r")
                    time.sleep(1)
                continue
            elif 'Too many requests. Please slow' in self.video_info:
                time.sleep(3)
            else:
                print(self.video_info)

    def use_service(self):
        if self.find_video()[0] is False:
            return False
        self.token = "".join(random.choices(ascii_letters+digits, k=16))
        request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
        try:
            res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
        except:
            time.sleep(3)
            return ""
        if 'Session expired. Please re-login' in res:
            print('Phiên hết hạn. Đang đăng nhập lại...')
            self.send_captcha()
            return ""
        elif 'Too many requests. Please slow' in res:
            time.sleep(3)
        elif 'service is currently not working' in res:
            return ('Dịch vụ hiện không hoạt động, hãy thử lại sau.')
        else:
            print(" " + Colorate.Horizontal(Colors.green_to_white, res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0]), end=" ")
            self.view_vd()
    def get_video_info(self):
        request = self.session.get(f'https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition("/")[2]}',headers={'authority':'tiktok.livecounts.io','origin':'https://livecounts.io','user-agent':self.headers['user-agent']}).json()
        if 'viewCount' in request:
            return request
        else:
            return {'viewCount':0, 'likeCount':0,'commentCount':0,'shareCount':0}

    def get_video_id(self, url_ = None, set_url=True):
        if url_ is None:
            url_ = self.url
        if url_[-1] == '/':
            url_ = url_[:-1]
        url = urlparse(url_).path.rpartition('/')[2]
        if url.isdigit():
            self.url = url_
            return url_
        request = requests.get(f'https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}',headers={'origin': 'https://tokcount.com','authority': 'api.tokcount.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
        if request.text == '':
            print(Colorate.Horizontal(Colors.red_to_white, f' URL LINK Video Không Hợp Lệ'))
            return False
        else:
            json_ = request.json()
        if 'author' not in json_:
            print(Colorate.Horizontal(Colors.red_to_white, f'{self.url}| URL LINK VIdeo Không Hợp Lệ'))
            return False
        if set_url:
            self.url = f'https://www.tiktok.com/@{json_["author"]}/video/{json_["id"]}'
            print(f'Formated video url --> {self.url}')
        return request.text

    def check_config(self):
        while True:
            try: 
                last_url = self.url
                if last_url != self.url:
                    self.get_video_id()
            except Exception as e:
                print(e)
            time.sleep(4)

    def update_name(self):
        while True:
            try:
                ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
                video_info = self.get_video_info()
                self.text = f"Views: {video_info['viewCount']} "
            except:
                pass
            time.sleep(5)

    def select_service(self):
        while True:
            self.get_table()
            service_id = input(Colorate.Horizontal(Colors.red_to_purple, f" Nhập Số Của Dịch Vụ Bạn Muốn Chọn: "))
            if service_id.isdigit():
                service_id = int(service_id)
                if service_id in range(1, len(self.services) + 1):
                    services_list = list(self.services.keys())
                    self.service = services_list[service_id - 1]
                    break
                else:
                    print(f"{Fore.RED}Vui lòng nhập một số hợp lệ.{Fore.RESET}")
            else:
                print(f"{do} Vui Lòng Nhập Đúng Số Dịch Vụ")

    def run(self):
        self.select_service()
        while True:
            trang = "\033[1;37m"
            xanh_la = "\033[1;32m"
            xanh_duong = "\033[1;34m"
            do = "\033[1;31m"
            vang = "\033[1;33m"
            tim = "\033[1;35m"
            try:
                if 'Service is currently not working, try again later' in str(self.use_service()):
                    print(f'{do}[\033[1;33mDịch vụ hiện không hoạt động, hãy thử lại sau.')
                    time.sleep(5)
            except Exception as e:
                print(f'LỖI {e}');time.sleep(10)
                time.sleep(0)
	
if __name__ == "__main__":
    print(Colorate.Horizontal(Colors.red_to_blue, ToolView_RVO))
    ToolViewDz = ToolView()
    print(Colorate.Horizontal(Colors.red_to_blue, ToolView_RVO))
    ToolViewDz.info_video()
    threading.Thread(target=ToolViewDz.check_config).start()
    threading.Thread(target=ToolViewDz.update_name).start()
    ToolViewDz.send_captcha()
    ToolViewDz.run() 
