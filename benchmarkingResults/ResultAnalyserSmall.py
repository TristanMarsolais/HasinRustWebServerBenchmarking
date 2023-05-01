import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            parts = line.strip().split()
            data.append(float(parts[5]))  # Change this line to read the correct column
    return data

def plot_benchmark(filenames, labels):
    for filename, label in zip(filenames, labels):
        data = read_data(filename)
        plt.plot(data, label=label)

    plt.xlabel('Request Index')
    plt.ylabel('Response Time (ms)')
    plt.title('Web Server Performance Comparison for small 1kB request')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    filenames = [
        'output_small_flask.txt',
        'output_small_nginx.txt',
        'output_small_node.txt',
        'output_small_rust.txt'
    ]

    labels = [
        'Flask',
        'NGINX',
        'Node.js',
        'Rust'
    ]

    plot_benchmark(filenames, labels)
