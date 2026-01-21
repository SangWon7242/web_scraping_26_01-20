# ==============================================================
# 6단계: 네이버 뉴스 스크래핑 (실전) �
# ==============================================================
# 
# 🎯 목표:
#    - 네이버 뉴스(IT/과학) 섹션의 헤드라인 뉴스 수집
#    - 제목, 내용 요약, 신문사, 링크 정보 가져오기
#    - 엑셀 파일로 저장하기
#
# ==============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# --------------------------------------------------------------
# 🌐 1. 웹사이트 접속 (User-Agent 설정 필수!)
# --------------------------------------------------------------
url = "https://news.naver.com/section/105"  # IT/과학 뉴스

# 🚨 중요: 네이버 같은 대형 포털은 로봇(프로그램) 접속을 막을 수 있습니다.
# "나는 로봇이 아니라 브라우저야!"라고 알려주기 위해 User-Agent 정보를 함께 보냅니다.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"🌐 네이버 뉴스에 접속 중... ({url})")
response = requests.get(url, headers=headers)

# 접속 확인
if response.status_code != 200:
    print(f"❌ 접속 실패! 상태 코드: {response.status_code}")
    exit()

# --------------------------------------------------------------
# 🥣 2. HTML 분석 준비
# --------------------------------------------------------------
soup = BeautifulSoup(response.text, "html.parser")

# --------------------------------------------------------------
# � 3. 뉴스 데이터 찾기
# --------------------------------------------------------------
print("🔍 뉴스를 찾고 있습니다...")

# 데이터를 담을 리스트
news_list = []

# 네이버 뉴스 리스트 아이템 찾기
# 사용자가 제공한 힌트: <li class="sa_item _SECTION_HEADLINE">
news_items = soup.select("li.sa_item")

print(f"총 {len(news_items)}개의 뉴스를 찾았습니다.")

for item in news_items:
    try:
        # 1) 뉴스 제목 (strong class="sa_text_strong")
        title_tag = item.select_one("strong.sa_text_strong")
        if not title_tag: continue  # 제목이 없으면 건너뜀
        title = title_tag.text.strip()

        # 2) 뉴스 내용 요약 (div class="sa_text_lede")
        summary_tag = item.select_one("div.sa_text_lede")
        summary = summary_tag.text.strip() if summary_tag else "요약 없음"

        # 3) 신문사 (div class="sa_text_press")
        press_tag = item.select_one("div.sa_text_press")
        press = press_tag.text.strip() if press_tag else "알 수 없음"

        # 4) 뉴스 링크 (a class="sa_text_title")의 href 속성
        link_tag = item.select_one("a.sa_text_title")
        link = link_tag["href"] if link_tag else ""

        # 딕셔너리로 묶기
        news_data = {
            "뉴스 제목": title,
            "뉴스 내용": summary,
            "신문사": press,
            "링크": link
        }
        
        # 리스트에 추가
        news_list.append(news_data)
        
        # 확인용 출력 (너무 많으면 주석 처리)
        # print(f"- {title} ({press})")

    except Exception as e:
        print(f"⚠️ 에러 발생: {e}")
        continue

print(f"✅ 수집 완료: {len(news_list)}개")

# --------------------------------------------------------------
# � 4. 엑셀 파일로 저장하기
# --------------------------------------------------------------
# 오늘 날짜 구하기
today = datetime.now()
date_str = today.strftime("%Y_%m_%d")

# 파일 이름: naver_news_2026_01_21.xlsx
file_name = f"naver_news_{date_str}.xlsx"

print(f"💾 엑셀 파일로 저장 중... ({file_name})")

# 데이터프레임 생성 및 저장
df = pd.DataFrame(news_list)
df.to_excel(file_name, index=False)

print("🎉 저장 완료!")
