import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args:
            command.extend(args)
        print(command, "command")
        completed_process = subprocess.run(command, timeout=30, capture_output=True, text=True, check=True)
        output_str = ''
      
        if completed_process.returncode != 0:
            outputstr +=  f"Process exited with code {completed_process.returncode}"
       
        if completed_process.stdout and completed_process.stderr:
            output_str += "Error: No output produced"

        output_str += f"STDOUT: {completed_process.stdout}"
        output_str += f"STDERR: {completed_process.stderr}"

        print(output_str, 'output_str')

        return output_str
            
    except Exception as e:
            print(f"Error: executing Python file: {e}")


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}