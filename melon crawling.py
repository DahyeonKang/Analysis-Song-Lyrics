import pandas as pd
from selenium import webdriver
import time


path = 'chromedriver_117.exe'
driver = webdriver.Chrome(path)

# 로그인
driver.get('http://www.melon.com')
time.sleep(2)
# driver.find_element_by_class_name('btn_login').click()
# time.sleep(1)
# driver.find_element_by_class_name('btn_gate.kakao').click()
# time.sleep(1)
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element_by_xpath('//*[@id="loginId--1"]').send_keys('kl1223k@daum.net')
# driver.find_element_by_xpath('//*[@id="password--2"]').send_keys('kl001223')
# driver.find_element_by_class_name('btn_g.highlight.submit').click()
# time.sleep(1)
# # 팝업창 닫기
# print(driver.window_handles)
# win = driver.window_handles
# driver.switch_to.window(win[0])
# time.sleep(1)


driver.get('https://www.melon.com/chart/search/index.htm')
time.sleep(1)
driver.find_element_by_class_name('tab03').click()  # 차트선택
time.sleep(1)
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[2]/span/label').click()  # 연대선택(8개)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[10]/span/label').click()  # 연도선택(연대마다 다름)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[2]/span/label').click()  # 국내종합
time.sleep(1)
driver.find_element_by_class_name('btn_b26').click()  # 검색
time.sleep(1)

data = pd.DataFrame(columns=['song', 'artist', 'genre', 'lyric'])

for i in range(0, 100):
    if i == 50:
        driver.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()
        time.sleep(1)
    try :
        more_info_list = driver.find_elements_by_css_selector('.btn.btn_icon_detail')
        more_info_list[i].click()
        time.sleep(1)

        # 제목 가져오기
        song = driver.find_element_by_css_selector('.song_name')
        # 가수 가져오기
        artist = driver.find_element_by_css_selector('.artist')
        # 장르 가져오기
        genre = driver.find_element_by_class_name('list')
        # 가사 가져오기
        lyric = driver.find_element_by_class_name('lyric')

        print(*[song.text, artist.text, genre.text.split('\n')[5], len(lyric.text)], sep='    ')
        data.loc[i] = [song.text, artist.text, genre.text.split('\n')[5], lyric.text]

        driver.back()
        time.sleep(1)
    except:
        pass

data.to_csv('lyric_2010.csv', index=False, encoding='utf-8')