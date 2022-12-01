var btn = document.getElementById('adapt_open_btn');
var div = document.getElementById('adapt_background');
var close = document.getElementById('adapt_close_button');

btn.onclick = function show() {
    div.style.display = "block";
}

close.onclick = function close() {
    div.style.display = "none";
}


var btn2 = document.getElementById('adapt_open_btn2');
var div2 = document.getElementById('adapt_cpu_background');
var close2 = document.getElementById('adapt_cpu_close_button');

btn2.onclick = function show() {
    div2.style.display = "block";
}

close2.onclick = function close() {
    div2.style.display = "none";
}