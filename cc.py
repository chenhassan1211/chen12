import os

def create_and_copy_sentence_to_file():
    # Create the source content
    source_content = "chen is smart"

    # Define the output directory
    output_dir = "/out/"

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Define the output file name
    output_file = os.path.join(output_dir, "output_file.txt")

    # Create the output file and copy the sentence into it
    with open(output_file, 'w') as file:
        file.write(source_content)

    print(f"Sentence '{source_content}' copied to '{output_file}'.")

    # Return the output file name
    return output_file

# Usage example:
try:
    result_file = create_and_copy_sentence_to_file()
    print(f"Output file name: {result_file}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

create_and_copy_sentence_to_file
