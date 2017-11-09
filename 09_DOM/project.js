//restart Button
var restart=document.querySelector('#b');

//grab squares
var squares=document.querySelectorAll('td');

//clear squares
function clearBoard(){
  for (var i=0; i<squares.length;i++){
    squares[i].textContent="";
  }
}

restart.addEventListener('click',clearBoard)

//check square marker
function changeMarker(){
  if(this.textContent===""){
    this.textContent='X';
  }else if (this.textContent==="X") {
    this.textContent='O';
  }else{
    this.textContent='';
  }
}

//event listeners
for (var i=0; i<squares.length;i++){
  squares[i].addEventListener('click',changeMarker)
}
