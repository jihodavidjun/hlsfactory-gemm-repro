# HLSFactory GEMM Reproduction

Goal:
- Verify that HLSFactory’s design expansion and synthesis flow works
- Extract latency–resource tradeoffs for GEMM
- Understand how HLS transformations impact performance vs hardware cost

---

## Repository structure

```
hlsfactory-gemm-repro/
├── README.md      
├── RUNME.sh
├── hlsfactory_work/
│   ├── designset_gemm/ # Expanded designs & HLS outputs
│   │   ├── polybench_gemm/
│   │   ├── polybench_gemm_opt_*/
│   │   └── ...
│   ├── scripts/
│   │   ├── stage1_expand_gemm.py # Stage 1: expand GEMM design space
│   │   ├── stage2_hls_synth_gemm.py # Stage 2: run Vitis HLS on expanded designs
│   │   └── stage3_parse_plot_gemm.py # Stage 3: parse + plot results
│   └── results/
│       ├── gemm_latency_vs_lut.png 
│       └── gemm_stage2_summary.csv
└── .gitignore
```

---

## How to run

From the repo root:

```bash
cd hlsfactory_work
./RUNME.sh
```

## Results
The main result is a latency–resource tradeoff plot:

- X-axis: Average latency (cycles)

- Y-axis: LUT usage

Each point corresponds to one expanded GEMM design.
The plot illustrates how aggressive optimizations reduce latency at the cost of significantly increased LUT usage.

### What I learned
Through this reproduction, I gained experience with:

- HLSFactory’s design expansion model

- Running and debugging Vitis HLS in batch mode

- Parsing HLS outputs into quantitative summaries

- Interpreting latency vs area tradeoffs in FPGA design
