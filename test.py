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
time.sleep(2)
# 点击我是助教
header_element = browser.find_element(By.CLASS_NAME,"header-nav-list")
a_element_list = header_element.find_elements(By.TAG_NAME,"a")
a_element_list[2].click()


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
    student_state_ele ={}
    student_state = {}
    student = student.find_elements(By.TAG_NAME,"td")
    
    for i in range(len(student)):
        student_state_ele[dict[i]] = student[i]
    
    for key in student_state_ele:
        if key != "操作":
           student_state[key] = student_state_ele[key].find_element(By.TAG_NAME,"span").text
    review_button_ele = student_state_ele["操作"].find_elements(By.TAG_NAME,"button")[0]
    reject_button_ele = student_state_ele["操作"].find_elements(By.TAG_NAME,"button")[1]

    print(student_state)

   
    # print(student.text)



time.sleep(100)

#app > div > div > div > div:nth-child(2) > form > div > div
