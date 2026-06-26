function rotear() {
  // Pega o hash da URL, tira o #, usa "dashboard" se não tiver nada
  let hash = window.location.hash.replace("#", "") || "dashboard";

  // Esconde todas as views
  document.getElementById("view-dashboard").style.display = "none";
  document.getElementById("view-alunos").style.display = "none";
  document.getElementById("view-aluno").style.display = "none";

  // Mostra a view correspondente ao hash
  let view = document.getElementById("view-" + hash);
  if (view) {
    view.style.display = "block";
  }
}

// Roteia quando a página carrega
rotear();

// Roteia quando o hash muda
window.addEventListener("hashchange", rotear);

function carregarAulasHoje() {
  let hoje = new Date().toISOString().split("T")[0];
  fetch("http://localhost:8000/aulas?data=" + hoje)
    .then(function (resposta) {
      return resposta.json();
    })
    .then(function (aulas) {
      document.querySelector(
        "#stats .badge:nth-child(1) .badge-num",
      ).textContent = aulas.length;
    });
}

function carregarAlunosAtivos() {
  fetch("http://localhost:8000/alunos")
    .then(function (resposta) {
      return resposta.json();
    })
    .then(function (alunos) {
      document.querySelector(
        "#stats .badge:nth-child(2) .badge-num",
      ).textContent = alunos.length;
    });
}
carregarAulasHoje();
carregarAlunosAtivos();
