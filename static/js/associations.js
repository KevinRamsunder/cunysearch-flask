// activate combobox
$('#institutions').combobox();
$('#terms').combobox();
$('#departments').combobox();

// footer
$('#footer').click(function() {
	dept();
	return false;
});

// inst select
$('#institutions').on('change', function() {
	var value = this.value;

    if(value == null) {
        value = $('li.active').attr('data-value');
    }

    setInst(value);
	return false;
});

// term select
$('#terms').on('change', function() {
	var value = this.value;

    if(value == null) {
        value = $('li.active').attr('data-value');
    }

    setTerm(value);
    return false;
});

// dept select
$('#departments').on('change', function() {
	var value = this.value;

    if(value == null) {
        value = $('li.active').attr('data-value');
    }

    setDept(value);
    return false;
});

// submit query
$('#submit').on('click', function() {
    var checkbox = $('#inlineCheckbox').is(':checked');
    getResults(checkbox);
    return false;
});