# 🏥 차치업무 도우미 챗봇

Python 기초 문법을 활용한 웹 기반 챗봇 학습 프로젝트입니다.

## 📋 프로젝트 개요

- **목적**: Python 기초 문법을 활용한 웹 기반 챗봇 UI 학습
- **기술 스택**: HTML, CSS, JavaScript, Python (기본 웹 서버)
- **특징**: AI/ML 없음, 하드코딩된 정적 데이터 사용, 학습 목적의 간단한 구조

## 🎯 주요 기능

### 💬 챗봇 기능
- 키워드 매칭 기반 응답 시스템
- 차치업무별 카테고리 분류 (수리, 물품, 제제약/수액, 멸균품/거즈, 격리실, ICU전동, 임종실, 신규백업, 기타)
- 자주 묻는 질문(FAQ) 자동 응답 (DARWIN 시스템, 의공기술실, 거즈공급 등)
- 사용자 이름 설정 및 개인화된 인사
- 응급상황 우선 처리
- 부서별 연락처 안내 (의공기술실, 원무과, CCU 등)

### 🌐 웹 인터페이스
- 모던하고 직관적인 챗봇 UI
- 실시간 타이핑 인디케이터
- 빠른 답변 버튼
- 모바일 반응형 디자인
- 접근성 향상 기능

### 🔧 기술적 특징
- 사용자별 세션 분리 (UUID 기반)
- 보안 강화된 파일 서빙
- 세분화된 에러 처리
- CORS 지원

## 🚀 실행 방법

### 1. 프로젝트 클론
```bash
git clone https://github.com/junjunwon/hospital-chat-request.git
cd hospital-chat-request
```

### 2. 서버 실행
```bash
python3 server.py
```

### 3. 브라우저에서 접속
```
http://localhost:8000
```

### 4. 커스텀 설정으로 실행
```bash
python3 server.py --host 0.0.0.0 --port 8080
```

## 📁 프로젝트 구조

```
hospital_chatbot/
├── chatbot.py          # 챗봇 로직 및 메시지 처리
├── data.py             # 정적 데이터 (카테고리, FAQ, 응답 등)
├── server.py           # 웹 서버 및 HTTP 요청 처리
├── static/
│   ├── script.js       # 클라이언트 사이드 JavaScript
│   └── style.css       # 챗봇 UI 스타일
├── templates/
│   └── index.html      # 메인 웹 페이지
├── .gitignore          # Git 제외 파일 목록
└── README.md           # 프로젝트 설명서
```

## 💻 사용 예시

### 기본 대화
- "안녕하세요" → 시간대별 인사말
- "제 이름은 김철수입니다" → 개인화된 응답
- "도움말" → 사용법 안내

### 업무 문의
- "EKG 수리 요청" → 수리 카테고리 응답
- "거즈 공급 언제 되나요?" → 멸균품/거즈 카테고리 응답
- "VRE 격리실 절차" → 격리실 카테고리 응답
- "ICU 전동 방법" → ICU전동 카테고리 응답

### 응급상황
- "응급", "화재", "코드블루" → 우선 처리 및 즉시 안내

### 연락처 조회
- "의공기술실 연락처" → 해당 부서 연락처 안내
- "연락처 전체" → 모든 부서 연락처 목록

## 🎓 학습 포인트

### Python 기초 문법
- 딕셔너리, 리스트를 활용한 데이터 관리
- 조건문/반복문을 이용한 키워드 매칭
- 함수와 클래스를 통한 모듈화
- 문자열 처리 및 패턴 매칭

### 웹 개발 기초
- HTTP 프로토콜 이해 (GET/POST)
- JSON 데이터 교환
- HTML/CSS/JavaScript 연동
- 클라이언트-서버 통신

### 실전 개발 경험
- 에러 처리 및 예외 상황 대응
- 사용자 경험(UX) 개선
- 보안 고려사항
- 코드 구조화 및 유지보수성

## 🔄 최신 업데이트 (2025.09.25)

### ✅ 주요 개선사항
- **사용자 세션 분리**: UUID 기반으로 다중 사용자 지원
- **타이핑 인디케이터**: CSS 버그 수정으로 애니메이션 정상 작동
- **이름 설정 기능**: 다양한 입력 패턴 지원으로 유연성 향상
- **보안 강화**: 파일 서빙 보안 및 에러 처리 개선
- **에러 처리**: 상황별 세분화된 사용자 메시지 제공

## 🌟 확장 학습 과제

### 초급
- [ ] 새로운 업무 카테고리 추가
- [ ] 더 많은 키워드와 응답 정의
- [ ] 시간대별 다른 메시지 구현

### 중급
- [ ] 대화 기록 파일 저장
- [ ] 관리자 패널 구현
- [ ] 통계 및 로그 분석 기능

### 고급
- [ ] Flask/Django 프레임워크로 전환
- [ ] 데이터베이스 연동 (SQLite → PostgreSQL)
- [ ] 실제 AI 모델 적용 (ChatGPT API 등)

## 📚 참고 자료

- [Python 공식 문서](https://docs.python.org/3/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [HTTP 서버 기초](https://docs.python.org/3/library/http.server.html)

## 📄 라이센스

이 프로젝트는 학습 목적으로 만들어졌으며 MIT 라이센스를 따릅니다.

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**💡 핵심 개념**: 이 프로젝트는 AI 없이도 유용한 챗봇을 만들 수 있음을 보여줍니다. 잘 정의된 데이터 구조와 효과적인 키워드 매칭, 직관적인 사용자 인터페이스를 통해 Python 기초 문법의 실전 활용을 학습할 수 있습니다! 🎯
