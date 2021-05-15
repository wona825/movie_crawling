import time
import selenium
from selenium import webdriver

URL = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%81%ED%99%94+%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4+%EC%88%9C%EC%9C%84&oquery=%EC%98%81%ED%99%94&tqi=h59nWwprvN8ssdVAPksssssssNh-375589'
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

movie_table=driver.find_elements_by_class_name("mflick")
print(len(movie_table))
movie_title=driver.find_elements_by_class_name("name")
print(len(movie_title))
movie_information=driver.find_elements_by_class_name("sub_text")
print(len(movie_information))

movie_title_list=[]
number=0
for title in movie_title:
    title.text
    number+=1
    movie_title_list.append(str(number) +'등. ' + title.text)
print(movie_title_list)

movie_title_list=movie_title_list[:10]
print(movie_title_list)


driver.close()

import matplotlib.pyplot as plt
import matplotlib

x=[1,2,3,4,5,6,7,8,9,10,11]
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.title('상영영화 일간 박스오피스')
plt.xticks(x,movie_title_list,rotation='vertical')

plt.show()
