import allure
from pages.example_page import ExamplePage

@allure.suite("메인")
@allure.title("메인 페이지 로딩 확인")
@allure.description("웹사이트가 정상적으로 로딩되고, 특정 텍스트나 요소가 페이지에 존재하는지 확인합니다.")
def test_example(page):

    example_page = ExamplePage(page)

    with allure.step("페이지 타이틀 확인"):
        title = example_page.get_title()
        print(f"Page Title: {title}")
        assert "예상되는 타이틀" in title, "페이지 타이틀이 일치하지 않습니다."

    with allure.step("특정 텍스트 존재 여부 확인"):
        content = page.content()
        assert "로그인" in content or "회원가입" in content, "로그인/회원가입 텍스트가 없습니다."

    with allure.step("버튼 요소 확인"):
        assert example_page.has_button(), "버튼 요소가 존재하지 않습니다."

    with allure.step("페이지 타이틀 검사"):
        assert "예상 타이틀" in page.title()

    with allure.step("로그인 버튼 클릭"):
        example_page.click_login_button()