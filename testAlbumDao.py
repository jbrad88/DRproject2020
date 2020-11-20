from AlbumDao import albumDao

album1 = {
    'code': 123,
    'artist': 'Ed Sheeran',
    'title': 'X',
    'price': 10

}
album2 = {
    'code': 123,
    'artist': 'Ed Sheeran',
    'title': 'The second coming',
    'price': 999

}

#returnValue = albumDao.create(album)
returnValue = albumDao.getAll()
print(returnValue)

returnValue = albumDao.findById(album2['code'])
print("find By Id")
print(returnValue)

returnValue = albumDao.update(album2)
print(returnValue)

returnValue = albumDao.findById(album2['code'])
print(returnValue)

returnValue = albumDao.delete(album2['code'])
print(returnValue)

returnValue = albumDao.getAll()
print(returnValue)
