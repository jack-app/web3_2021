import matplotlib
from PIL import Image
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import shutil
import PyPDF2
def henkan():
    

    new_jpg = './trash/gorilla_text.jpg'
    pdf_p = './trash/gorilla_text.pdf'
    pdf = './created/a_test.pdf'

    # 画像をファイルから読み込む
    image = Image.open(new_jpg)
    # 画像をNumpy配列に変換する
    image = np.asarray(image)

    # 画像のプロット先の準備
    fig = plt.figure()
    # グリッドの表示をOFFにする
    plt.axis('off')
    # Numpy配列を画像として表示する
    plt.imshow(image)

    # 保存するPDFファイル名
    pp = PdfPages(pdf_p)
    # 画像をPDFとして保存する
    pp.savefig(fig)
    # PDFの保存終了
    pp.close()


    #pdfを回転させる

    reader = PyPDF2.PdfFileReader(pdf_p, strict=False)

    page = reader.getPage(0)
    page.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    for i in range(1, reader.getNumPages()):
        page = reader.getPage(i)
        page.rotateClockwise(90)

        writer = PyPDF2.PdfFileWriter()
        writer.addPage(reader.getPage(i))

    with open(pdf, mode='wb') as f:
        writer.write(f)
    
    
    shutil.rmtree("./trash")