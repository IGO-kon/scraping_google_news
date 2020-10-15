import requests
from bs4 import BeautifulSoup
from flask import *
app = Flask(__name__)

@app.route('/')
def scp():

    # WebサイトのURLを指定
    url = "https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja"

    # Requestsを利用してWebページを取得する
    r = requests.get("https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja")

    # BeautifulSoupを利用してWebページを解析する
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup)

    # soup.find_allを利用して、ヘッドラインのタイトルを取得する
    elems = soup.find_all("a", class_="DY5T1d")
    # print(elems)
    titlelist = []
    for e in elems:
        # print(e.text)
        # print(type(e.text))
        # print("------------------------")
        titlelist.append(e.text)
    titlelist_str = str(titlelist)
    print(titlelist_str)
    return render_template("scp.html", title = titlelist)

if __name__ == "__main__":
    app.run(debug=True)