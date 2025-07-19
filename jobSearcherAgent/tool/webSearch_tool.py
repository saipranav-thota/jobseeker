from dotenv import load_dotenv
from crewai.tools import BaseTool

load_dotenv()

class JobScoutTool(BaseTool):
    name: str = ""
    description: str = (
        """" """
    )

    def _run(self, argument: str) -> str:
        return 0