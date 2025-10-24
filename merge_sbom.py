import json
import sys

def merge_sboms(sbom_paths, output_path):
    merged = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.5",
        "components": [],
        "metadata": {}
    }

    for path in sbom_paths:
        try:
            with open(path, "r") as f:
                sbom = json.load(f)
                components = sbom.get("components", [])
                merged["components"].extend(components)
                # Optionally merge metadata here if needed
        except Exception as e:
            print(f"Warning: Could not load {path}: {e}")

    # Remove duplicates
    unique = {}
    for comp in merged["components"]:
        key = (comp.get("name"), comp.get("version"))
        unique[key] = comp
    merged["components"] = list(unique.values())

    with open(output_path, "w") as f:
        json.dump(merged, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merge_sbom.py output.json input1.json input2.json ...")
        sys.exit(1)
    out = sys.argv[1]
    inputs = sys.argv[2:]
    merge_sboms(inputs, out)
