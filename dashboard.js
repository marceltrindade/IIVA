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
