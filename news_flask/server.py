import os
# re 字符串切割
import re

# flask 网页后端
from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__)


# 4.6.7.8.9.10.11.12.13.14

# part 5
# 教育
@app.route('/edu')
def edu():
    all_new = []
    with open(os.getcwd() + "/datasets/13_教育.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = re.split('\t', line)

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    return render_template('edu.html', all_new=all_new)


# 公益
@app.route('/community')
def community():
    all_new = []
    with open(os.getcwd() + "/datasets/12_旅游.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = re.split('\t', line)

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    return render_template('community.html', all_new=all_new)


# part 4
# 游戏
@app.route('/game')
def game():
    all_new = []
    with open(os.getcwd() + "/datasets/11_游戏.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = re.split('\t', line)

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    return render_template('game.html', all_new=all_new)


# 旅游
@app.route('/travel')
def travel():
    all_new = []
    with open(os.getcwd() + "/datasets/12_旅游.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = re.split('\t', line)

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    return render_template('travel.html', all_new=all_new)


# part 3
# 房产
@app.route('/property')
def property():
    all_new = []
    with open(os.getcwd() + "/datasets/9_房产.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = re.split('\t', line)

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    return render_template('property.html', all_new=all_new)


# 阅读
@app.route('/read')
def read():
    all_new = []
    with open(os.getcwd() + "/datasets/10_读书.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = re.split('\t', line)

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    return render_template('read.html', all_new=all_new)


# part 2
# 体育
@app.route('/sport')
def sport():
    all_new = []
    with open(os.getcwd() + "/datasets/4_体育.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = line.split('\t')

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    return render_template('sport.html', all_new=all_new)

# 科技
@app.route('/tech')
def tech():
    all_new = []
    with open(os.getcwd() + "/datasets/6_科技.txt", encoding='utf-8') as f:
        # 读每一行
        for line in f.readlines():
            # 按tab键切割字符串
            split_line = line.split('\t')

            all_new.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    # 使用模板消息渲染
    return render_template('tech.html', all_new=all_new)


# part 1

# 汽车
@app.route('/car')
def car():
    news = []
    with open(os.getcwd() + "/datasets/7_汽车.txt", encoding='utf-8') as f:
        # 读每一行
        for line in f.readlines():
            # 按tab键切割字符串
            split_line = line.split('\t')

            news.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    # 使用模板消息渲染
    return render_template('car.html', news=news)


# 女人
@app.route('/female')
def female():
    news = []
    # 打开文件
    with open(os.getcwd() + "/datasets/8_女人.txt", encoding='utf-8') as f:
        for line in f.readlines():
            split_line = line.split('\t')
            news.append({
                'title': split_line[0],
                'url': split_line[2]
            })
    # 返回渲染
    return render_template('female.html', news=news)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')




if __name__ == '__main__':
    # 运行flask 后端
    # 访问 http://localhost:5000/{相关的url}
    # 例如 http://localhost:5000/female
    app.run()
