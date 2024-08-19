import sys
import subprocess

def install_packages(packages):
    """Install a list of packages using pip."""
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def list_installed_packages():
    """List all installed pip packages."""
    subprocess.check_call([sys.executable, "-m", "pip", "list"])

def main():
    packages = ["pandas", "numpy", "matplotlib", "seaborn", "scikit-learn"]
    install_packages(packages)
    list_installed_packages()

if __name__ == "__main__":
    main()
