import allure
from playwright.sync_api import Page
from handler import safe_run

@allure.title("메인 페이지 로딩 확인")
@allure.description("웹사이트가 정상적으로 로딩되고, 특정 텍스트나 요소가 페이지에 존재하는지 확인합니다.")
def test_main_page_loads(page: Page) -> None:
    with allure.step("페이지 타이틀 확인"):
        title = page.title()
        print(f"Page Title: {title}")
        assert "예상되는 타이틀" in title, "페이지 타이틀이 일치하지 않습니다."

    with allure.step("특정 텍스트 존재 여부 확인"):
        content = page.content()
        assert "로그인" in content or "회원가입" in content, "로그인/회원가입 텍스트가 없습니다."

    with allure.step("버튼 요소 확인"):
        button = page.locator("button")
        assert button.count() > 0, "버튼 요소가 존재하지 않습니다."

    with allure.step("페이지 타이틀 검사"):
        assert "예상 타이틀" in page.title()

    # 존재하지 않는 요소에 대해 일부러 예외 유도
    safe_run("로그인 버튼 클릭", page, lambda: page.get_by_role("button", name="로그인").click())