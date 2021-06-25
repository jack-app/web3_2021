import create_image
import henkan_pdf
import os
from flask import Flask, request, redirect, url_for, render_template
from flask.helpers import flash
from werkzeug.utils import secure_filename
from flask import send_from_directory, jsonify
import cv2
import numpy as np
import json
import base64
from datetime import datetime 

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
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/triming', methods=['POST'])
def triming():
    data = json.loads(request.data)
    img = data['img']
    idx = img.find(',')
    img = img[idx+1:]

    now = datetime.now()
    time = now.strftime('%Y%m%d_%H%M%S')

    num = sum(
        os.path.isfile(os.path.join(UPLOAD_FOLDER, name))
        for name in os.listdir(UPLOAD_FOLDER))
    file_name = os.path.join(app.config['UPLOAD_FOLDER'],
             "image_" + str(num) + ".jpg")

    with open(file_name, mode='wb') as f:
        decoded = base64.b64decode(img.encode("utf-8").decode())
        f.write(decoded)
    return jsonify({'message': 'hello internal'}), 200


# ファイルを受け取る方法の指定
@app.route('/', methods=['GET', 'POST'])
def uploads_file():
    # session['username'] = 'aaa'
    # username = escape(session['username'])
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        max_age = 60 * 60 * 24
        expires = int(datetime.now().timestamp())
        myname = request.cookies.get("myname",None)
        gakuseki = request.cookies.get("gakuseki",None)

        create_image.create_image(myname, gakuseki)
        henkan_pdf.henkan(myname, gakuseki)
        # アップロード後のページに転送
        #         return redirect(url_for('uploaded_file', filename=filename))
        # return render_template('index.html')
        created_pdf = os.path.join('./static/image/uploads/' + gakuseki + '_' + myname + '.pdf')
        if os.path.exists(created_pdf):
            downloadFileName = gakuseki + '_' + myname + '.pdf'
            downloadFile = created_pdf
            print("download")
            # ダウンロードを実行
            return send_file(downloadFile, as_attachment = True, \
                attachment_filename = downloadFileName, \
                mimetype = PDF_MIMETYPE),shutil.rmtree('./static/image/uploads'),os.mkdir('./static/image/uploads')
    return render_template('index.html', ImgSrc="image/sozai_image_101085.jpg")


@app.route('/upload')
# ファイルを表示する
def uploaded_file():
    print(request.args.get("filename"))
    file_name = os.path.join(app.config['UPLOAD_FOLDER'],
                             request.args.get("filename")).replace(
                                 os.sep, "/")
    num = sum(
        os.path.isfile(os.path.join(UPLOAD_FOLDER, name))
        for name in os.listdir(UPLOAD_FOLDER)) - 1
    return render_template("img.html", num=num, fileUrl=file_name)
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
    app.run(host='0.0.0.0')
