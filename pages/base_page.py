from playwright.sync_api import Page
from playwright.sync_api import expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # ------------------------------
    # Locator 생성 메서드
    # ------------------------------

    def by_text(self, text: str, exact: bool = True):
        """텍스트로 요소 찾기"""
        return self.page.get_by_text(text, exact=exact)
    
    def by_role(self, role: str, name: str = None, exact: bool = True, **kwargs):
        """ARIA role로 요소 찾기"""
        if name:
            return self.page.get_by_role(role, name=name, exact=exact, **kwargs)
        return self.page.get_by_role(role, **kwargs)

    def by_placeholder(self, placeholder: str, exact: bool = True):
        """placeholder 속성으로 요소 찾기"""
        return self.page.get_by_placeholder(placeholder, exact=exact)

    def by_label(self, label: str, exact: bool = True):
        """label 텍스트로 요소 찾기"""
        return self.page.get_by_label(label, exact=exact)

    def by_alt_text(self, alt_text: str, exact: bool = True):
        """이미지 alt 속성으로 요소 찾기"""
        return self.page.get_by_alt_text(alt_text, exact=exact)

    def locator(self, selector: str, **kwargs):
        """CSS / XPath selector로 요소 찾기"""
        return self.page.locator(selector, **kwargs)
    
    # ------------------------------
    # Click 메서드
    # ------------------------------
    def click_by_text(self, text: str, exact: bool = True):
        """텍스트로 요소 찾아 클릭"""
        locator = self.by_text(text, exact=exact)
        expect(locator).to_be_visible()
        locator.click()

    def click_by_role(self, role: str, name: str = None, exact: bool = True):
        """role + name으로 요소 찾아 클릭"""
        locator = self.by_role(role, name=name, exact=exact)
        expect(locator).to_be_visible()
        locator.click()

    def click_by_alt_text(self, alt_text: str, exact: bool = True):
        """이미지 alt로 요소 찾아 클릭"""
        locator = self.by_alt_text(alt_text, exact=exact)
        expect(locator).to_be_visible()
        locator.click()

    def click_locator(self, selector: str, **kwargs):
        """CSS / XPath selector로 요소 찾아 클릭"""
        locator = self.locator(selector, **kwargs)
        expect(locator).to_be_visible()
        locator.click()

    # =========================================================
    # Input 메서드
    # =========================================================
    def fill_by_text(self, text_locator: str, value: str, exact: bool = True):
        """텍스트 기반 locator에 값 입력"""
        locator = self.by_text(text_locator, exact=exact)
        expect(locator).to_be_visible()
        locator.fill(value)

    def fill_by_role(self, role: str, value: str, name: str = None, exact: bool = True):
        """role + name 기반 locator에 값 입력"""
        locator = self.by_role(role, name=name, exact=exact)
        expect(locator).to_be_visible()
        locator.fill(value)

    def fill_by_placeholder(self, placeholder: str, value: str, exact: bool = True):
        """placeholder 기반 locator에 값 입력"""
        locator = self.by_placeholder(placeholder, exact=exact)
        expect(locator).to_be_visible()
        locator.fill(value)

    def fill_by_label(self, label: str, value: str, exact: bool = True):
        """label 기반 locator에 값 입력"""
        locator = self.by_label(label, exact=exact)
        expect(locator).to_be_visible()
        locator.fill(value)

    def fill_locator(self, selector: str, value: str):
        """CSS / XPath selector 기반 locator에 값 입력"""
        locator = self.locator(selector)
        expect(locator).to_be_visible()
        locator.fill(value)