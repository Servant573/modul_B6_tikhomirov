from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request
import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Список альбомов {}: ".format(artist)
        result += ", ".join(album_names)
    return result

@route("/albums", method="POST")
def write():
    user_data = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }
    user_album = str(user_data["album"])
    album_artist = album.find(user_data["artist"])
    album_names = [album.album for album in album_artist]
    if user_album in album_names:
        message = "Такой альбом уже имеется"
        result = HTTPError(409, message)
        return result
    elif not str(user_data["year"]).isdigit() or not (1900 < int(user_data["year"]) < 2030):
        message = "Введено некорректное значение года выпуска альбома"
        result = HTTPError(400, message)
        return result

    else:
        album.save_album(user_data)
        return "Данные успешно сохранены"


if __name__ == "__main__":
    album.find("Tommy Vice")
    run(host="localhost", port=8080, debug=True)
