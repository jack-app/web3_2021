from PIL import Image
import PIL.ImageDraw
import PIL.ImageFont
import os
import shutil


def create_image(myname,gakuseki):

    trash_path = "./trash"
    if not os.path.exists(trash_path):
        os.mkdir(trash_path)
    else:
        shutil.rmtree(trash_path)
        os.mkdir(trash_path)

    rabel = "./trash/image.png"           
    rabel_r = './trash/image_rotated.png'
    # img_b = os.path.join('./static/image/uploads/' + time + '_0_' + gakuseki + '.jpg')
    img_b = os.path.join('./static/image/uploads/image_1.jpg')
    
    #画像サイズを取得

    img_1 = Image.open(img_b)
    width = img_1.width
    height = img_1.height

    # create_rabel

    # 使うフォント，サイズ，描くテキストの設定
    ttfontname = "./fonts/GenShinGothic-Monospace-Medium.ttf"
    fontsize = 64*height//4032
    text = gakuseki + '_' + myname

    # 画像サイズ，背景色，フォントの色を設定
    # トリミングされてない画像だとcanvasSize = (2000, 150) 
    canvasSize = (width*2000//3024, height*150//4032)
    backgroundRGB = (255, 255, 255)
    textRGB = (0, 0, 0)

    # 文字を描く画像の作成
    img = Image.new('RGB', canvasSize, backgroundRGB)
    draw = PIL.ImageDraw.Draw(img)

    # 用意した画像に文字列を描く
    font = PIL.ImageFont.truetype(ttfontname, fontsize)
    textWidth, textHeight = draw.textsize(text, font=font)
    textTopLeft = (canvasSize[0]//6, canvasSize[1] //
                   2-textHeight//2)  # 前から1/6，上下中央に配置
    draw.text(textTopLeft, text, fill=textRGB, font=font)

    img.save(rabel)

    #rotate_rabel
    
    original_image = Image.open(rabel)

    roated_image = original_image.rotate(
        angle=90, resample=Image.BICUBIC, expand=True)

    roated_image.save(rabel_r)

        #rabeling

    img_2 = Image.open(rabel_r)

    img_1_2 = img_1.copy()

    img_1_2.paste(img_2,(50*width//3024,50*height//4032))

    img_1_2.save(os.path.join('./static/image/uploads/image_0.jpg'))
