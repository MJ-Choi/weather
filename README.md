# Weather API

## 사전준비
환경 변수에 API KEY 입력
```
# 1) .env_ex 파일을 .env로 변경
mv .env_ex .env

# 2) API key 입력
OPENWEATHER_API_KEY=api.openweathermap.org의 API_KEY 입력
```

## 구조
| 파일         | 설명                       |
|------------|--------------------------|
| config     | 환경변수 기반 설정 관리            |
| controller | API 라우팅 및 엔드포인트 정의       |
| service    | 비즈니스 로직, 메모리 캐시 TTL 관리   |
| util       | HTTP 호출 담당 (재시도, 백오프 포함) |
| test/      | 테스트 코드                   |

## 실행
### 어플리케이션 실행
```shell
# 1. 가상환경 생성 & 활성화
$ python -m venv .venv
$ source .venv/bin/activate

# 2. 패키지 설치
$ pip install -r requirements.txt

# 3. 어플리케이션 실행
$ uvicorn main:app --reload

웹페이지 접속
http://127.0.0.1:8000/docs
```

### 테스트 코드 실행
```shell
$ .venv/bin/pytest -rs
```


## Q. 좋은 코드란?
협업하는 동료들이 보았을 때 보기 좋고 하나의 클래스가 하나의 역할만을 수행하여
유지보수 하기 좋고 추후 서비스가 늘어나도 확장하기 쉬운 코드라고 생각합니다.