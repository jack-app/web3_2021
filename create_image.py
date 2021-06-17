from PIL import Image
import PIL.ImageDraw
import PIL.ImageFont
import os
import shutil

def create_image():
    # import os
    # import shutil

    trash_path = "./trash"
    if not os.path.exists(trash_path):
        os.mkdir(trash_path)
    else:
        shutil.rmtree(trash_path)
        os.mkdir(trash_path)


    # from flask import request
    rabel = "./trash/image.png"           
    rabel_r = './trash/image_rotated.png'
    #img_b = request.files['file']  #ここの変数に入力されたファイル名を代入したい
    img_b = './uploads/base_image.jpg'
    new_jpg = './trash/gorilla_text.jpg'
    # pdf_p = './trash/gorilla_text.pdf'
    # pdf = './created/gorilla-test.pdf'

    #create_rabel

    # import PIL.Image
    # import PIL.ImageDraw
    # import PIL.ImageFont
    
    # 使うフォント，サイズ，描くテキストの設定
    ttfontname = "./fonts/GenShinGothic-Monospace-Medium.ttf"
    fontsize = 64
    text = "名古屋大学情報学部自然情報学科　矢島夏希"

    # 画像サイズ，背景色，フォントの色を設定
    canvasSize    = (2000, 150)
    backgroundRGB = (255, 255, 255)
    textRGB       = (0, 0, 0)

    # 文字を描く画像の作成
    img  = Image.new('RGB', canvasSize, backgroundRGB)
    draw = PIL.ImageDraw.Draw(img)

    # 用意した画像に文字列を描く
    font = PIL.ImageFont.truetype(ttfontname, fontsize)
    textWidth, textHeight = draw.textsize(text,font=font)
    textTopLeft = (canvasSize[0]//6, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
    draw.text(textTopLeft, text, fill=textRGB, font=font)

    img.save(rabel)

    #rotate_rabel

    # from PIL import Image

    original_image = Image.open(rabel)

    roated_image = original_image.rotate(angle=90, resample=Image.BICUBIC, expand=True)

    roated_image.save(rabel_r)

    #rabeling

    img_1 = Image.open(img_b)
    img_2 = Image.open(rabel_r)

    img_1_2 = img_1.copy()

    img_1_2.paste(img_2,(50,50))

    img_1_2.save(new_jpg)
