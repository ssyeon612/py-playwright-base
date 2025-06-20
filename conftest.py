import pytest
import pymysql
import allure
from pathlib import Path
from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from db import get_connection
from dotenv import load_dotenv
import os

load_dotenv()

# DB 연결 설정: 세션 단위
@pytest.fixture(scope='session')
def db_connection():
    conn = get_connection()
    yield conn
    conn.close()

# Playwright 인스턴스 초기화 (세션 단위)
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

# 브라우저 인스턴스 설정 (세션 단위)
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

# 테스트 결과 Hook 설정
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_"+ rep.when, rep)


# 테스트 단위 페이지 fixture
"""
매 테스트마다 새로운 브라우저 context와 페이지를 생성하고,
사이트 접속 및 팝업 닫기 동작까지 처리합니다.

테스트 실패 시 스크린샷을 찍어 Allure 리포트에 첨부합니다.
"""
@pytest.fixture(scope="function")
def page(request, browser):
    context = browser.new_context()
    url = os.getenv('URL') or ""

    page = context.new_page()
    page.goto(url)

    print(f'연결된 웹사이트 주소: {url}')

    yield page

    # 테스트 실패 시 스크린샷 저장 및 Allure 리포트에 첨부
    if request.node.rep_call.failed:
        screenshots_dir = Path('screenshots')
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        screenshots_path = screenshots_dir / f"{request.node.name}.png"

        # 스크린샷 저장
        page.screenshot(path=str(screenshots_path))

        # Allure 첨부
        allure.attach.file(
            str(screenshots_path),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    # context 닫기 (clean-up)
    context.close()

    