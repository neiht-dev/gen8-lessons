// Common functions for worksheets

// Function to print the worksheet
function printWorksheet() {
    window.print();
}

// Function to check answers in input fields
function checkAnswer(input) {
    const userAnswer = input.value.toLowerCase().trim();
    const correctAnswer = input.dataset.answer.toLowerCase().trim();
    
    if (userAnswer === correctAnswer) {
        input.classList.remove('border-red-500');
        input.classList.add('border-green-500');
    } else {
        input.classList.remove('border-green-500');
        input.classList.add('border-red-500');
    }
}

// Function to highlight nouns in sentences
function highlightNouns(element) {
    const text = element.querySelector('p').textContent;
    const words = text.split(' ');
    
    // Common nouns to highlight
    const commonNouns = [
        'subject', 'art', 'activity', 'lunch', 'calculator', 'math', 'problem',
        'classmate', 'compass', 'swimming', 'pool', 'school', 'book', 'cat',
        'chair', 'water', 'milk', 'rice', 'apple', 'hour', 'sun', 'moon',
        'coffee', 'english', 'math', 'teacher', 'city', 'music', 'dog'
    ];
    
    const highlightedText = words.map(word => {
        const cleanWord = word.toLowerCase().replace(/[.,!?]/g, '');
        if (commonNouns.includes(cleanWord)) {
            return `<span class="bg-yellow-200">${word}</span>`;
        }
        return word;
    }).join(' ');
    
    element.querySelector('p').innerHTML = highlightedText;
} 