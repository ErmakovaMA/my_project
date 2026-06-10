install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

VD-games:
	uv run VD-games

clean:
	rm -rf dist/ build/ *.egg-info/

lint:
	uv run ruff check src/VD_games
	uv run ruff format src/VD_games
