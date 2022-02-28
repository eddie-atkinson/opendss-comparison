from pathlib import Path
import pandas as pd


LOAD_PROFILE_PATH = "./load_profiles"
N_LOADS = 100

load_profile_dir = Path(LOAD_PROFILE_PATH)


def pick_file(path_obj: Path):
    file_name = path_obj.name
    if not file_name.endswith(".csv") or not file_name.startswith("Load"):
        return False
    return True


files = [file_name for file_name in load_profile_dir.iterdir() if pick_file(file_name)]
df = pd.DataFrame()
assert len(files) == N_LOADS, f"Only found {len(files)} files expected {N_LOADS}"

for file_path in files:
    load_name = file_path.name.split("_5min.csv")[0].lower() + "_mw"
    temp_df = pd.read_csv(file_path, names=[load_name])
    temp_df[load_name] /= 1000
    df[load_name] = temp_df[load_name]

# Sort columns for ease of readability
df = df.sort_index(axis=1)

df.to_csv("combined_loads.csv")
