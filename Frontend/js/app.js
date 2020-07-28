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



})