import app.io.output as out
import app.io.input as inp

def main():
    user_input = inp.input_from_console()
    out.output_to_console(user_input)
    out.write_to_file_builtin("output.txt", user_input + "\n")

    text_from_file = inp.read_from_file_builtin("file.txt")
    out.output_to_console(text_from_file)
    out.write_to_file_builtin("output.txt", text_from_file + "\n")

    df = inp.read_from_file_pandas("data.csv")
    text_from_pandas = df.to_string()
    out.output_to_console(text_from_pandas)
    out.write_to_file_builtin("output.txt", text_from_pandas + "\n")

if __name__ == "__main__":
    main()
