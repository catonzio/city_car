from pathlib import Path

BASE_PATH: Path = Path(__file__).parent.parent.parent.resolve()
ASSETS_PATH: Path = BASE_PATH / "assets"
MAPS_PATH: Path = ASSETS_PATH / "maps"
