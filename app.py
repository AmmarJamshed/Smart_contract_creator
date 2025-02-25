#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
from smart_contract_generator import generate_solidity_code

st.title("Smart Contract Generator")
st.subheader("Generate Solidity Smart Contracts Using Natural Language")

# Sidebar for configuration
st.sidebar.title("Settings")
contract_type = st.sidebar.selectbox(
    "Contract Type",
    ["ERC20 Token", "Voting System", "Custom"],
)
st.sidebar.write("Select contract type to specify the use case.")

# Main app for user input
scenario = st.text_area(
    "Describe Your Smart Contract Scenario",
    "e.g., Create a voting contract where each voter can vote once for a specific candidate.",
)

if st.button("Generate Smart Contract"):
    if not scenario.strip():
        st.warning("Please provide a valid scenario.")
    else:
        # Generate Solidity code
        solidity_code = generate_solidity_code(scenario, contract_type)
        st.success("Smart Contract Generated!")
        st.code(solidity_code, language="solidity")

        # Option to download the contract
        st.download_button(
            "Download Smart Contract",
            solidity_code,
            file_name="smart_contract.sol",
            mime="text/plain",
        )


# In[ ]:




