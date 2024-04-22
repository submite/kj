import requests

from lxml import etree

# 定义请求头

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}

# 登陆页面

login_url = 'https://twitter.com/login'

# 获取登陆页面

response = requests.get(login_url, headers=headers)

# 获取登陆页面的html

html = etree.HTML(response.text)

# 获取authenticity_token

authenticity_token = html.xpath('//input[@name="authenticity_token"]/@value')[0]

# 登陆信息

data = {

    'session[username_or_email]': '你的用户名',

    'session[password]': '你的密码',

    'authenticity_token': authenticity_token

}

# 发送登陆请求

response = requests.post(login_url, headers=headers, data=data)

# 打印登陆状态

print(response.status_code)