var speed = 20;

function typeWriter(element, txt, i) {
    i = i || 0;
    if (i < txt.length) {
        element.innerHTML += txt.charAt(i);
        setTimeout(() => typeWriter(element, txt, i + 1), speed);
    }
}
