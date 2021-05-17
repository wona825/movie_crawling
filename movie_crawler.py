import time
import selenium
from selenium import webdriver

URL = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%81%ED%99%94+%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4+%EC%88%9C%EC%9C%84&oquery=%EC%98%81%ED%99%94&tqi=h59nWwprvN8ssdVAPksssssssNh-375589'
driver = webdriver.Chrome(executable_path='C:/Users/82104/Desktop/chromedriver.exe')
driver.get(url=URL)

movie_table=driver.find_elements_by_class_name("mflick")
print(len(movie_table))
movie_title=driver.find_elements_by_class_name("name")
print(len(movie_title))
movie_information=driver.find_elements_by_class_name("sub_text")
print(len(movie_information))

movie_title_list=[]
movie_information_list = []
number=0
for title in movie_title:
    title.text
    number+=1
    movie_title_list.append(str(number) +'등. ' + title.text)
print(movie_title_list)

for information in movie_information:
    information.text
    number+=1
    movie_information_list.append(information.text)
movie_information_list = movie_information_list[0:10]

for i in range(len(movie_information_list)):
    string = movie_information_list[i]
    if string[-2] == '만':
        string = string[0:len(string)-2]
        if len(string) == 3:
            string = string[0] + string[2]
            string = int(string) * 1000
        else :
            string = int(string) * 10000
    else :
        string = int(string[0] + string[2:5])
    movie_information_list[i] = string
print(movie_information_list)


movie_title_list=movie_title_list[:10]
print(movie_title_list)


driver.close()

import matplotlib.pyplot as plt
import matplotlib

x=[1,2,3,4,5,6,7,8,9,10]
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.title('상영영화 일간 박스오피스')
plt.xticks(x,movie_title_list,rotation='vertical')
plt.bar(x, movie_information_list)
plt.show()
