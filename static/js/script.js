let lastScrollTop = 0;

// Reemplazamos este bloque para verificar si barraScroll existe
window.addEventListener("scroll", function () {
    const barra = document.getElementById("barraScroll");
    if (barra) {
        if (window.scrollY > 100) {
            barra.classList.add("visible");
        } else {
            barra.classList.remove("visible");
        }
    }
});

document.addEventListener('DOMContentLoaded', () => {
    function mostrarMensaje(id, texto, incluirBoton = false) {
        const existente = document.querySelector('.mensaje-dinamico');
        if (existente) {
            existente.remove();
        }

        const mensaje = document.createElement('div');
        mensaje.className = 'mensaje-dinamico visible';
        mensaje.innerText = texto;

        if (incluirBoton) {
            const boton = document.createElement('a');
            boton.href = "https://wa.me/593968017735";
            boton.className = 'boton-whatsapp';
            boton.target = '_blank';
            boton.innerHTML = `<img src="/static/images/whatsapp.png" alt="WhatsApp"> Escríbenos por WhatsApp`;
            mensaje.appendChild(document.createElement('br'));
            mensaje.appendChild(boton);
        }

        const contenedor = document.getElementById('mensaje-dinamico-container');
        if (contenedor) {
            contenedor.appendChild(mensaje);

            setTimeout(() => {
                mensaje.classList.remove('visible');
                setTimeout(() => mensaje.remove(), 500);
            }, 3000);
        }
    }

    const iconoCompra = document.getElementById('icono-compra');
    const iconoPagos = document.getElementById('icono-pagos');
    const iconoWhatsapp = document.getElementById('icono-whatsapp');

    if (iconoWhatsapp) {
        iconoWhatsapp.addEventListener('click', (e) => {
            e.preventDefault();
            mostrarMensaje('whatsapp', '📲 Escríbenos directo a WhatsApp para hacer tu pedido.', true);
        });
    }

    // Scroll indicator dinámico corregido
    const dots = document.querySelectorAll('.scroll-indicator .dot');
    const sections = document.querySelectorAll('.seccion-scroll'); // Solo secciones importantes

    window.addEventListener('scroll', () => {
        let index = 0;
        sections.forEach((section, i) => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= window.innerHeight / 2) {
                index = i;
            }
        });

        dots.forEach(dot => dot.classList.remove('active'));
        if (dots[index]) {
            dots[index].classList.add('active');
        }
    });

    // NUEVO: scroll suave al hacer clic en los puntos
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
            if (sections[i]) {
                sections[i].scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
