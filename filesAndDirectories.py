from pathlib import Path

# Absolut path
# c:\Program Files\Microsoft

# Relative path

path = Path("ecommerce")
print(path.exists())

# ========================

path = Path()
# print(path.glob('*.*')) # search for all files
print(path.glob('*.py')) # search for all python files
# print(path.glob('*.xls')) # search for all xls files

path = Path()
for file in path.glob('*.py'): # search for all python files
    print(file)
