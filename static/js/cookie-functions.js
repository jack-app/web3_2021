

 // cookieの値を読み書きする要素
 //これ使ったらうまくいかなかったけど、一応残しておく
 function defineAll(){
    var keys = ['namae','bango','other'];
    var ids = ['input1','input2','input3'];
    
}
    

function writeAll(){
    //cookieのkeyを追加したかったら、keysとidsに追加お願いします。
    //varをこの関数の外においたらなぜかうまく動作しないです
    var keys = ['namae','bango','other'];
    var ids = ['input1','input2','input3'];
    for(let i=0;i<keys.length;i++){
        const inputId = ids[i];
        const key = keys[i];
        var value = document.getElementById(inputId).value;
        writeCookie(key,value);
    }
}

function deleteAll(){
    //cookieのkeyを追加したかったら、keysとidsに追加お願いします。
    //varをこの関数の外においたらなぜかうまく動作しないです
    var keys = ['namae','bango','other'];
    var ids = ['input1','input2','input3'];
    for(i=0;i<keys.length;i++){
        const inputId = ids[i];
        const key = keys[i];
        var value = document.getElementById(inputId).value;
        deleteCookie(key);
        
    }
}

// 書き込み一つだけ
function writeCookie(key,value) {  
      document.cookie = `${key}`+ "=" + value;
      console.log(document.cookie);
  
}

// 読み込み一つだけ
function readCookie() {
  var tmp = document.cookie;
  var cookieValue = document.cookie.replace(/(?:(?:^|.*;\s*)mycookie\s*\=\s*([^;]*).*$)|^.*$/, "$1");
  input1.value = cookieValue;
  console.log(document.cookie);
}

// 削除一つだけ
function deleteCookie(key) {
  document.cookie = `${key}=; expires=0`;
  console.log(document.cookie);
}