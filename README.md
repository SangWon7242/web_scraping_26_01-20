# 🐍 파이썬 가상환경 구성 튜토리얼

> 웹 스크래핑 학습을 위한 가상환경 설정 가이드

---

## 📚 가상환경이란?

가상환경은 **프로젝트별로 독립된 파이썬 작업 공간**을 만드는 것입니다.

### 🏠 비유로 이해하기

집을 여러 개의 방으로 나누는 것과 비슷해요!

- **거실** = 웹 스크래핑 프로젝트 (requests, beautifulsoup4 설치)
- **침실** = 게임 개발 프로젝트 (pygame 설치)
- **서재** = 데이터 분석 프로젝트 (pandas, numpy 설치)

각 방(가상환경)은 서로 영향을 주지 않아요. 거실에 소파를 놓아도 침실에는 소파가 없는 것처럼, 웹 스크래핑 프로젝트에 설치한 라이브러리는 다른 프로젝트에 영향을 주지 않습니다.

### ❓ 왜 가상환경을 사용하나요?

1. **프로젝트마다 다른 라이브러리 버전 사용 가능** - A 프로젝트는 requests 2.0, B 프로젝트는 requests 3.0 사용 가능
2. **충돌 방지** - 서로 다른 프로젝트의 라이브러리가 섞이지 않음
3. **깔끔한 관리** - 프로젝트를 지우면 해당 라이브러리도 함께 정리됨

---

## 🛠️ 1단계: 가상환경 만들기

터미널(명령 프롬프트)을 열고, 작업할 폴더로 이동한 후 아래 명령어를 입력하세요.

```bash
python -m venv web_scrap
```

### 📝 명령어 설명

| 부분        | 의미                                      |
| ----------- | ----------------------------------------- |
| `python`    | 파이썬 프로그램 실행                      |
| `-m venv`   | 가상환경 만드는 기능 사용                 |
| `web_scrap` | 가상환경 이름 (원하는 이름으로 변경 가능) |

### ✅ 확인하기

명령어 실행 후 `web_scrap` 폴더가 생성되었으면 성공!

```
📁 python_projects
└── 📁 web_scrap      ← 이 폴더가 생겼어요!
    ├── 📁 Include
    ├── 📁 Lib
    ├── 📁 Scripts
    └── 📄 pyvenv.cfg
```

---

## 🔌 2단계: 가상환경 활성화하기

가상환경을 사용하려면 먼저 **활성화**해야 합니다.

### Windows에서 활성화

```bash
web_scrap\Scripts\activate
```

### ✅ 활성화 확인 방법

활성화되면 프롬프트 앞에 **(web_scrap)**이 표시됩니다!

```
# 활성화 전
c:\Users\User\Desktop\python_projects>

# 활성화 후 ✨
(web_scrap) c:\Users\User\Desktop\python_projects>
```

> 💡 **팁**: `(web_scrap)`이 보이면 가상환경 안에 있다는 뜻이에요!

---

## 📦 3단계: 웹 스크래핑 라이브러리 설치하기

가상환경이 활성화된 상태에서 라이브러리를 설치합니다.

```bash
pip install requests beautifulsoup4
```

### 📝 설치되는 라이브러리

| 라이브러리       | 역할                                      |
| ---------------- | ----------------------------------------- |
| `requests`       | 웹사이트에서 데이터를 가져오는 도구       |
| `beautifulsoup4` | 가져온 데이터에서 원하는 정보를 찾는 도구 |

### ✅ 설치 확인하기

```bash
pip list
```

아래와 같이 설치된 라이브러리 목록이 나오면 성공!

```
Package            Version
------------------ --------
beautifulsoup4     4.14.3
requests           2.32.5
...
```

---

## 🔌 4단계: 가상환경 비활성화하기

작업을 마치면 가상환경을 비활성화합니다.

```bash
deactivate
```

### ✅ 비활성화 확인 방법

프롬프트 앞의 **(web_scrap)**이 사라집니다!

```
# 비활성화 전
(web_scrap) c:\Users\User\Desktop\python_projects>

# 비활성화 후 ✨
c:\Users\User\Desktop\python_projects>
```

---

## 📋 전체 명령어 요약

| 단계 | 명령어                                | 설명                      |
| ---- | ------------------------------------- | ------------------------- |
| 1    | `python -m venv web_scrap`            | 가상환경 생성             |
| 2    | `web_scrap\Scripts\activate`          | 가상환경 활성화 (Windows) |
| 3    | `pip install requests beautifulsoup4` | 라이브러리 설치           |
| 4    | `pip list`                            | 설치된 라이브러리 확인    |
| 5    | `deactivate`                          | 가상환경 비활성화         |

---

## ⚠️ 문제 해결 (에러가 발생했을 때)

### 🚨 `python`이 인식되지 않아요

파이썬이 설치되지 않았거나, 환경변수에 등록되지 않은 경우입니다.

**해결 방법:**

1. [python.org](https://www.python.org/downloads/)에서 파이썬 설치
2. 설치 시 **"Add Python to PATH"** 체크 필수!

### 🚨 활성화 스크립트 실행이 거부돼요

PowerShell에서 스크립트 실행 정책 문제입니다.

**해결 방법:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🎉 다음 단계

가상환경 설정이 완료되었습니다! 이제 웹 스크래핑을 시작할 준비가 되었어요.

다음에 작업할 때는:

1. 터미널에서 프로젝트 폴더로 이동
2. `web_scrap\Scripts\activate` 로 가상환경 활성화
3. 파이썬 코드 작성 및 실행
4. 작업 완료 후 `deactivate`

**즐거운 웹 스크래핑 학습 되세요!** 🚀
