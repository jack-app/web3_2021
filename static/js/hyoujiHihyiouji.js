window.onload = function() {
    document.getElementById("cropArea").style.display = "none";
    const nyuuryoku = document.getElementById("nyuuryoku");
    nyuuryoku.style.display = "none";
    const filename = document.getElementById("filename");
    filename.style.display = "none";
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


