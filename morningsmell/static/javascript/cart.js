'use strict';

const update= document.queryselector('.mybtn');
const updateForm = document.queryselector('.updForm');

updateForm.style.display = 'none';

update.addEventListener('click', function(){
   updateForm.style.display = 'block'
})