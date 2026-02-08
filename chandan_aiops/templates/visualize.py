import os
from pathlib import Path
import yaml
from graphviz import Digraph

def show_dvc_pipeline():
    """Visualize DVC pipeline DAG."""
    
    project_root = Path.cwd()
    dvc_file = project_root / "dvc.yaml"

    if not dvc_file.exists():
        print("ERROR: dvc.yaml not found in current directory.")
        return

    try:
        with open(dvc_file, "r") as f:
            dvc_config = yaml.safe_load(f)

        stages = dvc_config.get("stages", {})
        if not stages:
            print("No stages found in dvc.yaml.")
            return

        dot = Digraph(comment="DVC Pipeline", format="png")
        dot.attr(rankdir='LR', size='8,5')

        # Add nodes
        for stage_name in stages:
            dot.node(stage_name, stage_name, shape='box', style='filled', color='lightblue')

        # Add edges (dependencies)
        for stage_name, stage_info in stages.items():
            deps = stage_info.get("deps", [])
            for dep in deps:
                # If dep is a stage, create edge
                dep_stage = dep.split('.')[0] if dep.endswith('.py') else None
                if dep_stage and dep_stage in stages:
                    dot.edge(dep_stage, stage_name)

        # Save and render
        output_path = project_root / "dvc_pipeline"
        output_path.mkdir(exist_ok=True)
        file_path = output_path / "pipeline_dag"

        dot.render(str(file_path), view=True)
        print(f"DVC pipeline DAG generated at: {file_path}.png")

    except Exception as e:
        print(f"ERROR: Failed to generate pipeline DAG: {e}")


if __name__ == "__main__":
    show_dvc_pipeline()
