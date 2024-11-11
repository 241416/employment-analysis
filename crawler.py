import random

from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup
import pandas as pd

def get_cookie(url,cookie):
    #1. 打开浏览器
    driver = webdriver.Chrome()
    #2. 进入网页
    driver.get(url)
    #3. 进入网页之后，手动点击登录页码快速登录进去
    time.sleep(20)
    #4.在15s之内登录，获取所有cookie信息(返回是字典)
    dictCookies = driver.get_cookies()
    #5.是将dict转化成str格式
    jsonCookies = json.dumps(dictCookies)
    # 登录完成后,自动创建一个boss直聘.json的文件，将cookies保存到该环境根目录下
    with open(cookie, "w") as fp:
        fp.write(jsonCookies)
        print('cookies保存成功！')
# url='https://www.zhipin.com/web/geek/job-recommend'
# get_cookie(url,cookie='boss直聘.json')

def get_text(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(6)
    boss_text = driver.page_source
    try:
        soup = BeautifulSoup(boss_text, 'html.parser')
        content = soup.find(class_='job-sec-text').text
        job = soup.find('h1').text
        salary = soup.find(class_='salary').text
        experience = soup.find(class_='text-experiece').text
        degree = soup.find(class_='text-degree').text
        company = soup.find(class_='sider-company')
        company_name = company.find(class_='company-info').text
        company_name = company_name.strip()
        company_others = company.find_all('p')
        company_stage = company_others[1].text
        company_scale = company_others[2].text
        company_type = company_others[3].text
    except:
        time.sleep(10)
        try:
            soup = BeautifulSoup(boss_text, 'html.parser')
            content = soup.find(class_='job-sec-text').text
            job = soup.find('h1').text
            salary = soup.find(class_='salary').text
            experience = soup.find(class_='text-experiece').text
            degree = soup.find(class_='text-degree').text
            company_name, company_stage, company_type, company_scale = 'None', 'None', 'None', 'None'
            print(content, job)
        except:
            content,job,salary,experience,degree,company_name,company_stage,company_type,company_scale = 'None','None','None','None','None','None','None','None','None'

    driver.quit()
    return content,job,salary,experience,degree,company_name,company_stage,company_type,company_scale

details = []
#这里最后改成10
job_list = []
detail_list = []
salary_list =[]
experience_list = []
degree_list = []
co_name_list = []
co_stage_list = []
co_scale_list = []
co_type_list = []

# 这里的地址和其他东西都是可以更新的,'101020100','101280600'
#,'营销','销售','供应链','编辑','客服','产品'
#管培生、项目管理、咨询顾问，人力资源、行政、法务

jobtype=['广告','公关','物流','文科教师']
for job in jobtype:
    boss = webdriver.Chrome()
    for i in range(1,4):
        try:
            url = f'https://www.zhipin.com/web/geek/job?query={job}&city=101010100&page={i}'
            boss.get(url)
        except:
            time.sleep(20)
            url = f'https://www.zhipin.com/web/geek/job?query={job}&city=101010100&page={i}'
            boss.get(url)
        # 2.注入cookie
        with open(r"boss直聘.json", "r") as fp:
            jsonCookies = fp.read()
        # 3. 将 JSON 格式的 Cookie 转换为字典
        cookies = json.loads(jsonCookies)
        # 4.添加 Cookie 到 WebDriver 对象
        for cookie in cookies:
            boss.add_cookie(cookie)
        # 5.进入网页等待6s加载，然后获取源代码
        boss.get(url)
        time.sleep(random.randint(3,5))
        boss_text = boss.page_source
        # 1.将源代码加载进beatifulsoup
        soup = BeautifulSoup(boss_text, 'html.parser')
        # 2.查找所有 class="job-card-left" 的元素
        job_card_left_elements = soup.find_all(class_='job-card-left')
        # 遍历每个元素，获取 <a> 标签的 href 链接
        for element in job_card_left_elements:
            href = element['href']
            full_link = 'https://www.zhipin.com' + href
            details.append(full_link)
            time.sleep(random.randint(3,5))
            content,job,salary,experience,degree,company_name,company_stage,company_type,company_scale= get_text(full_link)
            job_list.append(job)
            detail_list.append(content)
            salary_list.append(salary)
            experience_list.append(experience)
            degree_list.append(degree)
            co_name_list.append(company_name)
            co_type_list.append(company_type)
            co_scale_list.append(company_scale)
            co_stage_list.append(company_stage)
    boss.quit()

data=pd.DataFrame()
data['job'] = job_list
data['detail'] = detail_list
data['工资'] = salary_list
data['经验要求']= experience_list
data['学历']=degree_list
data['公司名称']=co_name_list
data['公司阶段']=co_stage_list
data['公司规模']=co_scale_list
data['公司领域']= co_type_list
# 应用到 DataFrame 的每个字符串元素
def remove_illegal_characters(s):
    # 移除或替换控制字符
    return ''.join([char for char in s if char.isprintable()])
for col in data.columns:
    if data[col].dtype == object:  # 仅处理字符串类型的列
        data[col] = data[col].apply(remove_illegal_characters)
data.to_excel('boss_3.xlsx',index=False)












