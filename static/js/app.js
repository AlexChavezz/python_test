console.log
document.querySelector('.change_mode').addEventListener("click", function(){
    if(document.querySelector('body').classList.contains('light-mode')) document.querySelector('body').classList.toggle('dark-mode')
})