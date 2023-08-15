#Creating the entity
from dataclasses import dataclass
from pathlib import Path

#defining the return type of the dataclass
#this will return the configuration whenever I need the variables
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path