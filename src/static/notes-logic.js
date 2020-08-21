var active_note; 
// This is to reveal the 'create' form that is pre-filled with the desired note for editing
if ('{{ id }}') {
  var note_id = '{{ id }}'
  let active_note = true; 
  document.getElementById('create-note-content').classList.remove('display-nothing');
} else {
  let active_note = false; 
}

// Selecting an existing note 
$(".contain-notes-header").on("click", function() {

  if (this.classList.contains('clicked')) {
    active_note = false; 

    $(this).removeClass('clicked');

    $('.contain-notes-content').addClass('display-nothing');

    $('.clicked-back').removeClass('clicked-back');
} else {
    active_note = true; 

    $('.clicked').removeClass('clicked');
    $(this).addClass('clicked');

    $('.contain-notes-content').addClass('display-nothing');
    document.getElementById($(this).attr('value')).classList.remove('display-nothing');

    $('.clicked-back').removeClass('clicked-back');
    jQuery(this).find("article").addClass('clicked-back');
  }
})

// Removing an existing note 
$('.remove-note-btn').on('click', function() {
  if(active_note) {
    let obj_id = $('.clicked').attr('id');
    document.getElementById("delete-button").click(); 
  }
})
