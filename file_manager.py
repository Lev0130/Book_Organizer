from pathlib import Path
import ai_client  
import shutil


def get_all_books(folder: Path) -> list[Path]: #Función que recibe un Path y devuelve una lista de Paths
    
    files = [f for f in folder.rglob("*") if f.is_file()]
    return files

def get_names_books(folder: Path) -> list[str]: 
    
    files_names = [f.name for f in folder.rglob("*") if f.is_file()]
    return files_names


def move_books_to_all(folder: Path, files: list[Path]) -> None:
    new_folder = folder / "all"
    Path(new_folder).mkdir(exist_ok = True)
    
    for file in files:
        new_path = Path(new_folder) / file.name
        if file.parent.name == "all":
            continue
        elif new_path.exists():
            file.unlink()
            continue
        else: 
            file.rename(new_path)
            
    for element in folder.iterdir():
        if element.name == "all":
            continue
        else:
            element.rmdir()

def organize_books(organized: dict, path: Path) -> None:
    for name, values in organized.items():
        new_folder = path / name
        if new_folder.parent.name == name:
            continue
        else:
            Path(new_folder).mkdir(exist_ok = True)
        for value in values:
            new_path = new_folder / value
            all_path = path / "all" / value
            shutil.copy(all_path, new_path)
        