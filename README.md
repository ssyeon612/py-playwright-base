# Python + Playwright 기반 자동화 테스트 프로젝트

이 프로젝트는 **Python + Playwright** 기반의 자동화 테스트 시스템입니다.  

---

## 📦 기술 스택
- **언어**: Python 3.x
- **프레임워크**: [Playwright for Python](https://playwright.dev/python/)
- Allure (테스트 리포트)
- dotenv (환경 변수 관리)
- Makefile (자동화 스크립트)

---

## ⚙️ 환경 변수 설정

`.env.example` 파일을 참고하여 `.env` 파일을 생성한 뒤 정보를 입력하세요.

```env
URL=your_url
```

## 🛠 Makefile 사용 안내

이 프로젝트는 반복적인 테스트 실행 및 리포트 생성을 간편하게 하기 위해 `Makefile`을 사용합니다.  
아래 명령어들을 사용하면 `pytest`, Allure 리포트 생성 등을 보다 쉽게 수행할 수 있습니다.

### 📄 주요 명령어

| 명령어 | 설명 |
|--------|------|
| `make test` | pytest를 실행하여 테스트를 수행합니다 (`pytest.ini` 설정 기준으로 동작) |
| `make report` | Allure 리포트를 생성하고, 브라우저에서 결과를 엽니다 |
| `make clean` | 생성된 리포트 파일 및 스크린샷 등을 정리합니다 (`allure-results/`, `allure-report/`, `screenshots/` 삭제) |

## 📁 디렉토리 구조
<pre lang="markdown">
YT_TEST/
├── conftest.py         # 공통 테스트 초기화 설정 (진입 페이지, 팝업 닫기 등)
├── db.py               # DB 연결 및 쿼리 유틸 함수 (fetch, insert 등)
├── Makefile            # 테스트 실행 및 리포트 생성 자동화 명령어
├── pages/              # Page Object Model 구조 폴더
│ ├── base_page.py      # 공통 BasePage (locator, click, input 등 메서드)
├── tests/              # 테스트 스크립트 디렉토리
│ ├── test_example.py
│ └── ...
├── utils/            # 공통 유틸리티 함수
│ ├── error_handler.py  # 예외 처리 + 스크린샷 첨부
│ └── ... 
├── screenshots/        # 테스트 실패 시 스크린샷 저장 위치
├── allure-results/     # Allure 테스트 결과 저장 폴더
├── allure-report/      # Allure HTML 리포트가 생성되는 폴더
├── .env                # 개인 환경 변수
├── .env.example        # 환경 변수 예시 파일
├── requirements.txt    # 필요한 패키지들
└── README.md           # 현재 문서
</pre>
