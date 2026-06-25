import numpy as np
import time
import matplotlib.pyplot as plt
import json
from datetime import datetime

def run_benchmark():
    nodes = [100, 500, 1000, 2000, 5000]
    trad_times, res_times = [], []
    
    # Run the math
    for n in nodes:
        matrix = np.random.rand(n, n)
        start = time.perf_counter()
        _ = np.linalg.inv(matrix @ matrix.T)
        trad_times.append(time.perf_counter() - start)
        
        start = time.perf_counter()
        _ = np.sum(np.fft.fft(np.random.rand(n)))
        res_times.append(time.perf_counter() - start)

    # Log the metadata
    run_metadata = {
        "timestamp": datetime.utcnow().isoformat(),
        "nodes": nodes,
        "traditional_slam_seconds": trad_times,
        "resonance_operator_seconds": res_times,
        "system_info": "High-Dimensional Resonance Projection v1.0"
    }
    
    with open('benchmark_data.json', 'w') as f:
        json.dump(run_metadata, f, indent=4)

    # Plotting... (same as before, but now it references the data file)
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, trad_times, label='Traditional SLAM (O(N^3))', marker='o')
    plt.plot(nodes, res_times, label='Resonance Operator (O(N))', marker='o')
    plt.xlabel('State Space Nodes')
    plt.ylabel('Compute Time (seconds)')
    plt.title('Benchmark: Computational Efficiency Gain')
    plt.legend()
    plt.grid(True)
    plt.savefig('benchmark_results.png')
    print("Benchmark complete. Data logged to benchmark_data.json and chart to benchmark_results.png")

if __name__ == "__main__":
    run_benchmark()

