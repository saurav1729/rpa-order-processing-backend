# import requests
# from config import Config

# def create_bot_for_company(company_id, email, oauth_token):
#     url = f"https://yourorchestrator.com/api/robots"
#     headers = {"Authorization": f"Bearer {Config.ORCHESTRATOR_API_KEY}"}
#     data = {
#         "name": f"CompanyBot_{company_id}",
#         "email": email,
#         "oauth_token": oauth_token
#     }
#     response = requests.post(url, json=data, headers=headers)
#     return response.json()

# def configure_bot_for_email(bot_name, email, oauth_token):
#     url = f"https://yourorchestrator.com/api/robots/configure"
#     headers = {"Authorization": f"Bearer {Config.ORCHESTRATOR_API_KEY}"}
#     data = {
#         "bot_name": bot_name,
#         "email": email,
#         "oauth_token": oauth_token
#     }
#     response = requests.post(url, json=data, headers=headers)
#     return response.json()
