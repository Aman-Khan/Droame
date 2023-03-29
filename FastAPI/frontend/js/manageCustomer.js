// Updata Customer Details

document.getElementById("manage-customer-edit").addEventListener("submit", function(event) {
  event.preventDefault(); // prevent form from submitting normally

  // get form data
  const form = event.target;
  const searchOption = form.elements["search_option"].value;
  const customerId = form.elements["customer_id"].value;
  const searchValue = form.elements["search_value"].value;

  // make PUT request to update customer
  fetch(`http://127.0.0.1:8000/update/${customerId}`, {
    method: "PATCH",
    body: JSON.stringify({ [searchOption]: searchValue }),
    headers: {
      "Content-Type": "application/json",
      'Authorization': `Bearer ${token}`
    }
  })
  .then(response => {
    if (!response.ok) {
      alert(response.status)
      // throw new Error("Network response was not ok");
    }else{
      alert(`${response.status} - Updated`)

    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    // handle success response
  })
  .catch(error => {
    console.error("There was a problem with the fetch operation:", error);
    // alert(error.message);
    // handle error
  });
});


//Delete Customer from data base
document.getElementById("manage-customer-delete").addEventListener("submit", function(event) {
  event.preventDefault(); // prevent form from submitting normally

  // get form data
  const form = event.target;
  const customerId = form.elements["customer_id"].value;

  // make DELETE request to delete customer
  fetch(`http://127.0.0.1:8000/delete/${customerId}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      'Authorization': `Bearer ${token}`
    }
  })
  .then(response => {
    if (!response.ok) {
      alert(`${response.status} - customer not found`)
      // throw new Error("Network response was not ok");
    }
    else{
      alert('Customer Deleted')
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    // handle success response
  })
  .catch(error => {
    console.error("There was a problem with the fetch operation:", error);
    // handle error
  });
});
