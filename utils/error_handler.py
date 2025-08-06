# Playwright 테스트 실행 시 예외 처리 + 스크린샷 저장 및 Allure 첨부 모듈

import allure
from pathlib import Path
from datetime import datetime
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError


"""
테스트 단계 단위로 예외를 포착하고 Allure 리포트에 정보를 첨부하는 안전 실행 함수

Parameters:
    step_name (str): Allure 리포트에 표시할 단계명
    page (Page): Playwright의 페이지 객체 (스크린샷을 위해 필요)
    func (function): 실행할 함수 (예: lambda, click, fill 등)
    *args: func에 전달할 위치 인자
    **kwargs: func에 전달할 키워드 인자

Returns:
    func의 실행 결과

예외 발생 시:
    - 스크린샷을 찍어 allure에 첨부
    - 예외 메시지를 allure에 첨부
    - 테스트 실패 처리(assert False)
"""
def safe_run(step_name: str, page:Page, func, *args, **kwargs):
    try:
        with allure.step(step_name):
            return func(*args, **kwargs)
        
    except PlaywrightTimeoutError:
        _attach_screenshot(page, step_name)
        allure.attach(
            step_name, 
            name="TimeoutError 발생 단계", 
            attachment_type=allure.attachment_type.TEXT
            )
        assert False, f"[TimeoutError] {step_name}단계에서 타임아웃 발생"

    except Exception as e:
        _attach_screenshot(page, step_name)
        allure.attach(
            str(e), 
            name=f"{step_name} - 예외 메세지", 
            attachment_type=allure.attachment_type.TEXT
            )
        assert False, f"[Error] {step_name} 중 예외 발생: {e}"


"""
현재 페이지 상태의 스크린샷을 찍어 파일로 저장하고 Allure 리포트에 첨부

Parameters:
    page (Page): Playwright 페이지 객체
    step_name (str): 스크린샷 파일명 및 리포트에 사용될 이름
"""
def _attach_screenshot(page: Page, step_name: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_step_name = step_name.replace(" ", "_").replace("/", "_")
    screenshot_path = Path("screenshots") / f"{safe_step_name}_{timestamp}.png"

    # 스크린샷 디렉토리 생성
    Path("screenshots").mkdir(parents=True, exist_ok=True)

    # 스크린샷 저장
    page.screenshot(path=str(screenshot_path))

    # Allure 리포트에 스크린샷 첨부
    allure.attach.file(
        str(screenshot_path), 
        name=f"{step_name} 스크린샷", 
        attachment_type=allure.attachment_type.PNG
        )