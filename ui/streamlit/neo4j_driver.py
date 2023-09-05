import os
from graphdatascience import GraphDataScience

import streamlit as st

host = st.secrets["NEO4J_URI"]
user = st.secrets["NEO4J_USER"]
password = st.secrets["NEO4J_PASSWORD"]
db = st.secrets["NEO4J_DB"]

""" Setting aura_ds=False below for now in order to enable Neo4j EE instances as well. 
Once Aura Pro is available in Azure we can set back to True.
Setting to False also doesn't seem to be have any apparent negative impact on true Aura DS instances """
gds = GraphDataScience(
    host,
    auth=(user, password),
    aura_ds=False)

gds.set_database("neo4j")

def run_query(query, params=None):
    return gds.run_cypher(query, params=params)
