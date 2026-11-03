# CLAUDE.md

생명 가능 지대 탐구실: 단일 `index.html`로 된 고등학교 지구과학 웹앱입니다. `main` 브랜치가 Vercel로 배포됩니다.

## Git 작업 규칙: 항상 `main`에 머지

변경을 마치면 **사용자에게 따로 묻지 않고 항상 `main`까지 머지하고 푸시**합니다.

1. 작업 브랜치에서 커밋하고 푸시합니다.
2. `main`을 최신으로 받은 뒤, 작업 브랜치를 `main`에 머지합니다.
   - 가능하면 fast-forward(`git merge --ff-only`)로 합칩니다.
   - fast-forward가 안 되면 일반 머지를 하되, **충돌이 나면 멈추고 사용자에게 알립니다.**
3. `main`을 푸시합니다(`git push origin main`).
4. PR은 만들지 않습니다(사용자가 요청할 때만).
5. 머지 전에 아래 '확인'을 통과해야 합니다. 실패하면 머지하지 말고 결과를 알립니다.

```bash
git push -u origin <작업-브랜치>
git checkout main && git pull --ff-only origin main
git merge --ff-only <작업-브랜치>
git push origin main
git checkout <작업-브랜치>
```

## 확인 (머지 전)

- 페이지를 열면 콘솔에 `검증 수치 일치 ✓`가 나오고, `document.documentElement.dataset.selfcheck === 'pass'`인지 확인합니다.
- Playwright로 태블릿 가로(1280×800)·세로(800×1280), 전자칠판(1920×1080), 폰(390×844)에서 콘솔 오류·가로 스크롤이 없는지 봅니다.
- 태블릿·전자칠판·PC 크기에서는 페이지 스크롤 없이 한 화면에 들어와야 합니다.

## 지켜야 할 것

- 단일 `index.html`(HTML·CSS·JS·인라인 SVG), 외부 CDN 없음.
- 개인정보 입력, 쿠키·localStorage·서버 전송·분석 도구 금지. 상태는 페이지 변수에만 둡니다.
- 물리 상수(`HZ_INNER_S`, `HZ_OUTER_S`, `MASS_LUMINOSITY_POWER`)는 `<script>` 맨 위 한곳에서만 정의합니다.
- 제목을 누르면 1단계로, 푸터의 제작자 문구와 허브 링크(`연경쌤의 지구과학 실험실 둘러보기 →`)는 유지합니다.
- 화면 구조나 사용법이 바뀌면 `README.md`도 함께 고칩니다.
