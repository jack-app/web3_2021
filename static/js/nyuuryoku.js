const nyuuryokuStart = function() {
    if (nyuuryoku.style.display == "block") {
        // noneで非表示
        nyuuryoku.style.display = "none";
        filename.style.display = "none";
    } else {
        // blockで表示
        nyuuryoku.style.display = "block";
        filename.style.display = "block";
    }
}

const changeFile = function() {
    var gakuseki =
        filename.value = String(readCookie(gakuseki)) + String(readCookie(myname));
}

const cookieKousin = function() {
    const gakuseki = document.getElementById("gakuseki").value;
    const myname = document.getElementById("myname").value;
    let preview = document.getElementById("fileNameInput").value;
    preview = `${gakuseki}` + "_" + `${myname}`;
    if (gakuseki === undefined || myname === undefined) {
        alert("学籍番号と名前を入力して下さい");
    } else {
        console.log("writeCookieの前までは正常");
        writeCookie("gakuseki", `${gakuseki}`);
        writeCookie("myname", `${myname}`);
    }
    sendData();
}

const sendData = function() {
    var hostUrl = '/';
    let gakuseki;

    $.ajax({
        url: hostUrl,
        type: 'POST',
        dataType: 'json',
        data: { "gakuseki": gakuseki, "myname": myname },
        timeout: 3000,
    }).done(function(data) {
        alert("名前登録完了");
    }).fail(function(XMLHttpRequest, textStatus, errorThrown) {
        alert("登録が正常に完了しませんでした");
        console.log(errorThrown);
    })
}
