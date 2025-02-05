from flask import jsonify, request
from models.Bot_config import BotConfig
from models.Connection import Connection
from utils.db import db
import requests
import random 

# Import helper functions for interacting with UiPath Orchestrator
# from orchestrator import get_oauth_token, create_bot_in_orchestrator, update_bot_in_orchestrator, delete_bot_in_orchestrator

# Create a bot configuration in your database and also in UiPath Orchestrator
def configure_bot(current_company):
    data = request.get_json()
    company_id = current_company.id

    # Fetch the connection by ID to ensure it exists
    connection_id = data.get('connection_id')
    print(connection_id)
    # print()
    connection = Connection.query.filter_by(email=data['mail'], company_id=company_id).first()
    print("this is connectiion ", connection)

    if not connection:
        return jsonify({"error": "Connection not found"}), 404

    # Get OAuth token
    # try:
        # oauth_token = connection.oauth_token
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

    # Create bot in Orchestrator
    try:
        # orchestrator_bot_id = create_bot_in_orchestrator(oauth_token, {
        #     'name': data['name'],
        #     'robot_type': data['robot_type'],
        #     'environment_id': data['environment_id'],
        #     'machine_id': data['machine_id'],
        #     'package_version': data['package_version']
        # })
        orchestrator_bot_id = random.randint(100000, 999999) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Store bot configuration in the database
    bot_config = BotConfig(
        connection_id=connection_id,
        mail=data['mail'],
        Inventory_Api_url=data['Inventory_Api_url'],
        method=data['method'],
        origin_folder=data['origin_folder'],
        headers=data['headers'],
        destination_folder=data['destination_folder'],
        error_folder=data['error_folder'],
        success_email_subjects=data.get('success_email_subjects'),
        success_email_content=data.get('success_email_content'),
        error_email_subject=data.get('error_email_subject'),
        error_email_Body=data.get('error_email_Body'),
        sample_json=data['sample_json'],
        orchestrator_bot_id=orchestrator_bot_id
    )


    db.session.add(bot_config)
    db.session.commit()

    return jsonify({"message": "Bot configured successfully", "bot_id": bot_config.id, "orchestrator_bot_id": orchestrator_bot_id}), 201

# Update an existing bot configuration
def update_bot(bot_id):
    data = request.form

    # Fetch bot config by ID
    bot_config = BotConfig.query.get(bot_id)
    if not bot_config:
        return jsonify({"error": "Bot not found"}), 404

    # Get OAuth token
    # try:
    #     # oauth_token = get_oauth_token()
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

    # Update bot in Orchestrator
    # try:
    #     updated_bot = update_bot_in_orchestrator(oauth_token, bot_config.orchestrator_bot_id, data)
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

    # Update the bot config in your database if needed (e.g., change configuration)
    bot_config.mail = data.get('mail', bot_config.mail)
    bot_config.Inventory_Api_url = data.get('Inventory_Api_url', bot_config.Inventory_Api_url)
    bot_config.method = data.get('method', bot_config.method)
    bot_config.origin_folder = data.get('origin_folder', bot_config.origin_folder)
    bot_config.headers = data.get('headers', bot_config.headers)
    bot_config.destination_folder = data.get('destination_folder', bot_config.destination_folder)
    bot_config.error_folder = data.get('error_folder', bot_config.error_folder)
    bot_config.success_email_subjects = data.get('success_email_subjects', bot_config.success_email_subjects)
    bot_config.success_email_content = data.get('success_email_content', bot_config.success_email_content)
    bot_config.error_email_subject = data.get('error_email_subject', bot_config.error_email_subject)
    bot_config.error_email_Body = data.get('error_email_Body', bot_config.error_email_Body)
    bot_config.sample_json = data.get('sample_json', bot_config.sample_json)

    db.session.commit()

    return jsonify({"message": "Bot updated successfully", "updated_bot": updated_bot}), 200

# Delete a bot configuration
def delete_bot(bot_id):
    # Fetch bot config by ID
    bot_config = BotConfig.query.get(bot_id)
    if not bot_config:
        return jsonify({"error": "Bot not found"}), 404

    # Get OAuth token
    # try:
    #     oauth_token = get_oauth_token()
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

    # Delete bot from Orchestrator
    # try:
    #     result = delete_bot_in_orchestrator(oauth_token, bot_config.orchestrator_bot_id)
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

    # Delete the bot config from your database
    db.session.delete(bot_config)
    db.session.commit()

    return jsonify({"message": "Bot deleted successfully"}), 200
