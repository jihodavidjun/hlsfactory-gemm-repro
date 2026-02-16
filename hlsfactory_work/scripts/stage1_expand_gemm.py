from pathlib import Path

from hlsfactory.opt_dsl_frontend import OptDSLFrontend
from hlsfactory.framework import DesignDataset

WORK_DIR = Path("./work").resolve()
N_SAMPLES = 10

# Load the dataset
dataset = DesignDataset.from_dir("polybench_gemm", WORK_DIR / "designset_gemm")


# Grab one design object inside the dataset
try:
    designs = list(dataset)
except TypeError:
    designs = list(getattr(dataset, "designs"))

if len(designs) == 0:
    raise RuntimeError("No designs found in dataset. Check work/designs/gemm structure.")
if len(designs) > 1:
    print(f"Warning: found {len(designs)} designs; using the first one.")
design = designs[0]

print("Loaded design:", getattr(design, "name", design))

# OptDSL expansion (random sampling)
opt = OptDSLFrontend(
    str(WORK_DIR),
    random_sample=True,
    random_sample_num=N_SAMPLES,
)

generated_designs = opt.execute(design)

print(f"Generated {len(generated_designs)} concrete designs")
print("Work dir:", WORK_DIR)

# List generated opt.tcl files
opt_tcls = sorted(WORK_DIR.rglob("opt.tcl"))
print(f"Found {len(opt_tcls)} opt.tcl files")
for f in opt_tcls[:30]:
    print(" -", f)
