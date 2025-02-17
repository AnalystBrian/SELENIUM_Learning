# Python program that will run the Rust program "hello"
#----------- WORKING ----------------------------------------------

# It's very simple


import subprocess

# Path to your Rust program executable file:
rust_program_path = '/home/zab/Desktop/Rust_1/hello/target/release/hello'
# NB When doing your cargo build, you must do cargo build --release for this to work because you need the
# release folder with the executable file in it. cargo build is for debug mode (faster compilation but less optimisation)

# Call the Rust program using subprocess
try:
    result = subprocess.run([rust_program_path], capture_output=True, text=True, check=True)
    print("Rust program output:")
    print(result.stdout)  # If your Rust program prints anything
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
except FileNotFoundError:
    print(f"Could not find the program at {rust_program_path}. Make sure it's compiled and the path is correct.")

# Output:
#Rust program output:
#Hello, El Calafate and El Chaltan..
