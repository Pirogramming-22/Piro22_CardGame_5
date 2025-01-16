# Piro22_CardGame_5

## 과제 협의사항

### 1. Commit Type

| Keyword | When to use |
| --- | --- |
| `feat` | 기능 관련 커밋 |
| `fix` | 버그 수정 |
| `add` | 내용을 추가하였을 때 |
| `chore` | 기타 변경 사항 |
| `docs` | 문서 수정 |
| `style` | 코드 formatting, 세미콜론 누락, 코드 자체의 변경이 없는 경우 |
| `refactor` | 코드 리팩토링 |
| `test` | 테스트 코드, 리팩토링 테스트 코드 추가 |
| `design` | CSS 등 사용자 UI 디자인 변경 |
| `comment` | 필요한 주석 추가 및 변경 |
| `rename` | 파일 또는 폴더 명을 수정하거나 옮기는 작업만인 경우 |
| `remove` | 파일을 삭제하는 작업만 수행한 경우 |
| `!BREAKING CHANGE` | 커다란 API 변경의 경우 |
| `!HOTFIX` | 급하게 치명적인 버그를 고쳐야 하는 경우 |
- 기능을 추가하거나 코드 수정하기 전 자주 커밋하기
- 주요 부분 완성할 때 마다 main에 merge 하여 자주 동기화
- Merge 할 때 마다 팀원들에게 전파하기

### 2. 협업을 위한 업무분장

과제를 부여받은 즉시, `Sprint Planning`을 통해 figma 프로토타입을 먼저 제작하고, 전체적인 플로우차트를 구현하였다.

- Frontend:
  - Figma 프로토타입에 따른 디자인 작업(CSS 및 html 레이아웃 구성) / JavaScript 구현

- Backend:
  - 프론트 팀에서 이해하기 쉽게 기본 페이지 렌더링까지만 처리진행
  - 인증 관리(`app: user`) 및 비즈니스 로직 처리 (`app: game`)

## 커뮤니케이션 및 협업
- Daily Scrum: 
  - 매일 2회 (점심, 저녁) 개발 현황 공유
  - 주요 진행 사항 및 문제 해결 방안 논의

## 일정 및 진행 상태
- 각 Sprint 마일스톤:
  - 각 기능에 대한 작업 진행 상황을 매일 Scrum에서 점검
  - 진행 중인 작업 및 문제 해결 사항 공유

| Role     | Name     | Tasks                                   |
|----------|----------|-----------------------------------------|
| Frontend | 임유지   | 전체 페이지 디자인 및 레이아웃 구성       |
| Frontend | 김수연   | 로그인, Ranking 그래프 디자인            |
| Backend  | 홍다오   | Login, SSO                             |
| Backend  | 박혜린   | Game_start, game_detail, counter_attack, result |
| Backend  | 김영호   | Dashboard, game_history, ranking       |


## 프로젝트 설명


## 의존성 목록 정리
```
pip install django
pip install social-auth-app-django
```