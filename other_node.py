from langchain.schema import HumanMessage
from state import ReWOO
from termcolor import colored
import uuid

def node(state):
    print(colored("---Going to the A NODE from A-prime---", "light_blue"))
    print(colored(state , "red"))
    return {"task_ready": True}