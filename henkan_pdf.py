import pathlib
import matplotlib
from PIL import Image
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import shutil
import PyPDF2
import os
from pathlib import Path
import glob
def henkan(myname,gakuseki):
    path = './static/image/uploads/'
    files = glob.glob('./static/image/uploads/*.jpg')
    pdf = './static/image/uploads/d.pdf'
    print("henkan")

    # img_ = Image.open(img)
    # width = img_.width
    # height = img_.height
    # pdf化の繰り返し
    for l in files:
        if os.path.isfile(l) == True:
            print(l)
            image = Image.open(l)
            image = np.asarray(image)
    
            fig = plt.figure()
    
            plt.axis('off')
        
            plt.imshow(image)
            path_pdf = os.path.join(path + pathlib.PurePath(l).stem + '.pdf')
            pp = PdfPages(path_pdf)
            
            pp.savefig(fig)
        
            pp.close()
    
    #pdfを結合する

    # フォルダ内のPDFファイル一覧
    pdf_dir = Path(path)
    pdf_files = sorted(pdf_dir.glob("*.pdf"))

    # １つのPDFファイルにまとめる
    writer = PyPDF2.PdfFileWriter()
    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
        for i in range(pdf_reader.getNumPages()):
            writer.addPage(pdf_reader.getPage(i))

    # 保存ファイル名（先頭と末尾のファイル名で作成）
    
    merged_file = './static/' + pdf_files[0].stem + ".pdf"
    print("merged_file:" + merged_file)

    # 保存
    with open(merged_file, "wb") as f:
        writer.write(f)
    reader = PyPDF2.PdfFileReader(merged_file, strict=False)

    #pdfを回転させる

    out_put = PyPDF2.PdfFileWriter()
    for i in range(0, reader.getNumPages()):
        page = reader.getPage(i)
        page.rotateClockwise(90)

        out_put.addPage(page)

    with open(pdf, mode='wb') as f:
            out_put.write(f)
    os.remove(merged_file)

    path2 = os.path.join('./static/image/uploads/' + gakuseki + '_' + myname + '.pdf')

    os.rename(pdf,path2)
        
    shutil.rmtree("./trash")
    
