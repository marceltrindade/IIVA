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

      let tabela = document.querySelector("#tabela table");
      while (tabela.rows.length > 1) {
        tabela.deleteRow(1);
      }
      for (let i = 0; i < aulas.length; i++) {
        let aula = aulas[i];
        let linha = tabela.insertRow();
        linha.innerHTML =
          "<td>" +
          aula.aluno_nome +
          "</td>" +
          "<td>" +
          aula.aula_numero +
          "</td>" +
          "<td>" +
          aula.topico +
          "</td>" +
          "<td>" +
          aula.status +
          "</td>";
      }
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

// TODO: badge logs pendentes - blocker: não tem coluna log_criado

carregarAulasHoje();
carregarAlunosAtivos();
