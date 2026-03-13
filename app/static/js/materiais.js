document.addEventListener("DOMContentLoaded", function() {

    document.querySelectorAll(".editavel").forEach(celula => {

        celula.addEventListener("blur", function(){

            const id = this.dataset.id
            const campo = this.dataset.campo
            const valor = this.innerText

            fetch("/editar_inline", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    id: id,
                    campo: campo,
                    valor: valor
                })
            })
        })
    })
})