function send() {
    var f_n = document.getElementById("f_n").value;
    var l_n = document.getElementById("l_n").value;
    var pat = document.getElementById("pat").value;
    var gend = document.getElementById("gend").value;
    var form_data = new FormData();
    form_data.append('file', $('input[type=file]')[0].files[0]);
    form_data.append("f_n", f_n);
    form_data.append("l_n", l_n);
    form_data.append("pat", pat);
    form_data.append("gend", gend);
    $.ajax({
        type: 'POST'
        , url: '/make_by_text'
        , data: form_data
        , contentType: false
        , cache: false
        , processData: false
        , success: function (data) {
            window.location.href = data;
        }
    , });
}
