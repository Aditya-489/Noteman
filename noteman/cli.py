import click
from noteman.notes import create_note,list_all,get_note
from noteman.remove import remove_note

@click.group()
def cli():
    pass


@click.command()
@click.argument("title")
@click.argument("content")
def make(title:str,content:str) -> None:
    create_note(title,content)

@click.command()
@click.option("--i",type=int,help="ID of the note")
@click.option("--t",type=str,help="title of the note")
@click.option("--a","show_all",is_flag=True,help="List all notes")
def get(i:int=None,t:str=None,show_all:bool=False) -> None :
    if show_all:
        list_all()
    elif i is not None or t is not None:
        get_note(note_id=i,note_title=t)
    else:
        print("Please provide either --i or --t or --a")

@click.command()
@click.option("--i",type=int,help="ID of the note")
@click.option("--t",type=str,help="title of the note")
def kick(i:int=None,t:str=None) -> None:
    if i is not None or t is not None:
        remove_note(note_id=i,note_title=t)
    else:
        print("Please provide either --i or --t")

cli.add_command(kick)
cli.add_command(make)
cli.add_command(get)

