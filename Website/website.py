from flask import  Flask

app = Flak(__name__)

@app.route('/')
def index():
    return('首页')

if __name__== '__main__'
    app.run(host='ydxy64.github.io',debug=Ture)