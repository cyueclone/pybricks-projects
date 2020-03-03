#!/usr/bin/env python3
from os import scandir, path
from json import dump


def make_workspace(root):

    # Get list of folder names
    names = [d.name for d in scandir(root) if d.is_dir()]

    # Make the workspace dictionary
    workspace = {
        "folders": [
            {
                "path": name
            }
            for name in names
        ],
        "settings": {
            "debug.openDebug": "neverOpen"
        }
    }

    # Work space name is same as path
    workspace_name = root.replace('/', '_').replace('\\', '_')
    workspace_name += '.code-workspace'

    # Save workspace
    with open(path.join(root, workspace_name), 'w') as f:
        dump(workspace, f, indent=4)


# Make all the workspaces
roots = (
    path.join('snippets', 'ev3'),
)

for root in roots:
    make_workspace(root)
