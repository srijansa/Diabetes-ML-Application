document.addEventListener('DOMContentLoaded', function () {
    const singleForm=document.getElementById('single-prediction-form');
    const batchForm=document.getElementById('batch-prediction-form');

    singleForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData=new FormData(singleForm);
        const data=Object.fromEntries(formData.entries());

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response=>response.json())
        .then(result=>{
            const resultDiv = document.getElementById('single-prediction-result');
            resultDiv.innerHTML = `<h2>Prediction: ${result.prediction}</h2>`;
        })
        .catch(error=>{
            console.error('Error:', error);
        });
    });

    batchForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const fileInput= document.getElementById('file-input');
        const file =fileInput.files[0];
        const reader =new FileReader();
        reader.onload=function(e){
            const csvData = e.target.result;
            const rows = csvData.split('\n');
            const headers = rows[0].split(',');
            const data = rows.slice(1).filter(row => row).map(row => {
                const values = row.split(',');
                let obj = {};
                values.forEach((value, index) => {
                    obj[headers[index]] = value;
                });
                return obj;
            });

            fetch('/batch_predict',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response=>response.json())
            .then(result =>{
                const resultDiv=document.getElementById('batch-prediction-result');
                resultDiv.innerHTML= `<h2>Predictions:</h2><pre>${JSON.stringify(result.predictions, null, 2)}</pre>`;
            })
            .catch(error =>{
                console.error('Error:', error);
            });
        };

        reader.readAsText(file);
    });
});
