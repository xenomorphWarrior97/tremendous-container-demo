import os
import pathlib

import click
import flask
import matplotlib as mpl
from tremendous_app.utils import (
    select_random_meme,
)
# , get_mandle_bounds, generate_mandelbrot

mpl.use("Agg")

__version__ = "0.0.1"
MYAPP = flask.Flask(__name__)
APPDIR = pathlib.Path(__file__).parent


@MYAPP.route("/")
def welcome_page() -> flask.Response:
    """Establish endpoint for homepage.

    :return: Response to home endpoint.
    :rtype: flask.Response
    """
    return flask.render_template("index.html")


# @MYAPP.route("/mandelbrot.png")
# def showMandelBrot():
#    xMin,xMax,yMin,yMax = get_mandle_bounds()
#    mandelbrot_set = generate_mandelbrot(xMin, xMax, yMin, yMax, 600, 600 ,100)
#    fig, ax = plt.subplots()
#    ax.imshow(mandelbrot_set, cmap='hot', extent=[xMin,xMax, yMin, yMax])
#    ax.axis('off')
#
#    buf = io.BytesIO()
#    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
#    buf.seek(0)
#    plt.close(fig)
#    return flask.send_file(buf, mimetype='image/png')


@MYAPP.route("/get-meme")
def send_meme() -> flask.Response:
    """Establish get-meme endpoint.

    :return: Response to get-meme endpoint.
    :rtype: flask.Response
    """
    meme_path = pathlib.Path(flask.request.args.get("path"))
    if not pathlib.Path.is_file(meme_path):
        return "Sorry, got no meme bro...", 404

    return flask.send_file(
        str(meme_path), mimetype="image/jpeg"
    )


@MYAPP.route("/memes", methods=["GET", "POST"])
def memes() -> flask.Response:
    """Establish memes endpoint.

    :return: Response to memes endpoint back to server.
    :rtype: flask.Response
    """
    meme_path = first_name = last_name = fav_hobby = None
    if flask.request.method == "POST":
        first_name = flask.request.form.get("first_name")
        last_name = flask.request.form.get("last_name")
        fav_hobby = flask.request.form.get("hobby_desc")
        meme_path = str(
            select_random_meme(
                pathlib.Path(
                    os.environ.get("TREMENDOUS_MEMES_PATH")
                )
            )
        )
    return flask.render_template(
        "memes.html",
        meme_path=meme_path,
        first_name=first_name,
        last_name=last_name,
        hobby_desc=fav_hobby,
    )


@click.command("main")
@click.version_option(
    __version__, prog_name="tremendous-app"
)
@click.option(
    "--app-host",
    type=click.STRING,
    default="0.0.0.0",
    show_default=True,
)
@click.option(
    "--app-port",
    "-p",
    type=click.INT,
    default=os.environ.get("TREMENDOUS_PORT", 8000),
    show_default=True,
)
@click.option(
    "--debug-app",
    "-dbg",
    is_flag=True,
    default=True,
    show_default=True,
)
def main(
    app_host: str, app_port: int, debug_app: bool
) -> None:
    """Launch Web server.

    :param app_host: host ip for server.
    :type app_host: str
    :param app_port: port server will listen for requests on.
    :type app_port: int
    :param debug_app: launch with flask debug mode on.
    :type debug_app: bool
    """
    MYAPP.run(host=app_host, port=app_port, debug=debug_app)


if __name__ == "__main__":
    main()
