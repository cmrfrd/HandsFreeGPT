"""Tool for handsfreeGPT."""

import json
import subprocess
from tempfile import NamedTemporaryFile

from langchain.tools.base import BaseTool


class PythonTool(BaseTool):
    name = "Execute Python File"
    description = (
        "Use this to execute python code. "
        "Input should be valid python code. Outputs stdout and stderr. "
        "If you want to see the output of a value, you should print it out "
        "with `print(...)`."
    )
    sanitize_input: bool = True

    def _run(self, python_code: str) -> str:
        """Use the tool."""
        if self.sanitize_input:
            python_code = python_code.strip().strip("```")

        with NamedTemporaryFile() as temp:
            temp.write(python_code.encode())   
            temp.flush()         
            
            result = subprocess.run(
                f"python {temp.name}", 
                capture_output=True, 
                shell=True,
                text=True
            )
            output: dict = {
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
            return json.dumps(output, indent=2)

    async def _arun(self, python_code: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("PythonReplTool does not support async")

class ExecuteShellTool(BaseTool):
    name = "Execute Shell Command"
    description = (
        "Use this to execute python code. "
        "Input should be valid python code. Outputs stdout and stderr. "
        "If you want to see the output of a value, you should print it out "
        "with `print(...)`."
    )
    sanitize_input: bool = True

    def _run(self, command_line: str) -> str:
        """Use the tool."""
        if self.sanitize_input:
            command_line = command_line.strip().strip("```")

        result = subprocess.run(
            command_line, 
            capture_output=True, 
            shell=True,
            text=True
        )
        output: dict = {
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
        return json.dumps(output, indent=2)

    async def _arun(self, python_code: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("PythonReplTool does not support async")


class ThinkTool(BaseTool):
    """Tool that does no action but allows HandsFreeGPT to perform a think."""

    name = "Think"
    description = (
        "A tool that does no action. "
        "Useful for when an agent needs to pause and think "
        "of next actions to perform."
        "Input should be a reason."
    )

    def _run(self, reason: str) -> None:
        """Use the tool."""
        return

    async def _arun(self) -> None:
        """Use the tool asynchronously."""
        raise NotImplementedError("Think does not support async")
