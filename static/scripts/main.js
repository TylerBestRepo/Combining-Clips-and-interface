var fileButtonSelect = document.getElementById('my-file');


$('#my-button').click(function(){
    $('#my-file').click();
    console.log(fileButtonSelect.value);
});