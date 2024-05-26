import os
import shutil
import sys
import subprocess

def remove_invalid_distributions():
    site_packages_path = os.path.join(sys.prefix, 'Lib', 'site-packages')
    for item in os.listdir(site_packages_path):
        if item.startswith('-') or item.startswith('_'):
            item_path = os.path.join(site_packages_path, item)
            if os.path.isdir(item_path):
                print(f"Removing directory: {item_path}")
                shutil.rmtree(item_path)
            elif os.path.isfile(item_path):
                print(f"Removing file: {item_path}")
                os.remove(item_path)

def reinstall_packages():
    packages = [
        "langchain", "langchain-community", "pymysql",
        "sentence-transformers", "google-generativeai", "python-dotenv"
    ]
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall"] + packages)

if __name__ == "__main__":
    remove_invalid_distributions()
    reinstall_packages()
