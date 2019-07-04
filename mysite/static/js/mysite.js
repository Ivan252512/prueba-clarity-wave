$(document).ready(function () {

    //Add question
    $("#add_question").submit(function () {
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: $(this).data('id'),
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: {
                'question_text': $('#question').val() // from form
            },
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success: function () {
                location.reload();
            }
        });
        return false;
    });

    //Add choices
    $("#add_choice").submit(function () {
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: $(this).data('id'),
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: {
                'choice_text': $('#choice').val() // from form
            },
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success: function () {
                location.reload();
            }
        });
        return false;
    });


    //Delete question
    $("#delete").submit(function () {
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "DELETE",
            url: $(this).data('id'),
            headers: {
                "X-CSRFToken": csrftoken
            },
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success: function () {
                location.reload();
            }
        })
    });

    //Vote
    $.vote = function () {
        $('input').on('click', function () {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: "POST",
                url: $(this).data('id'),
                headers: {
                    "X-CSRFToken": csrftoken
                },
                csrfmiddlewaretoken: '{{ csrf_token }}',
                success: function () {
                    location.reload();
                }
            });
            return false;
        });
    };

    $("#vote").submit(function () {
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: $(this).data('id'),
            headers: {
                "X-CSRFToken": csrftoken
            },
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success: function () {
                location.reload();
            }
        });
        return false;
    });

});