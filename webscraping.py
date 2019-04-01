
from selenium import webdriver
from prettytable import PrettyTable
import  time
from selenium.webdriver.support.select import Select
import threading
table1 = PrettyTable()

def fun1():
    Count=input("Enter Country name :")
    Count=Count.title()

    #selection option from dropdown
    l1=["Canada","United States"]
    l2=['Any','Alberta' ,'British Columbia','Manitoba', 'New Brunswick', 'Newfoundland', 'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon']
    l3=['Any','Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado' ,'Connecticut' ,'Delaware' ,'District Of Columbia' , 'Florida' ,'Georgia' ,'Hawaii', 'Idaho', 'Illinois' ,'Indiana' ,'Lowa' ,'Kansas' ,'Kentucky', 'Louisiana' ]
    #while loop till  user enter valid option
    while Count not in l1:
        print("Enter Valid choice or choose from below option")
        print(l1)
        Count = input("Enter Country name :")
        Count = Count.title()


    provi=input("Enter Province name :")
    provi=provi.title()
    if Count== "Canada":
        while provi not in l2:
            print("Enter Valid choice or choose from below option")
            print(l2)
            provi = input("enter province name :")
            provi = provi.title()
    else:
        while provi not in l3:
            print(" enter valid choice")
            print(l3)
            provi = input("enter province name :")
            provi = provi.title()
        if provi=='District Of Columbia': #in dropdown text is not written in standard format ( small 'o' is used )
             provi='District of Columbia'

    driver = webdriver.Chrome()
    driver.get("https://obittree.com/obituary/list-obituaries.php")
    obj=Select(driver.find_element_by_name("Country"))
    obj.select_by_visible_text(Count)

    obj1=Select(driver.find_element_by_name("Province"))
    obj1.select_by_visible_text(provi)

    obj2=driver.find_element_by_class_name("obit-search-btn")
    obj2.click()


    SCROLL_PAUSE_TIME =4 # depends on internet speed
    last_height = driver.execute_script("return document.body.scrollHeight")
    #while loop for scrolling down to the page
    while True:

        # time.sleep(SCROLL_PAUSE_TIME)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2.5)
        # Calculate new scroll height and compare with last scroll height
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    post=driver.find_elements_by_class_name("obituary-item-name")


    post1=driver.find_elements_by_class_name("obituary-item-fhname")
    post2=driver.find_elements_by_class_name("obituary-item-dod")

    return post,post1,post2


time.sleep(1)
def fun2(*num1):

    for count, ele in enumerate(num1[1]):
        if num1[1][count].text!='':
            if num1[1][count].text != '':
                num1[0].append(num1[1][count].text)



if __name__ == "__main__":
    post1,post2,post3=fun1()
    ll1=[]
    l22=[]
    l33=[]
    l1 = [ll1,post1]
    l2 = [l22,post2]
    l3 = [l33,post3]
    # creating thread


    t1 = threading.Thread(target=fun2, args=(l1))
    t2 = threading.Thread(target=fun2, args=(l2))
    t3 = threading.Thread(target=fun2, args=(l3))


    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    t3.start()


    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    t3.join()
    table1.add_column("name", ll1)
    table1.add_column("DOB", l33)
    table1.add_column("Address", l22)

    if len(ll1) > 0:  # if record are Available
        print(table1)
    else:
        print(" No Record Available")

