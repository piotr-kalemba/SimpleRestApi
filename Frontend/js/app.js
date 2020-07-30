$(function(){

    const SOURCE = 'http://localhost:8000';

    $.ajax({
        method: 'GET',
        url: `${SOURCE}/`
    }).done(function(result){
        let list = $('#main-list');
        result.forEach(function(book){
            let title = $('<li class="list-group-item">').html(`${book.title}`);
            title.data('id', `${book.id}`);
            title.append($('<button type="button" class="btn btn-outline-primary">Delete</button>'));
            title.append($('<div class="container">'));
            list.append(title);
        });
    });


    $('#main-list').on('click', 'li',function(event){
        let li = $(event.target);
        let id = li.data('id');
        $.ajax({
        method: 'GET',
        url: `${SOURCE}/book/${id}`
    }).done(function(book){
        let author = book.author;
        let isbn = book.isbn;
        let content = $(`<ul><li>Author: ${author}</li> <li>Isbn: ${isbn}</li></ul>`);
        let div = li.find('div');
        if(div.html() === ""){
            div.append(content);
        }
        });
    });
    $('#main-list').on('click', 'button',function(event){
        let btn = $(event.target);
        let li = btn.parent();
        let id = li.data('id');
        $.ajax({
        method: 'DELETE',
        url: `${SOURCE}/book/${id}`
    }).done(function(){
        li.remove();
        }).fail(function (xhr, status, err) {
            console.log(xhr, status, err);
            alert('Your attempt at deleting the item has been unsuccessful!');
        });
    });


})