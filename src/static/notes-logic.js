var active_note; 
// This is to reveal the 'create' form that is pre-filled with the desired note for editing
if ('{{ id }}') {
  var note_id = '{{ id }}'
  let active_note = true; 
  document.getElementById('create-note-content').classList.remove('display-nothing');
} else {
  let active_note = false; 
}

// Creating a new note 
let create_active = false;
$('.create-note-btn').on('click', function() {
  // This logic is for EDITING a note, which needs selection of a note and clicking the 'create' button
  if (!create_active && active_note) {
    create_active = true; 
    let obj_id = $('.clicked').attr('id'); 
    document.getElementsByClassName(obj_id)[0].click(); 
  }

  if (create_active && !active_note) {
    create_active = false; 
    document.getElementById('create-note-content').classList.add('display-nothing');

  } else if (!active_note) {
    create_active = true; 
    $('.contain-notes-content').addClass('display-nothing');
    $('.clicked-back').removeClass('clicked-back');
    console.log(document.getElementById('create-note-content'))
    document.getElementById("create-note-content").classList.remove('display-nothing');
  } 
})

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
