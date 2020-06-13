$('.datepicker').each(function () {
    var picker = new Pikaday({
        field: this
    });
});


function success() {
    if (document.getElementById('msgInput').value === '' || document.getElementById('emailInput').value === '') {
        document.getElementById('submit').disabled = true;
    } else {
        document.getElementById('submit').disabled = false;
    }
}
