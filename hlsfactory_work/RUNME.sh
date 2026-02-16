#!/usr/bin/env bash
set -euo pipefail

# 1) Load Xilinx environment (adjust version if needed)
source /tools/software/xilinx/setup_env.sh
export RDI_DATADIR=/tools/software/xilinx/2025.1.1/Vivado/data

# 2) Make sure python can import HLSFactory (assumes repo exists at ~/HLSFactory)
export PYTHONPATH="$HOME/HLSFactory:$PYTHONPATH"

# 3) Run stages (from inside hlsfactory_work)
python scripts/stage1_expand_gemm.py
python scripts/stage2_hls_synth_gemm.py
python scripts/stage3_parse_plot_gemm.py
