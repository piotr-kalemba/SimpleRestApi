$(function(){

    const SOURCE = 'http://localhost:8000';

    $.ajax({
        method: 'GET',
        url: `${SOURCE}/`
    }).done(function(result){
        let tbody = $('#tbody');
        let i = 1;
        result.forEach(function(book){
            let tr = $('<tr>');
            let title = $('<td>').html(`${book.title}`);
            let author = $('<td>').html(`${book.author}`);
            let isbn = $('<td>').html(`${book.isbn}`);
            let num = $('<td>').html(i);
            tr.append(num);
            tr.append(title);
            tr.append(author);
            tr.append(isbn);
            tbody.append(tr);
            i++;
        })
    });

})