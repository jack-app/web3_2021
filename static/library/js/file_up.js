var fileNum = 0;
var imgsrc = [];

window.addEventListener('DOMContentLoaded', function(){
    $(function() { 
            $('input[name="file[]"]').on("change",function(e){
                let fs = this.files;
                fileNum = fs.length;
                imgsrc = [];
                $("#imgview").html("");
                for(let i=0; i < fileNum ;i++){
                    let fR = new FileReader();
                    fR.onload = function(e){
                    imgsrc.push(e.target.result);
                    $('<div>').appendTo('#imgview');
                    $('<img>', { 'class':'pic', 'alt':fs[i].name, 'src': imgsrc[i], 'id': "img_"+String(i)}
                    ).appendTo('#imgview');
                    $('</div>').appendTo('#imgview');
                }
                fR.readAsDataURL(fs[i]);

            }
        });
    })
});


