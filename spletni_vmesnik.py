import bottle
import game
import board
import bot

MAX_HEIGHT = 400

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
    size = MAX_HEIGHT / g.height
    grid_width = size * g.width
    return bottle.template('game.html', game=g, size=size, grid_width=grid_width)

@bottle.post('/back/')
def back():
    g.reset()
    g.resetScore()
    bottle.redirect('/')

@bottle.post('/reset/')
def reset():
    g.reset()
    bottle.redirect('/game/')

@bottle.post('/undo/')
def undo():
    g.grid.undo()
    while(g.bots[g.grid.turns % 2]):
        g.grid.undo()
    bottle.redirect('/game/')

@bottle.get('/play/<col:int>')
def play(col):
    on_turn = g.grid.turns % 2
    if g.grid.outcome() == board.inProgress and g.grid.validColumn(col) and not g.bots[on_turn]:
        g.grid.play(col)
        state = g.grid.outcome()
        if state == board.inProgress and g.bots[1 - on_turn]:
            move = bot.takeTurn(g.grid, 1 - on_turn, 3)
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