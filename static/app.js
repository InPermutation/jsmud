var Scrollback = 'uninitialized';

function send(cmd){
	$.get('/cmd', {cmd: cmd}, function(data){Scrollback.write(data); $("#input").val('').removeAttr('disabled'); });
}

jQuery(function($){
	const BUFFER = 24;
Scrollback = {
		lines: [],
		write: function(s){
			var lin = Scrollback.lines;
			lin.push(s);
			if(lin.length > BUFFER)
				Scrollback.lines = lin = lin.slice(lin.length - BUFFER);
			$('#console').html(lin.join('<br/>'));
		}
	};
Scrollback.write('Welcome to jsmud!');
for(var i = 0; i < BUFFER- 1; i++)
	Scrollback.write('');
	$('#input').focus();
	$('form').submit(function(e){ 
		e.preventDefault();
		var s = $('#input').attr('disabled','disabled').val();

		Scrollback.write('&gt; ' + s);
	       	send(s);
       	});
});
