import nbformat

# Load the notebook
notebook_path = "./House Price Prediction/House_Price_Prediction.ipynb"
with open(notebook_path, "r") as f:
    nb = nbformat.read(f, as_version=4)

# Remove 'metadata.widgets'
if "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

# Save the cleaned notebook
with open(notebook_path, "w") as f:
    nbformat.write(nb, f)

print("Fixed notebook saved.")