import os
import pathlib

import click
import flask
import numpy as np

__version__ = "0.0.1"
MYAPP = flask.Flask(__name__)
APPDIR = pathlib.Path(__file__).parent


def select_random_meme(
    meme_database_dir: pathlib.Path,
) -> pathlib.Path:
    """Select random meme from specified directory.

    :param meme_database_dir: directory containing tremendously awesome memes.
    :type meme_database_dir: pathlib.Path
    :raises RuntimeError: raises error if no memes are found in meme_database_dir.
    :return: path to one selected meme.
    :rtype: pathlib.Path
    """
    memes = os.listdir(meme_database_dir)
    num_memes = len(memes)
    if num_memes == 0:
        raise RuntimeError(
            f"Found {num_memes} in {meme_database_dir}! This is a tremendous problem!"
        )
    return (
        meme_database_dir
        / memes[np.random.randint(num_memes)]
    )


@MYAPP.route("/")
def welcome_page() -> flask.Response:
    """Establish endpoint for homepage.

    :return: Response to home endpoint.
    :rtype: flask.Response
    """
    return flask.render_template("index.html")


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
