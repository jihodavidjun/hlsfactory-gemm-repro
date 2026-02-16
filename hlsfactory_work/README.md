# HLSFactory GEMM reproduction bundle (GT ece-rschsrv)

## What this folder contains
- `designset_gemm/` : Stage 1 expanded designs + Stage 2 HLS outputs (`data_hls.json`)
- `scripts/` : stage1/stage2/stage3 scripts used to generate results
- `results/` : plots/csv summaries (optional)

## Requirements
- Access to Xilinx Vitis/Vivado on GT server
- HLSFactory repo available at `~/HLSFactory` (or installable as a Python package)

## Run
```bash
cd ~/hlsfactory_work
./RUNME.sh
