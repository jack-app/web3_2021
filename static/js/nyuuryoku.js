window.onload = function() {
    const nyuuryoku = document.getElementById("nyuuryoku");
    nyuuryoku.style.display ="none";
};


const nyuuryokuStart = function(){
        if(nyuuryoku.style.display=="block"){
		// noneで非表示
		nyuuryoku.style.display ="none";
	    }else{
		// blockで表示
		nyuuryoku.style.display ="block";
	    }
    }
    

const cookieKousin = function(){
        const gakuseki = document.getElementById("gakuseki").value;
        const myname = document.getElementById("myname").value;
        if(gakuseki===undefined||myname===undefined){
            alert("学籍番号と名前を入力して下さい");
        }else{
            console.log("writeCookieの前までは正常")
            writeCookie("gakuseki",`${gakuseki}`)
            writeCookie("myname",`${myname}`);
        }
        sendData();
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
