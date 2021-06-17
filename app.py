# import create_pdf_v
import create_image
import henkan_pdf
import os
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, request, redirect, url_for, render_template
from flask.helpers import flash
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory
# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = './uploads'
# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ファイルを受け取る方法の指定
@app.route('/', methods=['GET', 'POST'])
def uploads_file():
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        # データの取り出し
        file = request.files['file']
        # ファイル名がなかった時の処理
        # if file.filename == '':
        #     flash('ファイルがありません')
        #     return redirect(request.url)
        # ファイルのチェック
        if file and allwed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            # filename = secure_filename(file.filename)
            # ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'base_image.jpg'))
            # アップロード後のページに転送
            create_image.create_image()
            henkan_pdf.henkan()
            return redirect(url_for('uploaded_file', ))
    return '''
    <!doctype html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>
                ファイルをアップロードして判定しよう
            </title>
        </head>
        <body>
            <h1>
                ファイルをアップロードして判定しよう
            </h1>
            <form method = post enctype = multipart/form-data>
            <p><input type=file name = file></p>
            <input type = submit value = Upload>
            </form>
        </body>
    </html>
'''

# ファイルを表示する
#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# ファイルを変形
# @app.route('/uploads/create')#,methods = ['POST'])
# def create_file(filename):
#     #img_b = request.files['file']
#     print(filename)
#     #arranged = create_pdf_v.create_pdf()
#     create_pdf_v.create_pdf()
#     #return send_from_directory(app.config['UPLOAD_FOLDER'], arranged)
#     return redirect(url_for('uploaded_file'))

@app.route('/uploaded')
def uploaded_file():
    return 'アップロード完了'

if __name__ == "__main__":
    app.run(debug=True, port=5050)