const csvPath = "00_evidence/data/habitica_dailies_evidence.csv";

function parseCSV(text) {
    const lines = text.trim().split("\n");
    const headers = lines[0].split(",");

    return lines.slice(1).map((line) => {
    const values = line.split(",");
    const row = {};

    headers.forEach((header, index) => {
        row[header.trim()] = values[index] ? values[index].trim() : "";
    });

    return row;
    });
}

function renderSummary(rows) {
    const summaryBox = document.getElementById("csv-summary");

    const totalRows = rows.length;
    const dailyRows = rows.filter((row) => row.task_type === "Daily").length;
    const missedRows = rows.filter((row) => row.missed === "yes").length;
    const noContextRows = rows.filter((row) => row.context_recorded === "no").length;

    summaryBox.innerHTML = `
    <h3>CSV evidence summary</h3>
    <ul>
        <li>Total rows: <strong>${totalRows}</strong></li>
        <li>Rows classified as Daily: <strong>${dailyRows}</strong></li>
        <li>Rows marked as missed: <strong>${missedRows}</strong></li>
        <li>Rows with no contextual field recorded: <strong>${noContextRows}</strong></li>
    </ul>
    `;
}

fetch(csvPath)
    .then((response) => {
    if (!response.ok) {
        throw new Error("Could not load CSV file.");
    }
    return response.text();
    })
    .then((csvText) => {
    const rows = parseCSV(csvText);
    renderSummary(rows);
    console.log("CSV loaded successfully:", rows);
    })
    .catch((error) => {
    const summaryBox = document.getElementById("csv-summary");
    if (summaryBox) {
        summaryBox.innerHTML = `
        <p><strong>CSV could not be loaded.</strong></p>
        <p>Check the file path and make sure the local server is running.</p>
        `;
    }
    console.error(error);
    });

const toggleButtons = document.querySelectorAll(".toggle-btn");

toggleButtons.forEach((button) => {
    button.addEventListener("click", () => {
    const targetId = button.dataset.target;
    const target = document.getElementById(targetId);

    if (target.classList.contains("hidden-panel")) {
        target.classList.remove("hidden-panel");
        button.textContent = "Hide Evidence";
        button.classList.add("active");
    } else {
        target.classList.add("hidden-panel");
        button.textContent = targetId === "evidence-6" ? "Show Prototype" : "Show Evidence";
        button.classList.remove("active");
    }
    });
});

const switchButton = document.getElementById("switch-mode-btn");
const beforeCard = document.getElementById("before-card");
const afterCard = document.getElementById("after-card");

if (switchButton && beforeCard && afterCard) {
    switchButton.addEventListener("click", () => {
    if (afterCard.classList.contains("hidden-panel")) {
        beforeCard.classList.add("hidden-panel");
        afterCard.classList.remove("hidden-panel");
        switchButton.textContent = "Switch to Before";
        switchButton.classList.add("active");
    } else {
        afterCard.classList.add("hidden-panel");
        beforeCard.classList.remove("hidden-panel");
        switchButton.textContent = "Switch to After";
        switchButton.classList.remove("active");
    }
    });
}