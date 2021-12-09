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
      datasets: [{
          label: "faturamento",
          data: [15000.0, 18000.0, 30000.0, 52000.0, 28000.0, 68000.0, 12500.0,
            19000.0, 38000.0, 56500.0, 25000.0, 39.8,],
          backgroundColor: "black",          
          borderColor: "purple",
          borderWidth: 4.5,
          display: true,
          responsive: true,
          fill: false,
          elements: {
            bar: {
              borderWidth: 3,
            }
          }
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
          borderWidth: 0.5,
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