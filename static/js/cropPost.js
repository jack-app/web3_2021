$(function() {
    $('#ajax-button').click(
        function() {
            console.log("send!");
            var hostUrl = '/';
            let canvas = document.getElementById("croppedCanvas");
            var imgData = canvas.toDataURL("image/jpg");
            $.ajax({
                url: hostUrl,
                type: 'POST',
                dataType: 'json',
                data: { img: imgData },
                timeout: 3000,
            }).done(function(data) {
                alert("ok");
            }).fail(function(XMLHttpRequest, textStatus, errorThrown) {
                alert("error");
            })
        });
});
