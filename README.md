# social-networking-service
# 📎 목차

1. [social-networking-service]
2. [개발 기간]
3. [요구사항 및 분석]
4. [기술 스택]
5. [API Endpoints]


# 🚀 social networking crud api 서비스
- sns 기능을 구현한 서비스

# 📆 개발 기간
- 2022.09.29 ~ 2022.10.05


# 📝 구현 사항
### 1. 회원가입/로그인

- 회원가입
- 로그인
  - email, password로 로그인
  - 로그인 후 access token 발급

  
### 2. 게시글 CRUD

- 게시글 생성
- 게시글 조회
  - 게시글 상세 조회
  - 게시글 목록 조회
  - 게시글 정렬, 검색
- 게시글 수정
- 게시글 삭제


### 3. 좋아요 CRUD

- 좋아요 추가 삭제


# 🛠 기술 스택
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# 🎯 API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /user/signup/ | POST | 회원가입 | email: string, password: string, name: string | Token: json |
| /user/login/ | POST | 로그인 | email: string, password: string | Token: json |
| /post/create/ | POST | 게시글 생성 | title: string, content: string, hashtags: string | 성공 여부 |
| /post/read/detail/<int:post_id>/ | GET | 게시글 상세 조회 | post_id: int | post_list: json |
| /post/list/ | GET | 게시글 목록 조회 | post_number:int (생략 가능) | post: json |
| /post/like_count/<int:post_id>/ | GET | 게시글 정렬 검색 | search: string (생략 가능), orderby: [like_count, view_count, created_at] 중 하나 (생략 가능),page_number: int (생략가능), hashtag: string (생략 가능)  ** ex) hashtag="%23맛집"  | post_list: json |
| /post/update/ | PUT | 게시글 수정 | post_id: int, title: string, content: string | 성공 여부 |
| /post/delete/<int:post_id> | DELETE | 게시글 삭제 | post_id: int | 성공 여부 |
| /post/like_count/<int:post_id>/ | GET | 좋아요 추가 삭제 | post_id: int | 성공 여부 |


