from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome driver 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 셀렉터 헬퍼
from selenium.webdriver.common.by import By

# Chrome 꺼짐방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")

# Chrome driver Manager를 통해 크롬 드라이버 자동 설치 > 최신 버전을 설치 > Service에 저장
service = Service(excutable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 이동하려는 해당 웹페이지 주소 할당
driver.get("https://class101.net/ko")
print(driver.title)

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
