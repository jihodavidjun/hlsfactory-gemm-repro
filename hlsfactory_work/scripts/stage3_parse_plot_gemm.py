import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt

ROOT = Path("/nethome/jjun49/hlsfactory_work/designset_gemm").resolve()

files = sorted(ROOT.rglob("data_hls.json"))
print(f"Found {len(files)} data_hls.json files under {ROOT}")

rows = []
bad = 0

for fp in files:
    try:
        d = json.loads(fp.read_text())
        rows.append({
            "design": fp.parent.name,
            "lat_avg_cycles": d.get("latency_average_cycles"),
            "lat_avg_seconds": d.get("latency_average_seconds"),
            "lut": d.get("resources_lut_used"),
            "ff": d.get("resources_ff_used"),
            "dsp": d.get("resources_dsp_used"),
            "bram": d.get("resources_bram_used"),
            "clock_period_s": d.get("clock_period"),
            "path": str(fp),
        })
    except Exception as e:
        bad += 1

print(f"Parsable entries: {len(rows)} (bad: {bad})")

# Filter usable
rows = [r for r in rows if r["lat_avg_cycles"] is not None and r["lut"] is not None]
print(f"Usable entries (have latency & lut): {len(rows)}")

if not rows:
    print("No usable entries. Print one file to inspect schema:")
    if files:
        print("Sample:", files[0])
        print(files[0].read_text()[:1000])
    raise SystemExit(0)

# Save CSV
out_csv = ROOT / "gemm_stage2_summary.csv"
with out_csv.open("w") as f:
    f.write("design,lat_avg_cycles,lut,ff,dsp,bram,lat_avg_seconds,clock_period_s,path\n")
    for r in rows:
        f.write(f'{r["design"]},{r["lat_avg_cycles"]},{r["lut"]},{r["ff"]},{r["dsp"]},{r["bram"]},{r["lat_avg_seconds"]},{r["clock_period_s"]},"{r["path"]}"\n')
print("Wrote:", out_csv)

# Plot latency vs LUT
xs = [r["lat_avg_cycles"] for r in rows]
ys = [r["lut"] for r in rows]

plt.figure()
plt.scatter(xs, ys)
plt.xlabel("Latency (avg cycles)")
plt.ylabel("LUTs used")
plt.title("GEMM: Latency vs LUT (Stage 2 HLS synth)")

out_png = ROOT / "gemm_latency_vs_lut.png"
plt.savefig(out_png, dpi=200, bbox_inches="tight")
print("Saved plot:", out_png)

# Print a quick “best few” (lowest latency, lowest lut)
print("\nTop 5 lowest latency:")
for r in sorted(rows, key=lambda r: r["lat_avg_cycles"])[:5]:
    print(f'  {r["design"]}: cycles={r["lat_avg_cycles"]}, LUT={r["lut"]}')

print("\nTop 5 lowest LUT:")
for r in sorted(rows, key=lambda r: r["lut"])[:5]:
    print(f'  {r["design"]}: LUT={r["lut"]}, cycles={r["lat_avg_cycles"]}')
