# CodexTest
Codex 테스트용 브랜치

## 자동 리뷰 설정

이 저장소는 Pull Request가 생성되거나 갱신될 때 GitHub Codex 리뷰 기능을 호출하는 GitHub Actions 워크플로우가 설정되어 있습니다. 워크플로우는 `github/copilot-workflows` 저장소의 공식 PR 리뷰 재사용 워크플로우를 호출하므로 별도의 OpenAI API 키가 필요하지 않습니다. `language: ko` 입력을 사용해 Codex 리뷰 코멘트가 항상 한국어로 작성되도록 설정했습니다.
