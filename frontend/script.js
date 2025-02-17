import { renderCharts } from './chart.js';

// DOM Elements
const loadingElement = document.getElementById('loading');
const errorMessageElement = document.getElementById('error-message');
const successMessageElement = document.getElementById('success-message');
const noDataElement = document.getElementById('no-data');
const searchInput = document.getElementById('search');
const typeFilter = document.getElementById('type-filter');
const startDateFilter = document.getElementById('start-date');
const endDateFilter = document.getElementById('end-date');
const applyFiltersButton = document.getElementById('apply-filters');
const resetFiltersButton = document.getElementById('reset-filters');
const tableBody = document.getElementById('table-body');

let transactions = [];
const debugMode = true; // Enable for debugging

// Fetch transactions from backend
async function fetchTransactions() {
    loadingElement.style.display = 'block';
    errorMessageElement.style.display = 'none';
    successMessageElement.style.display = 'none';
    noDataElement.style.display = 'none';

    try {
        const response = await fetch('transactions.json'); // Updated path
        if (!response.ok) throw new Error(`Failed to load transactions: ${response.statusText}`);
        
        transactions = await response.json();
        renderData(transactions);
        showSuccess("Data loaded successfully!");
    } catch (error) {
        console.error("Error loading transactions:", error);
        errorMessageElement.textContent = "Error loading transactions. Please try again later.";
        errorMessageElement.style.display = 'block';
    } finally {
        loadingElement.style.display = 'none';
    }
}

// Render Table and Charts
function renderData(data) {
    renderTable(data);
    renderCharts(data);
}

// Render Table with Transaction Data
function renderTable(data) {
    tableBody.innerHTML = '';
    if (data.length === 0) {
        noDataElement.style.display = 'block';
    } else {
        noDataElement.style.display = 'none';
        tableBody.innerHTML = data.map(transaction => `
            <tr>
                <td>${transaction.id}</td>
                <td>${transaction.transaction_type || 'Unknown'}</td>
                <td>${transaction.amount.toLocaleString()} RWF</td>
                <td>${transaction.fee ? transaction.fee.toLocaleString() : '0'} RWF</td>
                <td>${transaction.details || 'N/A'}</td>
                <td>${new Date(transaction.date).toLocaleString()}</td>
            </tr>
        `).join('');
    }
}

// Filter Transactions
function filterTransactions() {
    const searchTerm = searchInput.value.toLowerCase().trim();
    const selectedType = typeFilter.value.trim().toLowerCase();
    const startDate = startDateFilter.value ? new Date(startDateFilter.value) : null;
    const endDate = endDateFilter.value ? new Date(endDateFilter.value) : null;

    let filteredData = transactions.filter(transaction => {
        const transactionType = transaction.transaction_type?.trim().toLowerCase() || '';
        const transactionDate = new Date(transaction.date);

        const matchesType = (selectedType === 'all' || transactionType === selectedType);
        const matchesSearch = searchTerm ? transaction.details.toLowerCase().includes(searchTerm) : true;
        const matchesDate = (startDate && endDate) ? (transactionDate >= startDate && transactionDate <= endDate) : true;

        return matchesType && matchesSearch && matchesDate;
    });

    renderData(filteredData);
    showSuccess("Filters applied successfully!");
}

// Reset Filters
function resetFilters() {
    searchInput.value = '';
    typeFilter.value = 'all';
    startDateFilter.value = '';
    endDateFilter.value = '';
    renderData(transactions);
    showSuccess("Filters reset successfully!");
}

// Show Success Message
function showSuccess(message) {
    successMessageElement.textContent = message;
    successMessageElement.style.display = 'block';
    errorMessageElement.style.display = 'none';
    setTimeout(() => successMessageElement.style.display = 'none', 3000);
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    searchInput.addEventListener('input', filterTransactions);
    typeFilter.addEventListener('change', filterTransactions);
    startDateFilter.addEventListener('change', filterTransactions);
    endDateFilter.addEventListener('change', filterTransactions);
    applyFiltersButton.addEventListener('click', filterTransactions);
    resetFiltersButton.addEventListener('click', resetFilters);
    
    fetchTransactions();
});

