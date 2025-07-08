var items = document.getElementsByClassName("search-item")
var count = 7
if(count<items.length){
    var d = document.createElement("button")
    document.body.appendChild(d)
    alert(1)
}
for (let index = count; index<items.length; index++) {
    let element = items.item(index)
    element.style.display = 'none'
}