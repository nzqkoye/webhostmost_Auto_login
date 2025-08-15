import requests
import sys
import os

def main():
    login_url = 'https://client.webhostmost.com/dologin.php'
    data = {
        'username': os.getenv('ADMIN_USERNAME'),  # 从环境变量获取用户名
        'password': os.getenv('ADMIN_PASSWORD'),  # 从环境变量获取密码
        'language': 'english',
        'currency': '1',
        # 若需CSRF令牌，需先GET登录页面提取，添加如'token': 'fetch_if_needed'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        response = requests.post(login_url, data=data, headers=headers, allow_redirects=True)
        if response.status_code == 200 and 'clientarea.php' in response.url:
            print('登录成功！已重定向到客户端区域。')
        else:
            print(f'登录失败。状态码：{response.status_code}，响应：{response.text[:200]}')
            sys.exit(1)
    except Exception as e:
        print(f'登录时出错：{str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main()  
