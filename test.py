from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()

url = "https://sso.buaa.edu.cn/login?service=https%3A%2F%2Fspoc.buaa.edu.cn%2Fspoc%2FmoocMainIndex%2FspocWelcome"
browser.get(url)
# 登录spoc
browser.switch_to.frame("loginIframe")
browser.find_element(By.ID,"unPassword").send_keys("zy2203203")
browser.find_element(By.ID,"pwPassword").send_keys("BJydcs001")
browser.find_element(By.CLASS_NAME,"submit-btn").click()
# 点击我是助教
list = browser.find_element(By.TAG_NAME,"a").click()
list[3].click()

# 点击课程
course = browser.find_element(By.CLASS_NAME,"rdjx-wgl-btn")
course.find_elements(By.TAG_NAME,"span")[3].click()

# # 选择第几堂课
# week_list = browser.find_elements(By.CLASS_NAME,"ivu-collapse-item.ivu-collapse-item-active")
# week = week_list[0]

student_list = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody")
student_list = student_list.find_elements(By.TAG_NAME,"tr")

dict = ["序号","学号","姓名","状态","作答时间","迟交状态","批阅状态","批阅时间","分数","操作"]
for student in student_list:




time.sleep(100)

#app > div > div > div > div:nth-child(2) > form > div > div
