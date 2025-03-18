#!/usr/bin/env python3
import subprocess

def run_helm_dry_run():
    """Runs the Helm install dry-run command and prints the output."""
    helm_cmd = ["helm", "install", "nginx", "nginx", "--dry-run"]

    try:
        # Run the Helm command and capture output
        result = subprocess.run(helm_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        
        print("✅ Helm Command Output:")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print("❌ Error running Helm command:")
        print(e.stderr)

if name == "__main__":
    run_helm_dry_run()
