# Python program that will run the Rust program called "py_multiplier"
# The "py_multiplier" program will take an input_value (defined in the Python
# program) and return that value multiplied by 2
#----------- WORKING ----------------------------------------------

import subprocess

# Path to your Rust program executable file:
rust_program_path = '/home/zab/Desktop/Rust_1/py_multiplier/target/release/py_multiplier'
# NB When doing your cargo build, you must do cargo build --release for this to work because you need the
# release folder with the executable file in it. cargo build is for debug mode (faster compilation but less optimisation)
# Once you have run this cargo build --release, it will generate the release folder in your program Root directory
# (the one with the cargo.toml in it) and you can then point your rust_program_path at the exe file in the release folder

# Call the Rust program using subprocess
input_value = '7' # Input value to pass to the Rust program

try:
    # Call the Rust program, passing the input directly
    result = subprocess.run(
        [rust_program_path],
        input=input_value,
        text=True,
        capture_output=True,
        check=True
    )

    # Print the result from the Rust program
    print("Result from Rust program:", result.stdout.strip())

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
except FileNotFoundError:
    print(f"Could not find the program at {rust_program_path}. Ensure it is compiled correctly.")

#---------------------------------------------------------------------------------------------------
# Output:
# /usr/bin/python3.12 /home/zab/PycharmProjects/SELENIUM_Learning/Python_Rust_3.py
# Result from Rust program: 14
#
# Process finished with exit code 0
#---------------------------------------------------------------------------------------------------

# Below is the Rust code from vsstudio main.rs  in Desktop>Rust_1>py_multiplier>src>main.rs
# (which is created in the normal way that you create Rust programs:
#--------------------------------
# use std::io;
#
# fn main() {
#     // Read integer from stdin
#     let mut input = String::new();
#     io::stdin().read_line(&mut input).unwrap();
#
#     // Parse the integer and double it
#     let number: i32 = input.trim().parse().unwrap();
#     let result = number * 2;
#
#     // Print the result
#     println!("{}", result);
# }
#---------------------------------------------------------------------------------------------------------