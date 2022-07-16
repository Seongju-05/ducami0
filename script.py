import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/gimsua672/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["yellow", "green"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "김수아")
write("description", "새론중학교")
write("button", "인스타그램")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생년월일": "2007년1월14일",
  "좋아하는 것": "영화, 노래",
  "애완동물": "고양이 루비",
  "좋아하는 영화": "코렐라인"
}
information(informations)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Priv
