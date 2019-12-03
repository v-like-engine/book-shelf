import sqlite3


def new_image(id, filename, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('update books set image = "' + filename + '" where id = ' + str(id) + '')
    conn.commit()


def get_image(id, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select image from books where id = ' +
                      str(id) + '').fetchall()
    return res[0][0]


def get_table(base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select id, title, (select name from authors where id = books.author_id), ' +
                      '(select genre from genres where id = books.genre_id), year ' +
                      'from books').fetchall()
    return res


def get_title(id, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select title from books where id = "' + str(id) + '"').fetchall()
    conn.close()
    return res[0][0]


def get_author(id, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select (select name from authors where id = books.author_id) from books where id = "' +
                      str(id) + '"').fetchall()
    conn.close()
    return res[0][0]


def get_genre(id, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select (select genre from genres where id = books.genre_id) from books where id = "' +
                      str(id) + '"').fetchall()
    conn.close()
    return res[0][0]


def get_year(id, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select year from books where id = "' +
                      str(id) + '"').fetchall()
    conn.close()
    return res[0][0]


def find_title(title, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select id, title, (select name from authors where id = books.author_id), ' +
                      '(select genre from genres where id = books.genre_id), year ' +
                      'from books where title like "%' + title + '%"').fetchall()
    conn.close()
    return res


def find_author(author, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select id, title, (select name from authors where id = books.author_id), ' +
                      '(select genre from genres where id = books.genre_id), year ' +
                      'from books where author_id in ' +
                      '(select id from authors where name like "%' + author + '%")').fetchall()
    conn.close()
    return res


def find_genre(genre, base='./resources/books.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select id, title, (select name from authors where id = books.author_id), ' +
                      '(select genre from genres where id = books.genre_id), year ' +
                      'from books where genre_id in' +
                      ' (select id from genres where genre like "%' + genre + '%")').fetchall()
    conn.close()
    return res
