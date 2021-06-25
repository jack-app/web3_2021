$(function() {
    $('#ajax-button').click(
        function() {
            console.log("send!");
            var hostUrl = '/triming';
            let canvas = document.getElementById("croppedCanvas");
            var imgData = canvas.toDataURL("image/jpg");
            axios.post(hostUrl, { img: imgData })
                .then((res) => alert("ok"))
                .catch((res) => alert(res))
        });
});
