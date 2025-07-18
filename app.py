import asyncio
import os
from nostr_sdk import NostrWalletConnectUri, Nwc, PayInvoiceRequest, MakeInvoiceRequest
from dotenv import load_dotenv

load_dotenv()  # take environment variables

async def main():
    # Substitua pela sua URI "nostr+walletconnect://..."
    uri_str = os.getenv("NOSTR_WALLETCONNECT_URI")
    uri = NostrWalletConnectUri.parse(uri_str)
    nwc = Nwc(uri)
    
    # Consulta saldo
    balance = await nwc.get_balance()
    print("Saldo:", balance, "mSAT")

    # # Paga um invoice (substitua por um BOLT11 real)
    # pay_req = PayInvoiceRequest(invoice="lnbc1...")
    # pay_res = await nwc.pay_invoice(pay_req)
    # print("Pagamento:", pay_res)

    # # Opcional: cria um invoice para receber sats
    # create_req = MakeInvoiceRequest(
    #     amount=1500,  #msat 1000 = 1 sat = 0.00000001
    #     description=None, description_hash=None, expiry=None)
    # create_res = await nwc.make_invoice(create_req)
    # print("Invoice criado:", create_res.invoice)

asyncio.run(main())