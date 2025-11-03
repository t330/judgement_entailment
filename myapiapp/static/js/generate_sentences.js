function generateSentences(isBulkyJudgement=false) {
    // F1 Button Click Event
    const generateSentences = '/generate_sentences/';

    // Fetch generated sentences
    if (isBulkyJudgement === true) {
        console.log('Bulky Judgement initiated');
        // F2 Button Click Event: Batch up to 100 pairs of entailment judgements
        fetch(generateSentences + '?batch=true').then(response => {
            if (!response.ok) {
                throw new Error('Error in generateSentences request');
            }
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error('Unexpected response status: ' + response.status);
            }
        })
        .then(data =>{
            console.log('Django Response:', data);
            document.getElementById('sentences').innerHTML = `${JSON.stringify(data['sentences'])}`;
            // Fetch a result of entailment judgement
            judgeEntailment(data);
        })
        .catch((error) => {
            console.error('Fetch Error:', error);
        });
    } else {
        console.log('Single Judgement initiated');
        // F1 Button Click Event: Single entailment judgement
        fetch(generateSentences).then(response => {
            if (!response.ok) {
                throw new Error('Error in generateSentences request');
            }
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error('Unexpected response status: ' + response.status);
            }
        })
        .then(data =>{
            console.log('Django Response:', data);
            document.getElementById('sentences').innerHTML = `${JSON.stringify(data['sentences'])}`;
            // Fetch a result of entailment judgement
            judgeEntailment(data);
        })
        .catch((error) => {
            console.error('Fetch Error:', error);
        });
    }
}
