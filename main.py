import requests

MERCADO_PAGO_ACCESS_TOKEN = "APP_USR-2067450290894309-010221-d3f0a2c6b3c51d9a60d4e482f4efa44f-1567018333"

def verify_payment(payment_id):
    """Verifica o status do pagamento no Mercado Pago."""
    url = f"https://api.mercadopago.com/v1/payments/{payment_id}"
    headers = {"Authorization": f"Bearer {MERCADO_PAGO_ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payment_data = response.json()
        status = payment_data.get("status")
        chat_id = payment_data.get("metadata", {}).get("chat_id")

        return status, chat_id

    return None, None
