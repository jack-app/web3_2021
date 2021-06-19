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
import cv2
import numpy as np

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = './static/image/uploads'
# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'web3'

def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ファイルを受け取る方法の指定
@app.route('/', methods=['GET', 'POST'])
def uploads_file():
    # session['username'] = 'aaa'
    # username = escape(session['username'])
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        # データの取り出し
        file = request.files['file']
        # files = request.files.getlist['file']
        print(file)
        print(request.files['file'])
        # ファイル名がなかった時の処理
        # for file in files:
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
            # ファイルのチェック
        if file and allwed_file(file.filename):
                # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            num = sum(os.path.isfile(os.path.join(UPLOAD_FOLDER, name)) for name in os.listdir(UPLOAD_FOLDER))
                # ファイルの保存
                # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], "image_" + str(num) + ".jpg"), img)
            create_image.create_image()
            henkan_pdf.henkan()
            # アップロード後のページに転送
    #         return redirect(url_for('uploaded_file', filename=filename))
    # return render_template('index.html')
            return render_template("index.html", ImgSrc="image/uploads/image_"+str(num)+".jpg")
    return render_template('index.html', ImgSrc="image/sozai_image_101085.jpg")

@app.route('/upload')
# ファイルを表示する
def uploaded_file():
    print(request.args.get("filename"))
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], request.args.get("filename")).replace(os.sep, "/")
    num = sum(os.path.isfile(os.path.join(UPLOAD_FOLDER, name)) for name in os.listdir(UPLOAD_FOLDER)) - 1
    return render_template("img.html", num = num, fileUrl = file_name)
    # return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# @app.route('/upload', methods=['GET', 'POST'])
# def uploads_trimmedfile():
#     # リクエストがポストかどうかの判別
#     print('ccc')
#     if request.method == 'POST':
#         # ファイルがなかった場合の処理
#         if 'file' not in request.files:
#             flash('ファイルがありません')
#             return redirect(request.url)
#         # データの取り出し
#         files = request.files.getlist['resultImg']
#         # ファイル名がなかった時の処理
#         if files.filename == '':
#             flash('ファイルがありません')
#             return redirect(request.url)
#         # ファイルのチェック
#         if files and allwed_file(files.filename):
#             # 危険な文字を削除（サニタイズ処理）
#             filename = secure_filename(files.filename)
#             num = sum(os.path.isfile(os.path.join(UPLOAD_FOLDER, name)) for name in os.listdir(UPLOAD_FOLDER))
#             # ファイルの保存
#             # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             for l in files:
#                 file = files[l]
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'base_image.jpg'))
# #             img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
# #             cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], "trimmedImage_" + str(num) + ".jpg"), img)
            
#             # 画像ファイル1枚保存のみ対応
#             create_image.create_image()
#             henkan_pdf.henkan()
#             # アップロード後のページに転送
#     return render_template("result.html")

if __name__ == "__main__":
    app.run()
