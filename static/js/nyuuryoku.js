const changeFilename = function(){
        var gakuseki = readCookie(gakuseki);
        let filename = String(readCookie(gakuseki))+"_"+String(readCookie(myname));
        const filenamePreview = document.getElementById("filenamePreview");
        filenamePreview.innerHTML = filename;
}

const changeStamp = function(){
    let a = getElementById("filenamePreview");
    let b = String(readCookie(gakuseki))+String(readCookie(myname));
    a.innerHTML = "<p>`${b}`</p>";
}

const cookieKousin = function(){
        let gakuseki = document.getElementById("gakuseki").value;
        let myname = document.getElementById("myname").value;
        //let preview = document.getElementById("fileNameInput").value;
        //preview = `${gakuseki}`+"_"+`${myname}`;
        if(gakuseki===undefined||myname===undefined){
            alert("学籍番号と名前を入力して下さい");
        }else{
            console.log("writeCookieの前までは正常");
            writeCookie("gakuseki",`${gakuseki}`);
            writeCookie("myname",`${myname}`);
        }
        sendData();
        changeStamp();
        changeFilename();
}
    


const sendData =function() {
        console.log("send!");
        var hostUrl= '/';
        let gakuseki;
        $.ajax({
            url: hostUrl,
            type:'POST',
            dataType: 'json',
            data : {"gakuseki" : gakuseki,"myname":myname},
            timeout:3000,
        }).done(function(data) {
                          alert("名前登録完了");
        }).fail(function(XMLHttpRequest, textStatus, errorThrown) {
                         alert("error");
        })
}
