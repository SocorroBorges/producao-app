document.addEventListener("DOMContentLoaded", function () {

    document.querySelectorAll(".btn-editar").forEach(botao => {
        botao.addEventListener("click", function () {

            const id = this.dataset.id
            const nome = this.dataset.nome
            const custo = this.dataset.custo
            const unidade = this.dataset.unidade

            abrirModal(id, nome, custo, unidade)
        })
    })
})

function abrirModal(id, nome, custo, unidade) {
    document.getElementById("modal").style.display = "block"

    document.getElementById("edit-id").value = id
    document.getElementById("edit-nome").value = nome
    document.getElementById("edit-custo").value = custo
    document.getElementById("edit-unidade").value = unidade
}

function fecharModal() {
    document.getElementById("modal").style.display = "nome"
}

function salvarEdicao() {
    const id = document.getElementById("edit-id").value
    const nome = document.getElementById("edit-nome").value
    const custo = document.getElementById("edit-custo").value
    const unidade = document.getElementById("edit-unidade").value

    fetch("/editar_inline", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: id,
            nome: nome,
            custo_unitario: custo,
            unidade_medida: unidade
        })
    })
    .then(() => location.reload())
}