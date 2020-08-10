window.addEventListener('load', function() {
    if (!window.location.hash) {
        window.location = window.location + '#loaded';
        window.location.reload();
    }

    let existing_reminders = document.getElementsByClassName('existing-reminders');
    let delay = 500; 

    setTimeout(function() {
        for (let i = 0; i < existing_reminders.length; i++) {
            existing_reminders[i].classList.remove('display-nothing');
            existing_reminders[i].classList.add('appear');
        }
    }, delay)

    let delete_buttons = document.getElementsByClassName('orig-1');
    for (let i = 0; i < delete_buttons.length; i++) {
        delete_buttons[i].addEventListener('click', deleteReminders);
    }
    let done_buttons = document.getElementsByClassName('orig-2');
    for (let i = 0; i < done_buttons.length; i++) {
        done_buttons[i].addEventListener('click', finishReminder);
    }

})

let remindersAdd = document.getElementById('reminders-add');
let remindersInput = document.getElementById('reminders-input');

function inputLength() {
    return remindersInput.value.length;
}

function createReminder() {
    let div = document.createElement('div');
    $(div).addClass('row');
    $(div).addClass('center-horizontal');
    let divchild = document.createElement('div');
    $(divchild).addClass('text-light');
    $(divchild).attr('id', 'reminders-input-cont');

    let divgrandchild = document.createElement('div');
    $(divgrandchild).attr('id', 'additional-reminder');

    divgrandchild.appendChild(document.createTextNode(remindersInput.value));
    let clone_1 = $('.clone-1').clone();
    clone_1.removeClass('display-nothing');
    // clone_1.addEventListener('click', deleteReminders);
    clone_1.appendTo(divgrandchild);

    divchild.appendChild(divgrandchild);
    div.appendChild(divchild);
    $(div).addClass('appear');
    $(div).insertAfter('.reminders-main');
}

function updateReminders() {
    $.ajax({
        url: '/reminder-add/',
        data: {'reminder_content':remindersInput.value},
        type: 'POST',
    })
    window.location = window.location.href.split('#')[0]
};

function deleteReminders(e) {
    let id = e.target.getAttribute('id');
    $.ajax({
        url: '/reminder-delete/',
        data: {'id':id},
        type: 'POST',
    })
    window.location = window.location.href.split('#')[0]
}

function finishReminder(e) {
    let id = e.target.getAttribute('id');
    let reminder_unfinished = document.getElementsByClassName('reminder-unfinished');
    for (let i = 0; i < reminder_unfinished.length; i++) {
        if (reminder_unfinished[i].getAttribute('id') == id) {
            reminder_unfinished[i].classList.add('display-nothing');
        }
    }
    let reminder_finished = document.getElementsByClassName('reminder-finished');
    for (let i = 0; i < reminder_finished.length; i++) {
        if (reminder_finished[i].getAttribute('id') == id) {
            reminder_finished[i].classList.remove('display-nothing');
        }
    }
    let existing_reminders = document.getElementsByClassName('additional-reminders');
    for (let i = 0; i < existing_reminders.length; i++) {
        if (existing_reminders[i].getAttribute('value') == id) {
            existing_reminders[i].style.backgroundColor = 'rgba(' + 0 + ',' + 0 + ',' + 0 + ',' + 0.5 + ')';
        }
    }

    $.ajax({
        url: '/reminder-delete/',
        data: {'id':id},
        type: 'POST',
    })
}

function updateReminderTrigger(e) {
    if (inputLength() > 0 && e.which === 13) {
        // createReminder();
        updateReminders();
    }
};

remindersInput.addEventListener('keypress', updateReminderTrigger);