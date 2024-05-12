import streamlit as st
import pandas as pd

# Mock data storage using dictionaries
clients = {}
campaigns = {}
influencers = {}

def add_client(name, decision_maker_name, decision_maker_email):
    clients[name] = {
        "name": name,
        "decision_maker": decision_maker_name,
        "email": decision_maker_email,
        "campaigns": []
    }

def add_campaign(client_name, campaign_name, start_date, end_date):
    if client_name in clients:
        campaign = {
            "name": campaign_name,
            "start_date": start_date,
            "end_date": end_date,
            "influencers": []
        }
        clients[client_name]['campaigns'].append(campaign)
        campaigns[campaign_name] = campaign

def add_influencer_to_campaign(campaign_name, influencer_name):
    if campaign_name in campaigns and influencer_name in influencers:
        campaigns[campaign_name]['influencers'].append(influencers[influencer_name])

def add_influencer(name, email):
    influencers[name] = {"name": name, "email": email, "communications": [], "tasks": []}

def send_contract(influencer_name):
    if influencer_name in influencers:
        # Placeholder for sending email functionality
        return f"Contract sent to {influencer_name}"

# Streamlit UI components
st.title('Simple CRM for Influencer Campaigns')

with st.sidebar:
    selected_option = st.radio("Navigate", ["Clients", "Campaigns", "Influencers", "Communications"])

if selected_option == "Clients":
    st.header("Client Management")
    st.subheader("Add New Client")
    name = st.text_input("Client Name")
    dm_name = st.text_input("Decision Maker Name")
    dm_email = st.text_input("Decision Maker Email")
    if st.button("Add Client"):
        add_client(name, dm_name, dm_email)
        st.success("Client added successfully!")

    st.subheader("View Clients")
    if clients:
        for client in clients.values():
            st.text(f"Name: {client['name']}, Decision Maker: {client['decision_maker']}, Email: {client['email']}")

elif selected_option == "Campaigns":
    st.header("Campaign Management")
    st.subheader("Add New Campaign")
    client_name = st.selectbox("Select Client", list(clients.values()))
    campaign_name = st.text_input("Campaign Name")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    if st.button("Create Campaign"):
        add_campaign(client_name, campaign_name, start_date, end_date)
        st.success("Campaign created successfully!")

    st.subheader("View Campaigns")
    if campaigns:
        for campaign in campaigns.values():
            st.text(f"Name: {campaign['name']}, Start: {campaign['start_date']}, End: {campaign['end_date']}")

elif selected_option == "Influencers":
    st.header("Influencer Management")
    st.subheader("Add New Influencer")
    influencer_name = st.text_input("Influencer Name")
    influencer_email = st.text_input("Influencer Email")
    if st.button("Add Influencer"):
        add_influencer(influencer_name, influencer_email)
        st.success("Influencer added successfully!")

    st.subheader("View Influencers")
    if influencers:
        for influencer in influencers.values():
            st.text(f"Name: {influencer['name']}, Email: {influencer['email']}")

elif selected_option == "Communications":
    st.header("Manage Communications")
    selected_influencer = st.selectbox("Select Influencer for Communication", list(influencers.keys()))
    message = st.text_area("Message")
    if st.button("Send Message"):
        if selected_influencer in influencers:
            influencers[selected_influencer]['communications'].append(message)
            st.success("Message sent to influencer!")
        else:
            st.error("Influencer not found.")
    
    st.subheader("Communication History")
    if selected_influencer in influencers:
        communications = influencers[selected_influencer]['communications']
        for msg in communications:
            st.text(msg)
