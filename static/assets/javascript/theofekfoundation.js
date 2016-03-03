$(document).ready(function() {
	var content_wrapper = $("#content-wrapper");
	content_wrapper.css('top', $('#navbar-top').height()).height($(window).outerHeight(true) - $('#navbar-top').outerHeight());
	vert_padding_align();
	// if (document.getElementById('navbar-top') !== null)
	// 	document.body.style.paddingTop = document.getElementById('navbar-top').clientHeight + "px";
});

function vert_padding_align() {
	var vert_padding_align = document.getElementsByClassName('vert-padding-align');
	for (var i = 0, elem = $(vert_padding_align[i]); i < vert_padding_align.length; i++, elem = $(vert_padding_align[i]))
		elem.css('padding-top', (elem.parent().height() - elem.height()) / 2 + "px");
}

function fit_parent() {
	var fit_parents = document.getElementsByClassName("fit-parent");
	var fp = fit_parents, elem;
	for (var i = 0; i < fp.length; i++) {
		elem = $(fp[i]);
		while (elem.height() > elem.parent().height())
		    elem.css('font-size', (parseInt(elem.css('font-size')) - 1) + "px" );
	}
}

function vert_align() {
	var vert_aligns = document.getElementsByClassName("vert-align");

	var va = vert_aligns, elem;
	for (var i = 0; i < va.length; i++) {
		elem = $(va[i]);
		elem.css('margin-top', (elem.parent().height() - elem.height()) / 2 + "px");
	}
}

function window_at(elem) {
	return $(document).scrollTop() + $(window).height() - $('.footer').outerHeight(true) >= elem.position().top;
}

function redirect(url) {
	window.location.href = url;
}