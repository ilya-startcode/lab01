import typer

# changed in main directly

app = typer.Typer(add_completion=False)

@app.command()
def greet(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Формальное приветствие."),
) -> None:
    """Печатает приветствие пользователю."""
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    app()
