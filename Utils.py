import json
import os
import pkgutil
import yaml
from typing import Any, Dict, List, Optional, Union

def load_data_file(*args) -> dict:
    fname = os.path.join("data", *args)

    try:
        filedata = json.loads(pkgutil.get_data("Manual_Sprashfecta_MuffinJets", fname).decode())
    except:
        filedata = []

    return filedata

def convert_to_list(data: Dict[str, Any], key: str) -> List[Any]:
    """Convert a dictionary with a 'data' key to a list."""
    if not isinstance(data, dict) or key not in data:
        raise ValueError(f"Expected dictionary with '{key}' key")
    return data[key]

class ManualFile:
    def __init__(self, filename: str, expected_type: type):
        self.filename = filename
        self.expected_type = expected_type
        self.data = None

    def load(self) -> Any:
        if self.data is None:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
            if not isinstance(self.data, self.expected_type):
                raise TypeError(f"Expected {self.expected_type.__name__}, got {type(self.data).__name__}")
        return self.data

def load_game_specific_data(game_name: str) -> Dict[str, Any]:
    """Load game-specific data from the appropriate JSON files."""
    game_data = {}
    
    # Load game-specific items
    items_file = f'items_{game_name}.json'
    if os.path.exists(items_file):
        game_data['items'] = convert_to_list(ManualFile(items_file, list).load(), 'data')
    
    # Load game-specific locations
    locations_file = f'locations_{game_name}.json'
    if os.path.exists(locations_file):
        game_data['locations'] = convert_to_list(ManualFile(locations_file, list).load(), 'data')
    
    # Load game-specific regions
    regions_file = f'regions_{game_name}.json'
    if os.path.exists(regions_file):
        game_data['regions'] = ManualFile(regions_file, dict).load()
        game_data['regions'].pop('$schema', '')
    
    return game_data

def load_player_preferences() -> Dict[str, Any]:
    """Load player preferences from the YAML file."""
    with open('player_preferences.yaml', 'r') as f:
        return yaml.safe_load(f) 