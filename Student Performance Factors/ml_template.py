import os


def create_ml_project_structure(name):
    name = name
    base_dir = os.getcwd()
    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "models",
        "reports/figures",
        "name/modeling",
    ]

    files = {
        ".gitignore": "*.pyc\n__pycache__/\n.env\n.DS_Store\nmodels/\ndata/raw/\n",
        "README.md": "# Machine Learning Project\n\nProject Description.",
        "requirements.txt": "# Add your Python dependencies here\nscikit-learn\npandas\nnumpy\nmatplotlib\n",
        f"{name}/__init__.py": "",
        "notebooks/example.ipynb": "",
        f"{name}/features.py": "",
        f"{name}/modeling/__init__.py": "",
        f"{name}/modeling/predict.py": "",
        f"{name}/modeling/train.py": "",
        f"{name}/plots.py": "",
    }

    # Create folders
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)

    print(f"✅ ML project structure created in: {base_dir}")


# Usage
if __name__ == "__main__":
    name = input("enter project name:\n").replace(" ", "-").lower()
    create_ml_project_structure(name)
