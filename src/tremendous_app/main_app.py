import os
import pathlib
import flask
import click
import numpy

myApp = flask.Flask(__name__)
appDir = pathlib.Path(__file__).parent

def selectRandomMeme(memeDatabaseDir : pathlib.Path):
    memes = os.listdir(memeDatabaseDir)
    numMemes = len(memes)
    if (numMemes == 0):
        raise RuntimeError(f"Found {numMemes} in {memeDatabaseDir}! This is a tremendous problem!")
    return memeDatabaseDir / memes[numpy.random.randint(numMemes)]

@myApp.route("/")
def welcomePage():
    return flask.render_template("index.html")

@myApp.route("/get-meme")
def sendMeme():
    memePath = flask.request.args.get('path')
    if not os.path.isfile(memePath):
        return "Got no meme bro...", 404
    
    return flask.send_file(memePath, mimetype='image/jpeg')
    
@myApp.route("/memes", methods=["GET", "POST"])
def memes():
    memePath = firstName = lastName = favHobby = None
    if flask.request.method == "POST":
        firstName = flask.request.form.get("first_name")
        lastName = flask.request.form.get("last_name")
        favHobby = flask.request.form.get("hobby_desc")
        memePath = str(selectRandomMeme(pathlib.Path(os.environ.get("TREMENDOUS_MEMES_PATH"))))
    return flask.render_template("memes.html", meme_path=memePath, first_name=firstName, last_name=lastName, hobby_desc=favHobby)

@click.command("main")
@click.version_option("0.0.1", prog_name="tremendous-app")
@click.option("--host", type=click.STRING, default="0.0.0.0")
@click.option("--port", "-p", type=click.INT, default=os.environ.get("TREMENDOUS_PORT", 8000))
@click.option("--debug", "-dbg", is_flag=True, default=True)
def main(host : str, port : int, debug : bool):
    myApp.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    main()


