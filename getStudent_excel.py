from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from password import PW
browser = webdriver.Chrome()
HOMEWORK_PATH = "D:\\Document\\Study\\研二上_电路助教\\buaa_spoc_automation\\data\\第一次作业"
pw = PW()
url = "https://sso.buaa.edu.cn/login?service=https%3A%2F%2Fspoc.buaa.edu.cn%2Fspoc%2FmoocMainIndex%2FspocWelcome"
browser.get(url)
# 登录spoc
browser.switch_to.frame("loginIframe")
browser.find_element(By.ID,"unPassword").send_keys(pw.ID)
browser.find_element(By.ID,"pwPassword").send_keys(pw.password)
browser.find_element(By.CLASS_NAME,"submit-btn").click()

# 切换到新的窗口句柄
browser.implicitly_wait(10)
handles = browser.window_handles
browser.switch_to.window(handles[-1])

# 点击我是助教
header_element = browser.find_element(By.CLASS_NAME,"header-nav-list")
a_element_list = header_element.find_elements(By.TAG_NAME,"a")
a_element_list[2].click()
browser.implicitly_wait(10)

# 点击作业
course = browser.find_element(By.CLASS_NAME,"rdjx-wgl-btn")
course.find_elements(By.TAG_NAME,"span")[3].click()

# # 选择第几堂课
# week_list = browser.find_elements(By.CLASS_NAME,"ivu-collapse-item.ivu-collapse-item-active")
# week = week_list[0]

# 切换到新的窗口句柄
browser.implicitly_wait(10)
handles = browser.window_handles
browser.switch_to.window(handles[-1])

browser.implicitly_wait(10)
browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div").click()

student_list = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody")
student_list = student_list.find_elements(By.TAG_NAME,"tr")

homework_state = pd.read_excel(os.path.join(HOMEWORK_PATH,"作业情况.xlsx"),index_col="学号",header=0)
print(homework_state.head)
print("学生人数",len(student_list))
dict = ["序号","学号","姓名"]

student_group = []
for student in student_list:
    student_state_ele ={}
    student_state = {}
    
    student = student.find_elements(By.TAG_NAME,"td")
    
    for i in range(len(student)):
        student_state_ele[dict[i]] = student[i]
    a = []
    for key in student_state_ele:
        if key != "操作":
           student_state[key] = student_state_ele[key].find_element(By.TAG_NAME,"span").text
           a.append(student_state[key])

    student_group.append(a)
    

    print(student_state)

df = pd.DataFrame(student_group,columns=dict)
df.to_excel("output.xlsx",index=False)
    # print(student.text)



time.sleep(100)

#app > div > div > div > div:nth-child(2) > form > div > div
