# Python program that will run the Rust program called "py_multiplier"
# The "py_multiplier" program will take an input_value (defined in the Python
# program) and return that value multiplied by 2

#v3 is working. v4 will try and apply the same function created in Rust (py_multipler) to a pandas df
#v4 is working!

import subprocess
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# Create a random df as a base:
df = pd.DataFrame(
    {
        "Name": ["Brian", "Brian", "Brian", "Brian", "Megan", "Megan", "Megan", "John"], # sets Col One
        "Number": [100, 50, 20, 30, 20, 40, 10, 9000], # sets Col 2
        "Fav Food": ["Hamburgers", "Pizza", "Milkshake", "Ice cream", "Chocolate", "Veggies", "Chicken", "KFC"], # sets Col 3
    },
    index=[0, 1, 2, 3, 4, 5, 6, 7], #sets the index
)
print(df)

# Get the number of rows in your dataframe:
no_of_rows = df.shape[0]
print(no_of_rows) # In this case, 8 rows (not including the column names)

# Path to your Rust program executable file:
rust_program_path = '/home/zab/Desktop/Rust_1/py_multiplier/target/release/py_multiplier'
# NB When doing your cargo build, you must do cargo build --release for this to work because you need the
# release folder with the executable file in it. cargo build is for debug mode (faster compilation but less optimisation)
# Once you have run this cargo build --release, it will generate the release folder in your program Root directory
# (the one with the cargo.toml in it) and you can then point your rust_program_path at the exe file in the release folder

# Loop through each of the rows
for x in range(no_of_rows):
    i_val = df.loc[x,'Number']
    # Call the Rust program using subprocess
    input_value = str(i_val) #Rust program is expecting a string value

    try:
        # Call the Rust program, passing the input directly
        result = subprocess.run(
            [rust_program_path],
            input=input_value,
            text=True,
            capture_output=True,
            check=True
        )

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print(f"Could not find the program at {rust_program_path}. Ensure it is compiled correctly.")

    df.loc[x, 'ExtraCol'] = result.stdout.strip() # Assign oputput of Rust program to 'ExtraCol'

print("---------------------------------------------------------------------------------------------------")
print(df)

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