export function renderCharts(data) {
    const labels = data.map(t => new Date(t.date).toLocaleDateString());
    const amounts = data.map(t => t.amount);
    const types = [...new Set(data.map(t => t.transaction_type))]; // Unique transaction types


    // Get chart contexts
    const ctxBar = document.getElementById('bar-chart').getContext('2d');
    const ctxPie = document.getElementById('pie-chart').getContext('2d');
    const ctxLine = document.getElementById('line-chart').getContext('2d');


    // Data for charts
    const barData = types.map(type => data.filter(t => t.transaction_type === type).reduce((sum, t) => sum + t.amount, 0));
    const pieData = types.map(type => data.filter(t => t.transaction_type === type).length);


    // Define colors dynamically
    const colors = [
        'rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)'
    ];


    // Bar Chart (Transaction Volume by Type)
    if (!window.barChart) {
        window.barChart = new Chart(ctxBar, {
            type: 'bar',
            data: {
                labels: types,
                datasets: [{
                    label: 'Transaction Amount (RWF)',
                    data: barData,
                    backgroundColor: colors.slice(0, types.length),
                    borderColor: colors.slice(0, types.length).map(c => c.replace('0.6', '1')),
                    borderWidth: 1
                }]
            },
            options: { responsive: true, scales: { y: { beginAtZero: true } } }
        });
    } else {
        window.barChart.data.labels = types;
        window.barChart.data.datasets[0].data = barData;
        window.barChart.update();
    }


    // Pie Chart (Transaction Distribution)
    if (!window.pieChart) {
        window.pieChart = new Chart(ctxPie, {
            type: 'pie',
            data: {
                labels: types,
                datasets: [{
                    label: 'Transaction Types',
                    data: pieData,
                    backgroundColor: colors.slice(0, types.length),
                    borderColor: colors.slice(0, types.length).map(c => c.replace('0.6', '1')),
                    borderWidth: 1
                }]
            },
            options: { responsive: true }
        });
    } else {
        window.pieChart.data.labels = types;
        window.pieChart.data.datasets[0].data = pieData;
        window.pieChart.update();
    }


    // Line Chart (Transaction Trends Over Time)
    if (!window.lineChart) {
        window.lineChart = new Chart(ctxLine, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Transaction Amount (RWF)',
                    data: amounts,
                    backgroundColor: 'rgba(10, 31, 68, 0.2)',
                    borderColor: 'rgba(10, 31, 68, 1)',
                    borderWidth: 1,
                    fill: true
                }]
            },
            options: { responsive: true, scales: { y: { beginAtZero: true } } }
        });
    } else {
        window.lineChart.data.labels = labels;
        window.lineChart.data.datasets[0].data = amounts;
        window.lineChart.update();
    }
}

