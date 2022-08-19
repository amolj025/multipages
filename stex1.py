import streamlit as st
import numpy as np
import pandas as pd
st.write(121111233455)


import requests

from requests.auth import HTTPDigestAuth



#url = 'https://httpbin.org/digest-auth/auth/user/pass'
#http://192.168.1.108/cgi-bin/snapshot.cgi

#url = 'http://192.168.1.108/cgi-bin/snapshot.cgi'   #working line

url = 'http://192.168.1.108/cgi-bin/snapManager.cgi?action=attachFileProc&channel=1&heartbeat=5&Flags[0]=Event&Events=[VideoMotion%2TrafficJunction]'   #working line

response = requests.get(url, auth=HTTPDigestAuth('admin', 'Admin@123'))
print(response)

# print request objec
#print(response)
st.write(response)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)