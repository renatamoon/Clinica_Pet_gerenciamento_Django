function gera_cor(qtd = 1) {
  var bg_color = [];
  var border_color = [];
  for (let i = 0; i < qtd; i++) {
    let r = Math.random() * 255;
    let g = Math.random() * 255;
    let b = Math.random() * 255;
    bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`);
    border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`);
  }

  return [bg_color, border_color];
}



function renderiza_faturamento_mensal() {
  const ctx = document.getElementById("faturamento_mensal").getContext("2d"); 
  const myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez",
      ],
      datasets: [
        {
          label: "faturamento",
          data: [
            15000.00, 18000.00, 30000.00, 52000.00, 28000.00, 68000.00, 12500.00, 19000.00, 38000.00, 56500.00, 25000.00,
            39.8,
          ],
          backgroundColor: "#CB1EA8",
          borderColor: "#FFFFFF",
          borderWidth: 0.2,
        },
      ],
    },
  });
}




function renderiza_consultas_mensal() {
  const ctx = document.getElementById("consultas_mensal").getContext("2d"); 
  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez",
      ],
      datasets: [
        {
          label: "consultas",
          data: [20, 22, 15, 56, 20, 80, 52, 20, 22, 45, 47, 68],
          backgroundColor: "	#00cccc",
          borderColor: "#FFFFFF",
          borderWidth: 0.2,
        },
      ],
    },
  });
}


function renderiza_animais_atendidos() {
  const ctx = document.getElementById("animais_atendidos").getContext("2d");
  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez",
      ],
      datasets: [
        {
          indexAxis: "y",
          label: "animais atendidos",
          data: [50, 60, 20, 80, 25, 101, 58, 78, 60, 20, 32, 25],
          backgroundColor: "#3300cc",
          borderColor: "#FFFFFF",
          borderWidth: 0.2,
          responsive: true,
          borderWidth: 0.2,
          elements: {
            bar: {
              borderWidth: 2,
            },
          },
        },
      ],
    },
  });
}


function renderiza_lotacao_clinica() {
  const ctx = document.getElementById("lotacao_clinica").getContext("2d");
  const myChart = new Chart(ctx, {
    type: "line",
    scales: {
      x: {
        display: true,
      },
      y: {
        display: true,
        type: "logarithmic",
      },
    },
    data: {
      labels: [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez",
      ],
      datasets: [
        {
          label: "lotação da clínica",
          data: [50, 60, 20, 80, 25, 101, 58, 78, 60, 20, 32, 25],
          backgroundColor: "red",
          borderColor: "#FFFFFF",
          borderWidth: 0.2,
          display: true,
          responsive: true,
          borderWidth: 0.2,
          fill: true,
          elements: {
            bar: {
              borderWidth: 2,
            },
          },
        },
      ],
    },
  });
}