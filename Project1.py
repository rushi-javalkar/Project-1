import action as action
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Project:
    def __init__(self,url):
        self.url=url
        self.driver = webdriver.Chrome("C:\\Users\\DELL\\PycharmProjects\\pythonProject2\\selenium driver\\chromedriver")
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

    def Login(self,username,password):
        #login using username and password
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(username)
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(password)
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(5)

    def Create_new_Employee(self,F_name,M_name,L_name,):
        # Navigate to PIM and create a new employee
        self.driver.find_element(By.XPATH,value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,value="//a[normalize-space()='Add Employee']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//input[@placeholder='First Name']").send_keys(F_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@placeholder='Middle Name']").send_keys(M_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@placeholder='Last Name']").send_keys(L_name)
        time.sleep(2)

        self.driver.find_element(By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(8)

    ''' # if we need to add Create_login_details
    def Create_login_details(self,E_Username, E_Password):
        self.driver.find_element(By.XPATH,value="//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

        self.driver.find_element(By.XPATH,value="(//input[@class='oxd-input oxd-input--active'])[3]").send_keys(E_Username)
        self.driver.find_element(By.XPATH,value="//label[normalize-space()='Enabled']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']").click()

        self.driver.find_element(By.XPATH,value="(//input[@type='password'])[1]").send_keys(E_Password)

        self.driver.find_element(By.XPATH,value="(//input[@type='password'])[2]").send_keys(E_Password)
        self.driver.find_element(By.XPATH,value="//button[@type='submit']").click()'''



        # Navigate to Admin section
    def create_user_Admin(self,employee_name,E_Username,E_Password):
        admin_section=self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//button[normalize-space()='Add']").click()
        time.sleep(4)

        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').click()
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(employee_name)
        listbox_1 = self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]')

        WebDriverWait(self.driver, 10).until(EC.visibility_of(listbox_1))

        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(listbox_1).click().perform()

        time.sleep(5)
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').click()
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys(E_Username)
        time.sleep(2)

        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').click()
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys(E_Password)
        time.sleep(2)

        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').click()
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys(E_Password)
        time.sleep(2)

        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
        statusListBox = self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of(statusListBox))
        action.move_to_element(statusListBox)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(2)

        userRole = self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')
        userRole.click()
        userRoleListBox1 = self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of(userRoleListBox1))

        userRoleListBox1content = self.driver.find_elements(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]/div')
        for i in userRoleListBox1content:
            print(i.text + "**")
            print(i.tag_name)
        print(len(userRoleListBox1content))

        action.move_to_element(userRoleListBox1)
        time.sleep(10)

        if (UserRole == "ESS"):
            action.move_to_element(userRoleListBox1content[2]).click().perform()
            print("ESS")
        elif (UserRole == "Admin"):
            action.move_to_element(userRoleListBox1content[1]).click().perform()
            print("Admin")
        time.sleep(2)

        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
        time.sleep(5)



    def Search_using_Admin(self, username, employee_name, UserRole):
        action = ActionChains(self.driver)
        time.sleep(3)

        WebDriverWait(self.driver,10).until(EC.visibility_of(self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')))
        self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').click()
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys(E_Username)
        time.sleep(2)

        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').click()
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').send_keys(employee_name)


        EmployeenameListbox=self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(EmployeenameListbox))
        time.sleep(2)
        action.move_to_element(EmployeenameListbox)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(2)

        contentsofemployeelistbox = self.driver.find_elements(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
        print(contentsofemployeelistbox)
        time.sleep(2)

        self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        userRoleList = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(userRoleList))

        userRoleListcontent = self.driver.find_elements(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div')

        for i in userRoleListcontent:
            print(i.text+"**")
            print(i.tag_name)
        print(len(userRoleListcontent))

        action.move_to_element(userRoleList)
        if UserRole == "Admin":
            action.move_to_element(userRoleListcontent[1]).click().perform()
            print("Admin")
        elif UserRole == "ESS":
            action.move_to_element(userRoleListcontent[2]).click().perform()
            print("ESS")
            time.sleep(2)


        self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').click()
        statuslistbox = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(statuslistbox))
        action.move_to_element(statuslistbox)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(2)


        self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(2)

        usname = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div').text
        usrole = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div').text
        empname= self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div').text
        empstatus= self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div').text

        print(usname+","+username)
        print(usrole+","+UserRole)
        print(empname+","+employee_name)
        print(empstatus)

        if usname == username and usrole == UserRole and empname == employee_name and empstatus == "Enabled":
            return True
        else:
            return False

    def logpout_of_the_Websight(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
        time.sleep(2)

        logoutlist = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul')
        WebDriverWait(self.driver,10).until(EC.visibility_of(logoutlist))
        action = ActionChains(self.driver)
        action.move_to_element(logoutlist)
        action.move_to_element(self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')).click().perform()
        time.sleep(10)


    def Login_using_created_Employee(self,E_Username,E_Password):
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(E_Username)
        time.sleep(2)
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(E_Password)
        time.sleep(2)
        self.driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(10)
        self.driver.quit()


url='https://opensource-demo.orangehrmlive.com/'
username = "Admin"
password = "admin123"
F_name= input("Enter the First name : ")
M_name=input("Enter the Middle name : ")
L_name=input("Enter the Last name : ")
UserRole = input("choose the user role(Admin / ESS) : ")
E_Username=input('Enter the Username [Should be at least 5 characters] : ')
E_Password=input('Enter the Password [For a strong password, please use a hard to guess combination of text with upper and lower case characters, symbols and numbers] : ')
employee_name = (F_name+" "+M_name+" "+L_name)
if M_name !="" and L_name !="":
    employee_name= F_name+" "+M_name+" "+L_name
elif M_name =="" and L_name !="":
    employee_name = F_name+" "+L_name
elif M_name !="" and L_name =="":
    employee_name = F_name+" "+M_name
elif M_name == "" and L_name == "":
    employee_name = F_name


p = Project(url)
p.Login(username,password)
p.Create_new_Employee(F_name,M_name,L_name)
#p.Create_login_details(E_Username,E_Password)
p.create_user_Admin(employee_name,E_Username,E_Password)
p.Search_using_Admin(E_Username,employee_name,UserRole)
p.logpout_of_the_Websight()
p.Login_using_created_Employee(E_Username,E_Password)