import bottle
import game

width = 7
height = 6
connect = 4

red = False
yellow = True

g = game.Game()

@bottle.get('/')
def index():
    return bottle.template('index.html', game=g)

@bottle.post('/game/')
def start_game():
    width = int(bottle.request.forms["W"])
    height = int(bottle.request.forms["H"])
    connect = int(bottle.request.forms["C"])
    print(width, height, connect)
    legal = g.setBoard(width, height, connect)
    if legal:
        bottle.redirect('/game/')
    else:
        bottle.redirect('/')

@bottle.get('/game/')
def game():
    return bottle.template('game.html', width=width, height=height)

@bottle.get('/change_red/')
def change_red():
    global red
    red = (bottle.request.query['red_control'] == 'Computer')
    bottle.redirect('/')

@bottle.get('/change_yellow/')
def change_yellow():
    global yellow
    yellow = (bottle.request.query['yellow_control'] == 'Computer')
    bottle.redirect('/')


@bottle.get('/sestej/')
def sestej():
    a = int(bottle.request.query['stA'])
    b = int(bottle.request.query['stB'])
    return "{} + {} = {}".format(a, b, a + b)

@bottle.get('/pozdravi/<ime>')
def pozdravi(ime):
    return 'Živjo, <b>{}</b>!'.format(ime)

@bottle.get('/kvad/<n:int>')
def kvadriraj(n):
    return '{}^2 = {}'.format(n, n ** 2)

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')

bottle.run(host='localhost', port=8080, debug=True, reloader=True)
#bottle.run(debug=True, reloader=True)
#bottle.run()