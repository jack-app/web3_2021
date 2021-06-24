var saveCount = 0;
    let cropper = null;
    const cropAspectRatio = NaN;
    
    const scaledWidth = 1000;

    const cropImage = function (evt) {
        const files = evt.target.files;
        if (files.length == 0) {
            return;
        }
        let file = files[0];
        let image = new Image();
        let reader = new FileReader();
        reader.onload = function (evt) {
            image.onload = function () {
                let scale = scaledWidth / image.width;
                console.log(image.width);
                let imageData = null;
                {
                    const canvas = document.getElementById("sourceCanvas");
                    
                    {
                        let ctx = canvas.getContext("2d");
                        canvas.width = image.width * scale;
                        canvas.height = image.height * scale;
                        canvas.style.width = String(canvas.width / devicePixelRatio) + "px";
                        canvas.style.height = String(canvas.height / devicePixelRatio) + "px";
                        console.log(String(canvas.height / devicePixelRatio));
                        ctx.drawImage(image, 0, 0, image.width, image.height, 0, 0, canvas.width, canvas.height);
                    }
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
                                {
                                    let ctx = croppedCanvas.getContext("2d");
                                    let croppedImageWidth = cropper.getData().width;
                                    console.log(croppedImageWidth);
                                    croppedCanvas.width = cropper.getData().width;//本来の横幅
                                    croppedCanvas.height = cropper.getData().height;
                                    croppedCanvas.style.width = String(croppedCanvas.width / devicePixelRatio) + "px";//見かけ上の横幅
                                    croppedCanvas.style.height = String(croppedCanvas.height / devicePixelRatio) + "px";
                                    ctx.drawImage(image,
                                        event.detail.x / scale, event.detail.y / scale, event.detail.width / scale, event.detail.height / scale,
                                        0, 0, croppedCanvas.width, croppedCanvas.height
                                    );
                                }
                            }
                    });
                }
            }
            image.src = evt.target.result;
        }
        reader.readAsDataURL(file);
    }

    const uploader = document.getElementById('uploader');
    uploader.addEventListener('change', cropImage);
    