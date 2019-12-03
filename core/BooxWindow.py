from random import choice

from PIL import Image
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem

from ui.src.BooksMenu import Ui_BookView
from core.db_work import *


class BookShelf(QMainWindow, Ui_BookView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bkid = 0
        self.stackedWidget.setCurrentIndex(0)
        self.start_b.clicked.connect(self.open_table_page)
        self.back_b.clicked.connect(self.back_to_menu)
        self.back_b_2.clicked.connect(self.open_table_page)
        self.check_b.clicked.connect(self.see_the_book)
        self.image_button.clicked.connect(self.open_image)
        self.titles_b.clicked.connect(self.search_title)
        self.authors_b.clicked.connect(self.search_author)
        self.genres_b.clicked.connect(self.search_genre)
        self.loopa.setIcon(QIcon('./resources/loop.png'))
        self.loopa.setIconSize(QSize(24, 24))
        self.label_9.setStyleSheet('background-color: rgba(255, 255, 255, 150);')
        self.change_bg()

    def change_bg(self):
        self.pm = QPixmap(choice(('./resources/book-bg.jpg', './resources/book-bg0.jpg', './resources/book-bg1.jpg',
                                  './resources/book-bg2.jpg', './resources/rbook-bg1.jpg')))
        self.label_2.setPixmap(self.pm)

    def open_table_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.set_table()

    def set_table(self):
        boox = get_table()
        self.fill_table(boox)

    def back_to_menu(self):
        self.stackedWidget.setCurrentIndex(0)
        self.change_bg()

    def to_the_book_review(self):
        self.stackedWidget.setCurrentIndex(2)

    def open_image(self):
        file_name = QFileDialog.getOpenFileName(self, 'Image', '',
                                                'Image' + '(*.jpg *.bmp)')[0]
        if file_name:
            new_image(self.bkid, file_name)
            self.look_at_book()

    def see_the_book(self):
        if self.books.currentRow() != -1:
            self.bkid = self.books.item(self.books.currentRow(), 0).text()
            self.look_at_book()

    def look_at_book(self):
        self.stackedWidget.setCurrentIndex(2)
        self.title_info.setText(get_title(self.bkid))
        self.author_info.setText(get_author(self.bkid))
        self.year_info.setText(str(get_year(self.bkid)))
        self.genre_info.setText(get_genre(self.bkid))
        if not get_image(self.bkid):
            self.image_info.setPixmap(QPixmap('./resources/rstandard.jpg'))
            self.spacer_1.setMinimumWidth((867 - 727) // 2)
        else:
            try:
                im = Image.open(get_image(self.bkid))
                size = im.size
                if size[0] > 867 or size[1] > 409:
                    x, y = size
                    if 409 < y:
                        x, y = x * 409 // y, 409
                    if 867 < x:
                        x, y = 867, y * 867 // x
                    im = im.resize((x, y))
                    fname = './resources/' + str(self.bkid) + '_' + str(x) + '_' + str(y) + '.jpg'
                    im.save(fname)
                    new_image(self.bkid, fname)
                    self.spacer_1.setMinimumWidth((867 - x) // 2)
                else:
                    self.spacer_1.setMinimumWidth((867 - size[0]) // 2)
                self.image_info.setPixmap(QPixmap(get_image(self.bkid)))
            except Exception:
                self.image_info.setPixmap(QPixmap('./resources/rstandard.jpg'))
                self.spacer_1.setMinimumWidth((867 - 727) // 2)

    def search_title(self):
        boox = find_title(self.search.text())
        self.fill_table(boox)

    def search_author(self):
        boox = find_author(self.search.text())
        self.fill_table(boox)

    def search_genre(self):
        boox = find_genre(self.search.text())
        self.fill_table(boox)

    def fill_table(self, boox):
        self.books.setRowCount(len(boox))
        for i in range(len(boox)):
            for j in range(5):
                self.books.setItem(i, j, QTableWidgetItem(str(boox[i][j])))
