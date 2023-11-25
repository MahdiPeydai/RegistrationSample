const csrftoken = $('[name=csrfmiddlewaretoken]').val();

$(document).ready(function() {
    $('.delete-btn').each(function() {
        $(this).on('click', function() {
            const user_id = $(this).data('id')
            $.ajax({
                url: $(this).data('url'),
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function (data) {
                    if (document.getElementById('message')) {
                        document.getElementById('message').remove()
                    }
                    let message = document.createElement('p');
                    message.id = 'message'
                    message.classList.add('text-success');
                    message.textContent = 'با موفقیت حذف شد';
                    document.getElementById('message-container').appendChild(message);
                    document.getElementById('user-' + user_id).remove();
                },
                error: function (xhr, status, error) {
                    if (document.getElementById('message')) {
                        document.getElementById('message').remove()
                    }
                    let message = document.createElement('p');
                    message.id = 'message'
                    message.classList.add('text-danger');
                    message.textContent = 'خطا';
                    document.getElementById('message-container').appendChild(message);
                }
            });
            return false;
        })
    })
});