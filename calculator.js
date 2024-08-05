function calculateMonthlyPayment(principal, annualRate, years) {
    let monthlyRate = annualRate / 12 / 100;
    let totalPayments = years * 12;
    if (monthlyRate === 0) {
        return principal / totalPayments;
    } else {
        return (principal * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -totalPayments));
    }
}

function calculateLoan() {
    let principal = parseFloat(document.getElementById('principal').value);
    let annualRate = parseFloat(document.getElementById('annualRate').value);
    let years = parseInt(document.getElementById('years').value);

    if (isNaN(principal) || isNaN(annualRate) || isNaN(years)) {
        document.getElementById('result').innerText = 'Please enter valid numbers.';
        return;
    }

    let monthlyPayment = calculateMonthlyPayment(principal, annualRate, years);
    document.getElementById('result').innerText = `Your monthly payment is: $${monthlyPayment.toFixed(2)}`;
}
