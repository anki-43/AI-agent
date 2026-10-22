from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
import json
from collections.abc import Callable
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file

available_functions: list = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]


function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name

    raw_arguments = tool_call.function.arguments or "{}"
    function_args = json.loads(raw_arguments)

    # Add working_directory to the function arguments
    function_args["working_directory"] = "./calculator"

    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }
    print(function_name, function_args, "function_args")
    result = function_map[function_name](**function_args)

    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }