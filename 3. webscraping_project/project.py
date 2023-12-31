import re
import requests
from bs4 import BeautifulSoup



def create_soup(url):
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hJ6TTlprvToss5OKYWGssssstzs-249920"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup
    
def print_news(index, title, link):
    print("{}.{}".format(index+1, title))
    print(" (링크 : {})".format(link))


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hJ6TTlprvToss5OKYWGssssstzs-249920/"
    soup = create_soup(url)

    # 흐림, 어제보다 00 높아요
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재 00 (최저 00 / 최고 00)
    curr_temp = soup.find("span", attrs={"class":"blind"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text() #최저 온도
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text() #최고 온도
    #오전 강수확률 00 / 오후 강수확률 00
    morning_rain_rate = soup.find("span",attrs={"class":"rainfall"}).get_text().strip() #오전 강수확률
    afternoon_rain_rate = soup.find("span",attrs={"class":"rainfall"}).get_text().strip() #오후 강수확률
    
    #미세먼지 00ug /m 좋음
    #초미세먼지 00ug /m 좋음
    dust = soup.find("ul", attrs = {"class":"today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text() #미세먼지
    pm25 = dust.find_all("li")[1].get_text() #초미세먼지
    
    #출력
    print(cast)
    print("현재 {} (최저 {} 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()
    
    
def scrape_headline_news():
     print("[헤드라인 뉴스]")
     url = "https://media.naver.com/press/018"
     soup = create_soup(url)
     news_list = soup.find("ul", attrs = {"class":"press_news_list as_bottom"})
     for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
     print()
     



def scrape_it_news():
    print("[IT뉴스]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"cluster_list"}).find_all("li", limit=3) #3개까지만 가져오기
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용
            
        a_tag = news.find_all("a")[a_idx]    
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()
    
    
def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8 문장이 있다고 가정할 때, index 기준 4~7 까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8 문장이 있다고 가정할 때, index 기준 0~3 까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()



if __name__ == "__main__":
    scrape_weather() #오늘의 날씨 정보 가져오기
    scrape_headline_news() #헤드라인 뉴스 정보 가져오기
    scrape_it_news() #IT 뉴스 정보 가져오기
    scrape_english()