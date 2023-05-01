# Web Server Benchmark Analysis

This repository contains Python scripts to analyze the performance of various web servers using benchmark output files. The benchmarks are run for two scenarios: serving small and large static files. The web servers compared in this analysis include Flask, NGINX, Node.js, and Rust.

## Overview

The analysis process consists of the following steps:

1. Running benchmarks on each web server and generating output files with the results.
2. Using the provided Python scripts to read the output files and generate graphs that visualize the performance differences between the servers.

## Prerequisites

- Python 3.x
- `matplotlib` library: Install it using `pip install matplotlib`

## Usage

1. Clone the repository.

2. Ensure you have the following benchmark output files:
output_large_flask.txt
output_large_nginx.txt
output_large_node.txt
output_large_rust.txt
output_small_flask.txt
output_small_nginx.txt
output_small_node.txt
output_small_rust.txt


These files should contain the results of benchmarking tests run on the various web servers.

3. Run the Python script to generate the graphs:


This script reads the data from the output files and generates two graphs:
- One for the performance comparison when serving small static files
- One for the performance comparison when serving large static files

## Results

![bigFilesResult](https://user-images.githubusercontent.com/58867539/235388765-1a4ec6c6-c27a-44c9-8fd7-a49eff16686b.png)
![smallFilesResult](https://user-images.githubusercontent.com/58867539/235388774-31bf317c-ec1f-4a1a-baa9-cd7769b12e3a.png)

