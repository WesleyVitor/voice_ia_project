import asyncio
import os

from langchain.agents import tool
from langchain.schema.agent import AgentFinish, AgentActionMessageLog

from langchain.tools.render import format_tool_to_openai_function
from nostr_sdk import NostrWalletConnectUri, Nwc, PayInvoiceRequest, MakeInvoiceRequest

from models import GetBalanceRequest, PayInvoiceRequest, MakeInvoiceRequest

from dotenv import load_dotenv

load_dotenv()

uri_str = os.getenv("NOSTR_WALLETCONNECT_URI")
uri = NostrWalletConnectUri.parse(uri_str)
nwc = Nwc(uri)


@tool()
async def get_balance_from_nostr() -> str:
    """
    Get the balance of the Nostr wallet.
    """
    
    # balance = await nwc.get_balance()
    # return f"{balance} mSAT"
    return "72 mSAT"

@tool(args_schema=PayInvoiceRequest)
async def pay_invoice_request(bolt11_str: str) -> str:
    """
    Pay an invoice with the given bolt11 string.
    """
    # pay_req = PayInvoiceRequest(invoice=bolt11_str)
    # pay_res = await nwc.pay_invoice(pay_req)
    # return f"Payment successful: {pay_res}"
    return "OK, invoice paid successfully."

@tool(args_schema=MakeInvoiceRequest)
async def make_invoice_request(amount: int):
    """
    Create an invoice for the given amount.
    """
    # if amount < 0:
    #     return "Amount must be a positive integer."
    
    # create_req = MakeInvoiceRequest(
    #     amount=amount,  #msat 1000 = 1 sat = 0.00000001 btc
    #     description=None, 
    #     description_hash=None, 
    #     expiry=None
    # )
    # create_res = await nwc.make_invoice(create_req)
    # return create_res.invoice if create_res.invoice else "Invoice creation failed."
    return f"Invoice created for {amount} mSAT."
    


functions = [
    format_tool_to_openai_function(get_balance_from_nostr),
    format_tool_to_openai_function(pay_invoice_request),
    format_tool_to_openai_function(make_invoice_request)
]


def route(result: AgentActionMessageLog | AgentFinish) -> str:
    """
    Route the result to the appropriate tool or return the final output.
    """
    if isinstance(result, AgentFinish):
        return result.return_values['output']
    else:
        tools = {
            "get_balance_from_nostr": get_balance_from_nostr,
            "pay_invoice_request": pay_invoice_request,
            "make_invoice_request": make_invoice_request
        }
        return asyncio.run(
            tools[result.tool].ainvoke(result.tool_input)
        )
