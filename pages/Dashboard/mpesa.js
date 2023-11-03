function populateTable(data) {
  const table = document.getElementById('data-table');
  const tbody = table.getElementsByTagName('tbody')[0];

  for (const key in data) {
    if (data.hasOwnProperty(key)) {
      const payment = data[key].payment;
      const date = data[key].date;
      const transactionCost = data[key].transaction_cost;

      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${key}</td>
        <td>${payment}</td>
        <td>${date}</td>
        <td>${transactionCost}</td>
      `;

      tbody.appendChild(row);
    }
  }
}

async function getDataFromAPI(url) {
    try {
   const response = await fetch(url);

   if (!response.ok) {
     throw new Error('Network response was not ok');
   }

   const data = await response.json();
   return data;
 } catch (error) {
   console.error('Error fetching data from the API:', error);
   return null;
 }
}
     const apiUrl = 'http://127.0.0.1:8000/'; // Replace with your API URL
     getDataFromAPI(apiUrl) //fetch method to get data from api 
     .then(data => { // is a promise
     if (data) {
     console.log('Data from API:', data);
     populateTable(data)
     // Process the data here
   }
 })
 .catch(error => {
   console.error('Error getting data from the API:', error);
 });
  
