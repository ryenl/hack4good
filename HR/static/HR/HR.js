document.addEventListener('DOMContentLoaded', function() {
    console.log("loaded");
  });


function remove(id){
    
    removebutton = document.getElementById(`removebutton_${id}`);
    userdata = document.getElementById(`employee_data_${id}`);

        fetch(`/remove/${id}`)
        .then(response => response.json())
        .then(result => {
            if (result.message == "user removed"){
                userdata.remove();
            } else{
                userdata.innerHTML = "error, could not remove"
            }
            console.log(result);
                              
      })
    };

    function myFunction() {
      // Declare variables
      console.log("Searching");
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
    
      // Loop through all table rows, and hide those who don't match the search query
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
    };

      
      let date = new Date(),
      currYear = date.getFullYear(),
      currMonth = date.getMonth();
      const months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
      function calendar(){
        fetch('/getprojects')
        .then(response => response.json())
        .then(result => {
            projects = result;
            console.log(projects);
            let date_header = document.getElementById("currentdate");
        date_header.innerText= ` ${months[currMonth]} / ${currYear}`;
        let firstDayofMonth = new Date(currYear, currMonth, 1).getDay(); // getting first day of month
        console.log(firstDayofMonth);
        //first day of month
    lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(), // getting last date of month
    lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(), // getting last day of month
    lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate(); // getting last date of previous month
    console.log(lastDayofMonth);
    console.log(date);
    test = new Date(currYear, currMonth + 1, 5);
    console.log(test);
    let tdTag = "";
    let daycount = 0;
    let datenumber =1;
    for (let i = firstDayofMonth; i > 0; i--) { // creating li of previous month last days
      tdTag += `<td class = "day">${lastDateofLastMonth - i + 1}`;
      let current_date = `${currYear}-0${currMonth}-${lastDateofLastMonth - i + 1}`;
      current_date = current_date.toString();
      projects.forEach(element => {
        console.log(element.duedate == `${currYear}-0${currMonth}-${lastDateofLastMonth - i + 1}` );
        if (element.duedate == current_date || element.duedate == `${currYear}-${currMonth}-${lastDateofLastMonth - i + 1}` ){
        console.log(element.title);
        tdTag += `<div class ="calendar_task">${element.title}<div>`;
    }});         
      daycount++;
    }
    console.log(daycount);
    for (let i = daycount; i <7; i++){
      tdTag += `<td class = "day">${datenumber}`;
      let current_date = `${currYear}-0${currMonth + 1}-0${datenumber}`;
      current_date = current_date.toString();
      console.log(current_date);
      projects.forEach(element => {
        if (element.duedate == current_date || element.duedate == `${currYear}-${currMonth + 1}-0${datenumber}` || element.duedate == `${currYear}-${currMonth + 1}-${datenumber}`){
        console.log(element.title);
        tdTag += `<div class ="calendar_task">${element.title}<div>`;
    }});
      datenumber ++;}

  console.log(daycount);
  const week1 = document.getElementById("week1")
  week1.innerHTML = tdTag;
  tdTag =""
  next_month_date = 0;
  for (let x =2; x<6; x++)
{
  for (let i = 0; i<7; i++){
    if (datenumber >= lastDateofMonth + 1){
      next_month_date++ 
      tdTag += `<td class = "day">${next_month_date}`;
      let current_date = `${currYear}-0${currMonth + 2}-0${next_month_date}`;
      current_date = current_date.toString();
      console.log(current_date);
      projects.forEach(element => {
        if (element.duedate == current_date || element.duedate == `${currYear}-${currMonth + 2}-0${next_month_date}` || element.duedate == `${currYear}-${currMonth + 2}-${next_month_date}`){
        console.log(element.title);
        tdTag += `<div class ="calendar_task">${element.title}<div>`;
    }});

    }else{
      tdTag += `<td class = "day">${datenumber}`;
      let current_date = `${currYear}-0${currMonth + 1}-0${datenumber}`;
      current_date = current_date.toString();
      console.log(current_date);
      projects.forEach(element => {
        if (element.duedate == current_date || element.duedate == `${currYear}-${currMonth + 1}-0${datenumber}` || element.duedate == `${currYear}-${currMonth + 1}-${datenumber}`|| element.duedate == `${currYear}-0${currMonth + 1}-${datenumber}`){
        console.log(element.title);
        tdTag += `<div class ="calendar_task">${element.title}<div>`;
    }});

      datenumber ++;
    }

  }
  const week = document.getElementById(`week${x}`)
  week.innerHTML = tdTag;
  tdTag = ""
}

            });
        
  }

function changemonth(int){
  // if clicked icon is previous icon then decrement current month by 1 else increment it by 1
  currMonth = currMonth + int;
  if(currMonth < 0 || currMonth > 11) { // if current month is less than 0 or greater than 11
      // creating a new date of current year & month and pass it as date value
      date = new Date(currYear, currMonth, new Date().getDate());
      currYear = date.getFullYear(); // updating current year with new date year
      currMonth = date.getMonth(); // updating current month with new date month
  } else {
      date = new Date(); // pass the current date as date value
  }
  calendar(); // calling renderCalendar function
};

function getprojects(){
  fetch('/getprojects')
        .then(response => response.json())
        .then(result => {
            projects = result;
            console.log(projects);
            return(projects);
            });
};

function markasdone(id){
  fetch(`/markasdone/${id}`)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            task = document.getElementById(`task_${id}`);
            task.remove();
            calendar(); 
      })
}

function addtotodo(){
  const inputValue = document.getElementById("todoinput").value.trim();
            if (inputValue === '') {
                alert("Please enter a task!");
                return;
            }

            const li = document.createElement("li");
            li.classList.add("list-group-item", "d-flex", "justify-content-between", "align-items-center", "bg-light");
            li.textContent = inputValue;

            const removeIcon = document.createElement("ion-icon");
            removeIcon.setAttribute("name", "close-circle-outline");
            removeIcon.style.cursor = "pointer";
            removeIcon.classList.add("text-danger");
            removeIcon.addEventListener("click", () => li.remove());

            li.appendChild(removeIcon);
            document.getElementById("myUL").appendChild(li);
            document.getElementById("todoinput").value = '';
  fetch(`/addtodo/${inputValue}`)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            var li = document.createElement("li");
            var t = document.createTextNode(inputValue);
            li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  }
      })
}

function removetodo(id){
  todoitem = document.getElementById(`todo_${id}`);
  fetch(`/removetodo/${id}`)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            todoitem.remove();

          })
  
}

function approveleave(id){
  leavestatus = document.getElementById(`leave_status_${id}`);
  leaveinfo = document.getElementById(`leave_info_${id}`);
  fetch(`/approve/${id}`)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            if (leavestatus.innerHTML == "PENDING"){            
            leavestatus.innerHTML = "APPROVED";
            x = document.getElementById(`approveleavebtn_${id}`);
            leaveinfo.className = "table-success";
            x.remove();}
          else{
            leavestatus.innerHTML = "Successfully Unapproved";
            x = document.getElementById(`unapproveleavebtn_${id}`);
            x.remove();
          }

          })
  
}








      

