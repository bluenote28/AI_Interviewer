var i = 0;
var speed = 20

function typeWriter(txt) {

    if (i < txt.length) {

        document.getElementById("lastanswer").innerHTML += txt.charAt(i);
        i++;
        setTimeout(() => typeWriter(txt), speed);
    }
}