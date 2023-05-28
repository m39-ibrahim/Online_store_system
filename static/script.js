
function openForm() {
  document.getElementById("myForm").style.display = "block";
  document.getElementById("add-item").onclick = closeForm;
}

function openForm2() {
  document.getElementById("myForm2").style.display = "block";
  document.getElementById("delete-item").onclick = closeForm2;
}

function openForm3() {
  document.getElementById("myForm3").style.display = "block";
  document.getElementById("add-set").onclick = closeForm3;
}

function openForm4() {
  document.getElementById("myForm4").style.display = "block";
  document.getElementById("delete=set").onclick = closeForm4;
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
  document.getElementById("add-item").onclick = openForm;
}

function closeForm2() {
  document.getElementById("myForm2").style.display = "none";
  document.getElementById("delete-item").onclick = openForm2;
}

function closeForm3() {
  document.getElementById("myForm3").style.display = "none";
  document.getElementById("add-set").onclick = openForm3;
}

function closeForm4() {
  document.getElementById("myForm4").style.display = "none";
  document.getElementById("delete=set").onclick = openForm4;
}


var inputCount = 1;
function addInput() {
  var container = document.getElementById("input-container");
  var input = document.createElement("input");
  input.type = "text";
  input.placeholder = "Enter ID number";
  input.name = "add-id" + inputCount;
  container.appendChild(input);
  inputCount++;
}


function submitForm() {
  document.getElementById("file_to_append_to").value.concat('1');
  var csvFiles = ["Online Store Items Sales", "Online Store Project Items for Sale ALTERNATIVE SHOP A", "Online Store Project Items for Sale ALTERNATIVE SHOP B", "Online Store Project Items for Sale"];
  
  if (confirm("Do you want to add to " + csvFiles[0] + "?")) {
    document.getElementById("file_to_append_to").value = document.getElementById("file_to_append_to").value.concat('1');
    alert("Item is added to " + csvFiles[0]);
  }

  console.log(document.getElementById("file_to_append_to").value)

  if (confirm("Do you want to add to " + csvFiles[1] + "?")) {
    document.getElementById("file_to_append_to").value =document.getElementById("file_to_append_to").value.concat('2');
    alert("Item is added to "  + csvFiles[1]);
  }

  console.log(document.getElementById("file_to_append_to").value)

  if (confirm("Do you want to add to " + csvFiles[2] + "?")) {
    document.getElementById("file_to_append_to").value = document.getElementById("file_to_append_to").value.concat('3');
    alert("Item is added to "  + csvFiles[2]);
  }

  console.log(document.getElementById("file_to_append_to").value)

  if (confirm("Do you want to add to " + csvFiles[3] + "?")) {
    document.getElementById("file_to_append_to").value = document.getElementById("file_to_append_to").value.concat('4');
    alert("Item is added to " + csvFiles[3]);
  }

  console.log(document.getElementById("file_to_append_to").value)
  document.getElementById("add_items").submit();
}

function handlesetSubmit(event) {
  event.preventDefault(); // prevent the form from submitting normally

  // POST request to the server to add the set
  fetch('/add_sets', {
    method: 'POST',
    body: new FormData(event.target),
  })
    .then(response => {
      if (response.ok) {
        // show a confirmation message
        alert('The set has been added to the file.');

        // clear the form inputs
        event.target.reset();
      } else {
        alert('An error occurred. Please try again.');
      }
    })
    .catch(error => {
      console.error(error);
      alert('An error occurred. Please try again.');
    });
}

function handlesetdelete(event) {
  event.preventDefault(); // prevent the form from submitting normally

  // make a POST request to the server to delete the set
  fetch('/delete_set', {
    method: 'POST',
    body: new FormData(event.target),
  })
    .then(response => {
      if (response.ok) {
        // show a confirmation message
        alert('The set has been deleted from the file.');

        // clear the form inputs
        event.target.reset();
      } else {
        alert('An error occurred. Please try again.');
      }
    })
    .catch(error => {
      console.error(error);
      alert('An error occurred. Please try again.');
    });
} 

function handleitemdelete(event) {
  event.preventDefault(); // prevent the form from submitting normally
  // make a POST request to the server to delete the set
  fetch('/delete_item', {
    method: 'POST',
    body: new FormData(event.target),
  })
    .then(response => {

        // show a confirmation message
        alert('The item has been deleted from the files.');
        alert('The set has been complemnted.');
        alert('Date sold has been added to items sales file.');
        // clear the form inputs
        event.target.reset();
      })
      .catch(error => {
        console.error(error);
        alert('An error occurred. Please try again.');
      });
  }
  /* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

