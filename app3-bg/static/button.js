document.getElementById('predict-btn').addEventListener('click', function() {
    const sepal_length = document.getElementById('sepal_length').value;
    const sepal_width = document.getElementById('sepal_width').value;
    const petal_length = document.getElementById('petal_length').value;
    const petal_width = document.getElementById('petal_width').value;

    // 將輸入值發送到Flask後端
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sepal_length: sepal_length,
            sepal_width: sepal_width,
            petal_length: petal_length,
            petal_width: petal_width
        })
    })
    .then(response => response.json())
    .then(data => {
        // 在網頁上顯示預測結果
        document.getElementById('result').textContent = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

