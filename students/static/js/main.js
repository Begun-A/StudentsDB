function initJournal() {
    var indicator = $('#ajax-progres-indicator')
    $('.day-box input[type="checkbox"]').click(function (event) {
        var box = $(this)
        $.ajax(box.data('url'), {
            'type': "POST",
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('student-id'),
                'date': box.data('date'),
                'present': box.is(':checked') ? '1' : '',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'beforeSend': function (xhr, setting) {
                indicator.show()
            },
            'error': function (xhr, status, error) {
                alert(error)
                indicator.hide()
            },
            'success': function (data, status, xhr) {
                indicator.hide()
            }
        });
    });

};

function initGroupSelector() {
    $('#group-selector select').change(function (event) {
        var group = $(this).val()
        if (group) {
            $.cookie('current_group', group, {'path': '/', 'expires': 365});

        }
        else {
            $.removeCookie('current_group', {'path': '/'});
        }
        location.reload()

        return true;
    })
};

function initGroupPresent() {
    $('.group-present').click(function (event) {
        var group = $(this).val()
        if (group) {
            $.cookie('current_group', group, {'path': '/', 'expires': 365});

        }
        else {
            $.removeCookie('current_group', {'path': '/'});
        }

        return true;
    })
};

function initDataField() {
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD'
    }).on('dp.hide', function (event) {
        $(this).blur();
    });
};

function initEditStudentPage() {
    $('a.student-edit-form-link').click(function (event) {
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'type': 'GET',
            'dataType': "html",
            'success': function (data, status, xhr) {
                if (status != 'success') {
                    alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
                    return false;
                }
                var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                initEditStudentForm(form, modal);

                modal.modal('show');
            },
            'error': function () {
                alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
                return false;
            }
        });
        return false
    });
}

function initEditStudentForm(form, modal){
    initDataField();
    form.find('input[name="cancel_button"]').click(function(event){
        modal.modal('hide');
        return false;
    });

    form.ajaxForm({
        'dataType' : 'html',
        'error': function(){
            alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
            return false;
        },
        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');

            modal.find('.modal-body').html(html.find('.alert'));

            if (newform.length > 0){
                modal.find('.modal-body').append(newform);
                initEditStudentForm(newform, modal);
            }
            else{
              setTimeout(function(){location.reload(true);},500);
            }
        }
    });
}

$(document).ready(function () {
    initJournal();
    initGroupSelector();
    initGroupPresent();
    initDataField();
    initEditStudentPage();
})


