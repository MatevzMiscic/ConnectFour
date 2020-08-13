import bottle
import game

MAX_HEIGHT = 500

g = game.Game()

@bottle.get('/')
def index():
    return bottle.template('index.html', game=g)

@bottle.post('/set_grid/')
def set_grid():
    width = int(bottle.request.forms["W"])
    height = int(bottle.request.forms["H"])
    connect = int(bottle.request.forms["C"])
    print(width, height, connect)
    legal = g.setBoard(width, height, connect)
    if legal:
        bottle.redirect('/')
    else:
        bottle.redirect('/')

@bottle.post('/change_red/')
def change_red():
    computer = (bottle.request.forms['red_control'] == 'Computer')
    g.setFirst(computer)
    bottle.redirect('/')

@bottle.post('/change_yellow/')
def change_yellow():
    computer = (bottle.request.forms['yellow_control'] == 'Computer')
    g.setSecond(computer)
    bottle.redirect('/')

@bottle.post('/game/')
def start_game():
    bottle.redirect('/game/')

@bottle.get('/game/')
def game():
    return bottle.template('game.html', game=g)

@bottle.get('/play/<col:int>')
def play(col):
    print(col)
    bottle.redirect('/game/')

@bottle.get('/kvadriraj/<n:int>')
def kvadriraj(n):
    return '{}^2 = {}'.format(n, n ** 2)

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')

bottle.run(host='localhost', port=8080, debug=True, reloader=True)
#bottle.run(debug=True, reloader=True)
#bottle.run()