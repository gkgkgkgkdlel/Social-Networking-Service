# social-networking-service
# ๐ ๋ชฉ์ฐจ

1. [social-networking-service]
2. [๊ฐ๋ฐ ๊ธฐ๊ฐ]
3. [์๊ตฌ์ฌํญ ๋ฐ ๋ถ์]
4. [๊ธฐ์  ์คํ]
5. [API Endpoints]


# ๐ social networking crud api ์๋น์ค
- sns ๊ธฐ๋ฅ์ ๊ตฌํํ ์๋น์ค

# ๐ ๊ฐ๋ฐ ๊ธฐ๊ฐ
- 2022.09.29 ~ 2022.10.05


# ๐ ๊ตฌํ ์ฌํญ
### 1. ํ์๊ฐ์/๋ก๊ทธ์ธ

- ํ์๊ฐ์
- ๋ก๊ทธ์ธ
  - email, password๋ก ๋ก๊ทธ์ธ
  - ๋ก๊ทธ์ธ ํ access token ๋ฐ๊ธ

  
### 2. ๊ฒ์๊ธ CRUD

- ๊ฒ์๊ธ ์์ฑ
- ๊ฒ์๊ธ ์กฐํ
  - ๊ฒ์๊ธ ์์ธ ์กฐํ
  - ๊ฒ์๊ธ ๋ชฉ๋ก ์กฐํ
  - ๊ฒ์๊ธ ์ ๋ ฌ, ๊ฒ์
- ๊ฒ์๊ธ ์์ 
- ๊ฒ์๊ธ ์ญ์ 


### 3. ์ข์์ CRUD

- ์ข์์ ์ถ๊ฐ ์ญ์ 


# ๐  ๊ธฐ์  ์คํ
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# ๐ฏ API Endpoints
| endpoint | HTTP Method | ๊ธฐ๋ฅ   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /user/signup/ | POST | ํ์๊ฐ์ | email: string, password: string, name: string | Token: json |
| /user/login/ | POST | ๋ก๊ทธ์ธ | email: string, password: string | Token: json |
| /post/create/ | POST | ๊ฒ์๊ธ ์์ฑ | title: string, content: string, hashtags: string | ์ฑ๊ณต ์ฌ๋ถ |
| /post/read/detail/<int:post_id>/ | GET | ๊ฒ์๊ธ ์์ธ ์กฐํ | post_id: int | post_list: json |
| /post/list/ | GET | ๊ฒ์๊ธ ๋ชฉ๋ก ์กฐํ | post_number:int (์๋ต ๊ฐ๋ฅ) | post: json |
| /post/like_count/<int:post_id>/ | GET | ๊ฒ์๊ธ ์ ๋ ฌ ๊ฒ์ | search: string (์๋ต ๊ฐ๋ฅ), orderby: [like_count, view_count, created_at] ์ค ํ๋ (์๋ต ๊ฐ๋ฅ),page_number: int (์๋ต๊ฐ๋ฅ), hashtag: string (์๋ต ๊ฐ๋ฅ)  ** ex) hashtag="%23๋ง์ง"  | post_list: json |
| /post/update/ | PUT | ๊ฒ์๊ธ ์์  | post_id: int, title: string, content: string | ์ฑ๊ณต ์ฌ๋ถ |
| /post/delete/<int:post_id> | DELETE | ๊ฒ์๊ธ ์ญ์  | post_id: int | ์ฑ๊ณต ์ฌ๋ถ |
| /post/like_count/<int:post_id>/ | GET | ์ข์์ ์ถ๊ฐ ์ญ์  | post_id: int | ์ฑ๊ณต ์ฌ๋ถ |


