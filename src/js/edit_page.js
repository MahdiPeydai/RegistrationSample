const csrftoken = $('[name=csrfmiddlewaretoken]').val();

$(document).ready(function() {
    $('#update-form').submit(function(event) {
        event.preventDefault();

        const formData = $(this).serialize();

        $.ajax({
            url: $(this).data('url'),
            method: 'PUT',
            data: formData,
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function() {
                if (document.getElementById('message')) {
                        document.getElementById('message').remove()
                    }
                let message = document.createElement('p');
                message.id = 'message'
                message.classList.add('text-success');
                message.textContent = 'با موفقیت ویرایش شد';
                document.getElementById('message-container').appendChild(message);
            },
            error: function(xhr) {
                if (document.getElementById('message')) {
                        document.getElementById('message').remove()
                    }
                let message = document.createElement('p');
                message.id = 'message'
                message.classList.add('text-danger');
                message.textContent = 'خطا';
                for (var key in xhr.responseJSON) {
                    if (Object.prototype.hasOwnProperty.call(xhr.responseJSON, key)) {
                        message.textContent =message.textContent + ' , ' + xhr.responseJSON[key];
                    }
                }
                document.getElementById('message-container').appendChild(message);
            }
        });
        return false;
    })
});
