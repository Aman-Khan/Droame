async function fetchRecentCustomers() {
    try {
      const response = await fetch('http://127.0.0.1:8000/recent/customers', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
      });
      const data = await response.json();
      if (response.status !== 200) {
          alert('recent customer data is not fetched');
      }
      return data;
    } catch (error) {
      console.error(error);
    }
  }
  
  // Fetch recent customer data and populate the table
  async function populateRecentCustomersTable() {
    const objectData = await fetchRecentCustomers();
    let tableData = "";
    let i=1;
    objectData.map((values)=>{
        tableData+=`<tr>
        <th scope="row">${i++}</th>
        <td>${values.customer_id}</td>
        <td>${values.customer_name}</td>
      </tr>`;
    })
    document.getElementById("quick1-table-body").innerHTML=tableData;
  }
  
  // Call the function to populate the table on page load
  populateRecentCustomersTable();