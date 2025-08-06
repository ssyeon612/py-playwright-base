from pages.base_page import BasePage

class ExamplePage(BasePage):

    def get_title(self) -> str:
        """페이지 타이틀 확인"""
        return self.page.title()

    def has_text_in_content(self, *texts: str) -> bool:
        """페이지 HTML 전체에서 특정 텍스트 존재 여부 확인"""
        content = self.page.content()
        return any(text in content for text in texts)

    def has_button(self) -> bool:
        """버튼 요소 존재 여부 확인"""
        return self.page.locator("button").count() > 0

    def click_login_button(self):
        self.click_by_role("button", name="로그인")