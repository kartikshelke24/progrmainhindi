
let course_container = document.getElementById('course_content')
function myFunction(x) {
  if (x.matches) { // If media query matches
    
    course_container.classList.add("collapse");
  } else {
    course_container.classList.remove("collapse");
  }
}

var x = window.matchMedia("(max-width: 990px)")
myFunction(x) // Call listener function at run time
x.addListener(myFunction) // Attach listener function on state changes
