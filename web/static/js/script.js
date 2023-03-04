$(document).ready(function() {
    function incrementIdName(template) {
        template.find('input').each(function() {
            var name = $(this).attr('name');
            var id = $(this).attr('id');
            var index = name.match(/\d+/)[0];
            var new_index = parseInt(index) + 1;
            $(this).attr('name', name.replace(index, new_index));
            $(this).attr('id', id.replace(index, new_index));
        });
    }

    $('#add-natural-shareholder').click(function() {
        var template = $('.natural-shareholder-form:first').clone();
        console.log(template)
        template.find('input').val('');
        // make founder checkbox unchecked
        template.find('input[type=checkbox]').prop('checked', false);
        // increment name and id attributes
        incrementIdName(template);
        // add remove button
        template.append('<button class="btn btn-sm btn-danger remove-shareholder" type="button">X</button>');
        template.insertAfter('.natural-shareholder-form:last');
    });



    $('#add-legal-shareholder').click(function() {
        var template = $('.legal-shareholder-form:first').clone();
        template.find('input').val('');
        // make founder checkbox unchecked
        template.find('input[type=checkbox]').prop('checked', false);
        // increment name and id attributes
        incrementIdName(template);
        // add remove button
        template.append('<button class="btn btn-sm btn-danger remove-shareholder" type="button">X</button>');
        template.insertAfter('.legal-shareholder-form:last');
    });

    $(document).on('click', '.remove-shareholder', function() {
        $(this).parent().remove();
    });
});