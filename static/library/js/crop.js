document.addEventListener("DOMContentLoaded", function(){

const imgview = document.getElementById("imgview");
const cropArea = document.getElementById("cropArea");
const cropimg = document.getElementById("cropimg");



    window.onload = function() {
        imgview.style.display = "flex";
        cropArea.style.display ="none";
        cropimg.style.display ="none";
    }

    const cropStart = function(){
        if (fileNum == 0) {
            return; //実行を停止
            } 
        if(imgview.style.display=="flex"){
            // noneで非表示
            imgview.style.display ="none";
        }else{
            // blockで表示
            imgview.style.display ="flex";
        }

        if(cropArea.style.display=="block"){
            // noneで非表示
            cropArea.style.display ="none";
        }else{
            // blockで表示
            cropArea.style.display ="block";
        }
    }

    var saveCount = 0;
    imgview.addEventListener('click',function(e){
        var t=e.target;
        if(t.nodeName=="IMG"){
          console.log(t.id);
          saveCount = Number(t.id.slice(-1));
        }
      });

    
    let cropper = null;
    const cropAspectRatio = NaN; //Not a Number の略
        
    const scaledWidth = 100;



    const cropImage = function(){

        if (fileNum == 0) {
        return; //実行を停止
        }   
        var image = new Image();

        image.onload = function(){
            var canvas = document.getElementById("sourceCanvas");
            var scale = scaledWidth / image.width;
            var ctx = canvas.getContext("2d");
            canvas.width = image.width ;
            canvas.height = image.height;
            // canvas.style.width = String(canvas.width / devicePixelRatio) + "px";
            // canvas.style.height = String(canvas.height / devicePixelRatio) + "px";
            //console.log(String(canvas.height / devicePixelRatio));
            ctx.drawImage(image, 0, 0, image.width, image.height, 0, 0, canvas.width, canvas.height);
            
            if (cropper != null) {
                // 画像を再読み込みした場合は破棄が必要
                cropper.destroy();
            }
                cropper = new Cropper(canvas, {
                    aspectRatio: cropAspectRatio,
                    movable: false,
                    scalable: false,
                    zoomable: false,
                    data: {
                        width: canvas.width,
                        height: canvas.width * 2
                    },
                    crop: function (event) {
                        const croppedCanvas = document.getElementById("croppedCanvas");
                        let ctx = croppedCanvas.getContext("2d");
                        let croppedImageWidth = cropper.getData().width;
                        //console.log(croppedImageWidth);
                        croppedCanvas.width = cropper.getData().width;//本来の横幅
                        croppedCanvas.height = cropper.getData().height;
                        // croppedCanvas.style.width = String(croppedCanvas.width / devicePixelRatio) + "px";//見かけ上の横幅
                        // croppedCanvas.style.height = String(croppedCanvas.height / devicePixelRatio) + "px";
                        ctx.drawImage(image,
                            event.detail.x, event.detail.y, event.detail.width, event.detail.height,
                            0, 0, croppedCanvas.width, croppedCanvas.height);
                    }
                })
            };
        image.src = imgsrc[saveCount];
    }

    const cropEnd = function(){
        const croppedCanvas = document.getElementById("croppedCanvas");
        const imagePost = document.getElementById("imagePost");
        var croppedview = document.getElementById("img_"+String(saveCount));
        croppedview.src = croppedCanvas.toDataURL();
        imagePost.src = croppedCanvas.toDataURL();

    }

    var crop_btn = document.getElementById("crop_btn");
    crop_btn.addEventListener('click', cropStart, false);
    crop_btn.addEventListener('click', cropImage, false);

    var endCrop = document.getElementById("endCrop");
    endCrop.addEventListener("click", cropEnd, false);
    endCrop.addEventListener('click', cropStart, false);
});



    //デバイスにダウンローどするやつ
    /*document.getElementById("save").onclick = (event) => {
    let canvas = document.getElementById("croppedCanvas");
    window.localStorage[`img${saveCount}`] = canvas.toDataURL("image/jpg");//base64方式のtxtで保存される、img1,2,3...
    saveCount++;
    //localstrageを消すにはlocalstrage.crear();
    //間違えてsaveしてしまった時用の消す画面が必要？
    if(saveCount>0){
        var saveOK = document.createElement('p');
        saveOK.textContent = "saveOK";
        document.getElementById("body").appendChild(saveOK);
    }
    }

    document.getElementById("download").onclick = (event) => {
    let canvas = document.getElementById("croppedCanvas");
    let link = document.createElement("a");
    link.href = canvas.toDataURL("image/jpg");
    link.download = "base_image.jpg";
    link.click();
    }*/