let display = document.getElementById('display');

function appendToDisplay(value) {
    if (display.value === '0' && value !== '.') {
        display.value = value;
    } else {
        display.value += value;
    }
}

function clearDisplay() {
    display.value = '0';
}

function deleteLast() {
    if (display.value.length > 1) {
        display.value = display.value.slice(0, -1);
    } else {
        display.value = '0';
    }
}

function calculate() {
    try {
        let expression = display.value;
        // Replace custom operators with JavaScript operators
        expression = expression.replace('÷', '/').replace('×', '*').replace('−', '-');
        
        // Evaluate the expression
        let result = eval(expression);
        
        // Handle floating point precision
        result = Math.round(result * 100000000) / 100000000;
        
        display.value = result;
    } catch (error) {
        display.value = 'Error';
        setTimeout(() => {
            display.value = '0';
        }, 1500);
    }
}

// Allow keyboard input
document.addEventListener('keydown', (e) => {
    const key = e.key;
    
    if (key >= '0' && key <= '9') {
        appendToDisplay(key);
    } else if (key === '+' || key === '-' || key === '*' || key === '/') {
        e.preventDefault();
        appendToDisplay(key);
    } else if (key === '.') {
        appendToDisplay(key);
    } else if (key === 'Enter') {
        e.preventDefault();
        calculate();
    } else if (key === 'Backspace') {
        e.preventDefault();
        deleteLast();
    } else if (key === 'Escape') {
        e.preventDefault();
        clearDisplay();
    }
});
