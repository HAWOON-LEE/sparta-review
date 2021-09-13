from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give') #title_give로 가지고 온 값 여기다 한 번 찍어줘봐
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/mypage')
def mypage():
   return 'mypage입니다.'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)