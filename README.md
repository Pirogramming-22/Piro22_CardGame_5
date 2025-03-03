# 🖐️Piro22_CardGame_5🖐️

## 📜의존성 목록 정리
```
pip install django
pip install social-auth-app-django
pip install django-environ
```

## 1. 컨벤션

### 🧐Commit Type

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

### 🌿Branch

| Branch 종류        | 설명             |
|---------------------|------------------|
| `main`              | 메인 브랜치      |
| `member's name`     | 담당 부분별 분업화 |


## 2. 협업을 위한 업무분장

과제를 부여받은 즉시, `Sprint Planning`을 통해 figma 프로토타입을 먼저 제작하고, 전체적인 플로우차트를 구현하였다.

- Frontend:
  - Figma 프로토타입에 따른 디자인 작업(CSS 및 html 레이아웃 구성) / JavaScript 구현

- Backend:
  - 프론트 팀에서 이해하기 쉽게 기본 페이지 렌더링까지만 처리진행
  - 인증 관리(`app: user`) 및 비즈니스 로직 처리 (`app: game`)

### 사용한 협업 툴
  📒노션<br>
  https://simplistic-almanac-499.notion.site/Piro22_CardGame_5-17dde9999953807a8fa3fcd4f8a44130

  🎨피그마<br> 
  https://www.figma.com/design/T0daihMCqHHkf99ZpiNLrk/%ED%94%BC%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-5%EC%A1%B0?node-id=0-1&t=NII8nJSGoZOrPKCD-1

  🌱깃허브<br>
  https://github.com/Pirogramming-22/Piro22_CardGame_5.git

### 커뮤니케이션 및 협업
📆Daily Scrum: 
  - 매일 2회 (점심, 저녁) 개발 현황 공유
  - 주요 진행 사항 및 문제 해결 방안 논의

### 역할 분담
🚩각 Sprint 마일스톤:
  - 각 기능에 대한 작업 진행 상황을 매일 Scrum에서 점검
  - 진행 중인 작업 및 문제 해결 사항 공유

| Role     | Name     | Tasks                                   |
|----------|----------|-----------------------------------------|
| Frontend | 임유지   | 전체 페이지 디자인 및 레이아웃 구성       |
| Frontend | 김수연   | 로그인, Ranking 그래프 디자인            |
| Backend  | 홍다오   | Login, SSO                             |
| Backend  | 박혜린   | Game_start, game_detail, counter_attack, result |
| Backend  | 김영호   | Dashboard, game_history, ranking       |


## 3. 프로젝트 설명
### 유저 간의 카드 대결을 통해 점수를 얻거나 잃고, 최종적으로 랭킹을 결정하는 게임

### 📌주요 기능

- **소셜 로그인**: 구글로 소셜 로그인 기능을 구현하여, 유저가 쉽게 로그인할 수 있도록 지원합니다.
- **카드 선택 및 게임 대결**: 1~10까지의 숫자 카드 중 랜덤으로 제공된 5개 카드 중 하나를 선택하여 상대방에게 게임을 걸 수 있습니다.
- **게임 결과**: 선택한 카드에 따라 점수가 계산되며, 승자는 점수를 획득하고 패자는 점수를 잃습니다.
- **무승부 처리**: 같은 카드를 선택한 경우, 무승부로 처리하여 점수 차감이 없습니다.
- **랭킹 시스템**: 진행된 게임에서 획득한 점수를 바탕으로 유저별 랭킹을 확인할 수 있습니다.
- **게임 삭제 기능**: 유저는 자신이 시작한 게임을 삭제할 수 있습니다.


### 🎮게임 흐름🎮

1. **로그인**: 유저는 먼저 로그인합니다. (일반 로그인 또는 소셜 로그인 옵션 제공)
2. **게임 시작**: 로그인한 유저(나)는 숫자 카드 5개 중 하나와, 공격할 상대도 선택합니다. 
3. **게임 대기**: 상대는 자신의 계정으로 로그인 후, 대기 중인 게임 목록에서 유저(나)의 도전장을 확인하고 반격할 수 있습니다.
4. **카드 선택**: 유저(나)은 자신의 카드를 선택하고, 게임에 응답합니다.
5. **게임 결과**: 서로 선택한 카드 숫자에 따라 대결을 벌이고, 결과를 확인합니다.(카드 숫자가 작은 사람이 승리!)
    - **승리**: 승리자는 자신의 카드 숫자만큼 점수를 얻습니다.
    - **패배**: 패배자는 자신의 카드 숫자만큼 점수를 잃습니다.
    - **무승부**: 두 유저가 동일한 카드를 낸 경우로,  양쪽 모두 점수 차감이 없습니다.
6. **랭킹 리그**: 각 유저의 게임 결과에 따라 점수가 합산되어 랭킹이 표시됩니다.
7. **게임 삭제**: 유저는 자신이 공격한 게임을 삭제할 수 있습니다.


