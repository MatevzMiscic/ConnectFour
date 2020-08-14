import bottle
import random
import game
import board
import bot

MAX_HEIGHT = 460
DEPTH = 3
SECRET = 'bottle je trash'

users = {}

def get_user():
    name = bottle.request.get_cookie('name', secret=SECRET)
    print("name:", name)
    if name is None:
        new_name = str(random.randint(0, 2 ** 32))
        while new_name in users:
            new_name = str(random.randint(0, 2 ** 32))
        name = new_name
        print("someone is getting new name:", new_name)
    if name not in users:
        user = game.Game()
        users[name] = user
        print("new user")
    bottle.response.set_cookie('name', name, secret=SECRET)
    return users[name]

@bottle.get('/')
def index():
    g = get_user()
    return bottle.template('index.html', game=g)

@bottle.post('/set_grid/')
def set_grid():
    g = get_user()
    width = int(bottle.request.forms["W"])
    height = int(bottle.request.forms["H"])
    connect = int(bottle.request.forms["C"])
    print(width, height, connect)
    g.setBoard(width, height, connect)
    bottle.redirect('/')

@bottle.post('/change_red/')
def change_red():
    computer = (bottle.request.forms['red_control'] == 'Computer')
    g = get_user()
    g.setFirst(computer)
    bottle.redirect('/')

@bottle.post('/change_yellow/')
def change_yellow():
    computer = (bottle.request.forms['yellow_control'] == 'Computer')
    g = get_user()
    g.setSecond(computer)
    bottle.redirect('/')

@bottle.post('/game/')
def start_game():
    g = get_user()
    if g.bots[0]:
        move = bot.takeTurn(g.grid, 0, DEPTH)
        g.grid.play(move)
    bottle.redirect('/game/')

@bottle.get('/game/')
def plyaing():
    g = get_user()
    size = MAX_HEIGHT / g.height
    grid_width = size * g.width
    return bottle.template('game.html', game=g, size=size, grid_width=grid_width)

@bottle.post('/back/')
def back():
    g = get_user()
    g.reset()
    g.resetScore()
    bottle.redirect('/')

@bottle.post('/reset/')
def reset():
    g = get_user()
    g.reset()
    bottle.redirect('/game/')

@bottle.post('/undo/')
def undo():
    g = get_user()
    if g.grid.turns > 0:
        g.grid.undo()
        while(g.bots[g.grid.turns % 2]):
            g.grid.undo()
    bottle.redirect('/game/')

@bottle.get('/play/<col:int>')
def play(col):
    g = get_user()
    on_turn = g.grid.turns % 2
    if g.grid.outcome() == board.inProgress and g.grid.validColumn(col) and not g.bots[on_turn]:
        g.grid.play(col)
        state = g.grid.outcome()
        if state == board.inProgress and g.bots[1 - on_turn]:
            move = bot.takeTurn(g.grid, 1 - on_turn, DEPTH)
            if g.grid.validColumn(move):
                g.grid.play(move)
        state = g.grid.outcome()
        if state == board.red:
            g.firstWins()
        elif state == board.blue:
            g.secondWins()
    bottle.redirect('/game/')

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')

bottle.run(host='localhost', port=8080, debug=True, reloader=True)
#bottle.run(debug=True, reloader=True)
#bottle.run()