from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from password import PW
import random

HOMEWORK_PATH = "D:\\Document\\Study\\研二上_电路助教\\buaa_spoc_automation\\data\\第一次作业"
serial = "1"
A_socres = [100,99,98,97,96]
B_socres = [90,91,92,93,94,95]
C_socres = [80,81,82,83,84,85,86,87,88,89]


browser = webdriver.Chrome()

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
dict = ["序号","学号","姓名","状态","作答时间","迟交状态","批阅状态","批阅时间","分数","操作"]
for student in student_list:
    
    student_state_ele ={}
    student_state = {}
    time.sleep(1)
    student = student.find_elements(By.TAG_NAME,"td")
    
    for i in range(len(student)):
        student_state_ele[dict[i]] = student[i]
    
    for key in student_state_ele:
        if key != "操作":
           student_state[key] = student_state_ele[key].find_element(By.TAG_NAME,"span").text

    student_result = homework_state.loc[int(student_state['学号'])]
    if student_state['状态']=='已提交':
        time.sleep(1)
        review_button_ele = student_state_ele["操作"].find_elements(By.TAG_NAME,"button")[0]
        reject_button_ele = student_state_ele["操作"].find_elements(By.TAG_NAME,"button")[1]


        if student_result["评级"]=="A":
            

            if isinstance(student_result['评语'],str):
                pass
            else:
                review_button_ele.click()
                
                handles = browser.window_handles
                browser.switch_to.window(handles[-1])
                
                # 分数
                score_input_ele = browser.find_elements(By.CLASS_NAME,"ivu-input")[1]
                score_input_ele.send_keys(random.choice(A_socres))
                
                # 上传文件                
                upload_button_ele = browser.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[2]/form/div/div[4]/div/div/button")
                upload_button_ele.click()                 

                input_ele = browser.find_element(By.CLASS_NAME,"uploader-btn").find_element(By.TAG_NAME,"input")
                
                file_path = os.path.join(HOMEWORK_PATH,"批改后",serial+"-"+student_state["学号"]+"-"+student_result["姓名"]+".pdf")
                input_ele.send_keys(file_path)
                time.sleep(1)
                browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[3]/div/button").click()
                # 上传评语
                # 切换窗口
                # iframe = browser.find_element(By.TAG_NAME,"iframe")
                # browser.switch_to.frame(iframe)
                # body_ele = browser.find_element(By.ID,"tinymce")
                # text_ele = body_ele.find_element(By.TAG_NAME,'p')
                # text_ele.send_keys("sadfafd")
                # browser.switch_to.default_content()

                # 点击确认
                browser.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/button[2]").click()
                
            
        elif student_result["评级"]=="B":
            if isinstance(student_result['评语'],str):
                pass
            else:
                review_button_ele.click()
                
                handles = browser.window_handles
                browser.switch_to.window(handles[-1])
                
                # 分数
                score_input_ele = browser.find_elements(By.CLASS_NAME,"ivu-input")[1]
                score_input_ele.send_keys(random.choice(A_socres))
                
                # 上传文件                
                upload_button_ele = browser.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[2]/form/div/div[4]/div/div/button")
                upload_button_ele.click()                 

                input_ele = browser.find_element(By.CLASS_NAME,"uploader-btn").find_element(By.TAG_NAME,"input")
                
                file_path = os.path.join(HOMEWORK_PATH,"批改后",serial+"-"+student_state["学号"]+"-"+student_result["姓名"]+".pdf")
                input_ele.send_keys(file_path)
                time.sleep(5)
                browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[3]/div/button").click()
                # 上传评语
                # 切换窗口
                # iframe = browser.find_element(By.TAG_NAME,"iframe")
                # browser.switch_to.frame(iframe)
                # body_ele = browser.find_element(By.ID,"tinymce")
                # text_ele = body_ele.find_element(By.TAG_NAME,'p')
                # text_ele.send_keys("sadfafd")
                # browser.switch_to.default_content()

                # 点击取消
                browser.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/button[1]")            
        elif student_result["评级"]=="C":
            if isinstance(student_result['评语'],str):
                pass
            else:
                review_button_ele.click()
                
                handles = browser.window_handles
                browser.switch_to.window(handles[-1])
                
                # 分数
                score_input_ele = browser.find_elements(By.CLASS_NAME,"ivu-input")[1]
                score_input_ele.send_keys(random.choice(A_socres))
                
                # 上传文件                
                upload_button_ele = browser.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[2]/form/div/div[4]/div/div/button")
                upload_button_ele.click()                 

                input_ele = browser.find_element(By.CLASS_NAME,"uploader-btn").find_element(By.TAG_NAME,"input")
                
                file_path = os.path.join(HOMEWORK_PATH,"批改后",serial+"-"+student_state["学号"]+"-"+student_result["姓名"]+".pdf")
                input_ele.send_keys(file_path)
                time.sleep(5)
                browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[3]/div/button").click()
                # 上传评语
                # 切换窗口
                # iframe = browser.find_element(By.TAG_NAME,"iframe")
                # browser.switch_to.frame(iframe)
                # body_ele = browser.find_element(By.ID,"tinymce")
                # text_ele = body_ele.find_element(By.TAG_NAME,'p')
                # text_ele.send_keys("sadfafd")
                # browser.switch_to.default_content()

                # 点击取消
                browser.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/button[1]")
        elif student_result["评级"]=="D":
            reject_button_ele.click()
        print(student_result["姓名"],"is ok")
    print(student_state)

   
    # print(student.text)



time.sleep(100)

#app > div > div > div > div:nth-child(2) > form > div > div
