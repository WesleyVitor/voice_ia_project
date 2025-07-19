from langchain.agents import tool
from models import GetBalanceRequest, PayInvoiceRequest, MakeInvoiceRequest

from langchain.tools.render import format_tool_to_openai_function

from langchain.schema.agent import AgentFinish

@tool(args_schema=GetBalanceRequest)
def get_balance_from_nostr() -> str:
    """
    Get the balance of the Nostr wallet.
    """
    return "72 mSAT"  

@tool(args_schema=PayInvoiceRequest)
def pay_invoice_request(bolt11_str: str) -> str:
    """
    Pay an invoice with the given bolt11 string.
    """
    return f"Paid invoice with {bolt11_str}."

@tool(args_schema=MakeInvoiceRequest)
def make_invoice_request(amount: int):
    """
    Create an invoice for the given amount.
    """
    return f"Created invoice for {amount} mSAT."


functions = [
    format_tool_to_openai_function(get_balance_from_nostr),
    format_tool_to_openai_function(pay_invoice_request),
    format_tool_to_openai_function(make_invoice_request)
]


def route(result):
    if isinstance(result, AgentFinish):
        return result.return_values['output']
    else:
        tools = {
            "get_balance_from_nostr": get_balance_from_nostr,
            "pay_invoice_request": pay_invoice_request,
            "make_invoice_request": make_invoice_request
        }
        return tools[result.tool].run(result.tool_input)