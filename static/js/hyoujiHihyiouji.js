window.onload = function() {
    document.getElementById("cropArea").style.display = "none";
    const nyuuryoku = document.getElementById("nyuuryoku");
    nyuuryoku.style.display = "none";
    const filename = document.getElementById("filename");
    filename.style.display ="none";
    const stamp = document.getElementById("stamp");
    stamp.style.display = "none";
};

const cropStart = function() {
    const uploader = document.getElementById('uploader');
    const cropArea = document.getElementById("cropArea");

    if (cropArea.style.display == "block") {
        // noneで非表示
        cropArea.style.display = "none";
    } else {
        // blockで表示
        cropArea.style.display = "block";
    }
}

const nyuuryokuStart = function(){
    if(nyuuryoku.style.display=="block"){
        // noneで非表示
        nyuuryoku.style.display ="none";
	}else{
        // blockで表示
        nyuuryoku.style.display ="block";
	}
}

const filenameStart = function(){
    if(filename.style.display=="block"){
        // noneで非表示
        filename.style.display ="none";
    }else{
        // blockで表示
        filename.style.display ="block";
    }
}

const stampStart = function(){
    if(stamp.style.display=="block"){
        // noneで非表示
        stamp.style.display ="none";
    }else{
        // blockで表示
        stamp.style.display ="block";
    }
}
