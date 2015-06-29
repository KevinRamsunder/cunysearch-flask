function setInst(value) {
	$.post('/instChange', {
		newInst: value
	})

	.done(function() {
		term();
		dept();
	});
}

function setTerm(value) {
	$.post('/termChange', {
		newTerm: value
	})

	.done(function() {
		dept();
	});
}

function setDept(value) {
	$.post('/deptChange', {
		newDept: value
	});
}

function term() {
	$.post('/term', {
	})

	.done(function (data) {
		$('#terms').empty();

		for(var key in data) {
			var school = "<option class = '" + data[key] + "'>" + key + "</option>";
			$('#terms').append(school);
		}

		$('#terms').combobox('refresh');
	});
}

function dept() {
	$.post('/dept', {
	})

	.done(function (data) {
		$('#departments').empty();

		for(var key in data) {
			var school = "<option class = '" + data[key] + "'>" + key + "</option>";
			$('#departments').append(school);
		}

		$('#departments').combobox('refresh');
	});
}

function getResults(checkbox) {
	$('#table').hide();

	$.post('/results', {
		checkboxValue : checkbox
	})
	
	.done(function (data) {
		var parsedData = $.parseJSON(data);

		$.post('/getTable', {
		})
		.done(function (tableText) {
			$('div#puttable').html('');
			$('div#puttable').append(tableText);
			$('#table').bootstrapTable({data: parsedData});
			$('#table').show();
		});
	});
}

function actionFormatter(value, row, index) {
    return [
        '<a class="loadclassdata" title="Load Class Data">',
        '<i class="glyphicon glyphicon-circle-arrow-right"></i>',
        '</a>'
    ].join('');
}

window.actionEvents = {
    'click .loadclassdata': function (e, value, row, index) {
        var htmlKey = row['htmlKey'];

        $.post('/getSeats', {
        	key : htmlKey
		})

		.done(function(data) {
			var parsedData = $.parseJSON(data);
			$('#table').bootstrapTable('updateRow', {
				index: index,
				row: {
					cap: parsedData[0]['classcapacity'],
					enroll: parsedData[0]['enrollmenttotal'],
					avail:  parsedData[0]['availableseats']
				}
			});

			$('#table').bootstrapTable('refresh');
		});
    }
};
