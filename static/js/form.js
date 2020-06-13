$(document).ready(function () {

    $('form').on('submit', function (event) {

        $.ajax({
            data: {
                name: $('#nameInput').val(),
                email: $('#emailInput').val(),
                msg: $('#msgInput').val(),
                number: $('#numberInput').val()
            },
            type: 'POST',
            url: '/process'
        })
            .done(function (data) {

                if (data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                } else if (data.success) {
                    $('form').trigger('reset')
                    $('#successAlert').text(data.success).show();
                    $('#errorAlert').hide();
                }
            });

        event.preventDefault();

    });

});