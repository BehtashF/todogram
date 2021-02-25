document.getElementById('div_id_description').style.display = 'none'
document.getElementById('submit_task_btn').style.display = 'none'


window.addEventListener('click', function(e){   
    if (document.getElementById('create_task_box').contains(e.target)){
        document.getElementById('div_id_description').style.display = 'block'
        document.getElementById('submit_task_btn').style.display = 'block'
    } else{
        document.getElementById('div_id_description').style.display = 'none'
        document.getElementById('submit_task_btn').style.display = 'none'
    }
});