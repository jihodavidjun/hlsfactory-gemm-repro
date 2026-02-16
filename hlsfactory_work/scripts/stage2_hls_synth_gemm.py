from pathlib import Path
from hlsfactory.framework import DesignDataset
from hlsfactory.flow_vitis import VitisHLSSynthFlow

# Path where Stage 1 outputs live
DESIGNSET = Path("/nethome/jjun49/hlsfactory_work/designset_gemm").resolve()

# Load dataset produced by Stage 1
dataset = DesignDataset.from_dir("gemm_stage1", DESIGNSET)

# Only run HLS on expanded designs
opt_designs = [d for d in dataset.designs if "_opt_" in d.name]
print(f"Found {len(opt_designs)} expanded designs")

# Use vitis-run
flow = VitisHLSSynthFlow(
    vitis_hls_bin="/tools/software/xilinx/2025.1.1/Vitis/bin/vitis-run --mode hls --tcl"
)

for d in opt_designs:
    print("Synth:", d.name)
    flow.execute(d)

print("Done.")
print("Verify with:")
print("  find /nethome/jjun49/hlsfactory_work/designset_gemm -name data_hls.json | wc -l")
