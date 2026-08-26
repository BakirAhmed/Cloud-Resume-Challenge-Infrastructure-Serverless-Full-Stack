// Remplacer par l'URL de sortie Terraform "api_endpoint"
const API_URL = "https://REPLACE_ME.execute-api.eu-west-3.amazonaws.com/count";

async function loadVisitCount() {
  const el = document.getElementById("visit-count");
  try {
    const res = await fetch(API_URL);
    const data = await res.json();
    el.textContent = data.visits;
  } catch (err) {
    el.textContent = "N/A";
    console.error("Erreur lors de la récupération du compteur :", err);
  }
}

loadVisitCount();
