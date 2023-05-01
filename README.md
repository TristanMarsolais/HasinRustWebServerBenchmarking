# Web Server Benchmarking

This repository contains the code and tools to benchmark the performance of Hasin's Rust server against other popular web servers such as NGINX, Flask, and Node.js using ApacheBench (`ab`). The results are visualized using a Python script that generates a graph to show the performance differences between the servers.

## Overview

The benchmarking process consists of the following steps:

1. Setting up each web server with a minimal configuration to serve static content.
2. Generating load on the servers using ApacheBench (`ab`).
3. Collecting performance metrics such as requests per second, latency, and resource usage.
4. Analyzing and visualizing the results using a Python script to create a graph.

## Prerequisites

- Docker (to run the web servers in containers)
- Python 3.x (to run the visualization script)
- ApacheBench (`ab`) installed on your system

## Usage

1. Clone the repository:

2. Run the web servers:

3. Run the benchmark: