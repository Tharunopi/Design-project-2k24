import streamlit as st
import random 
import time
from twilio.rest import Client

account_sid = 'ACf867ac43d3e65c2a2bea6b23725fb323'
auth_token = '2d5e8aa4e52727e35921068c6516b226'
client = Client(account_sid, auth_token)

if 'otp_sent' not in st.session_state:
    st.session_state.otp_sent = None

def message(number):
    st.session_state.otp_sent = random.randint(1000, 9999)
    message = client.messages.create(
        from_='+12243872051',
        body=str(st.session_state.otp_sent),
      to='+91'+number
    )
    st.success("message sent")



st.title("authentication")

reciever = (st.text_input("Enter your mobile number", '9360496526'))

if len(str(reciever)) == 10:
    st.button("message", on_click=lambda:message(reciever))

otp_recieved = (st.text_input("Enter otp"))

def checker():
    if st.session_state.otp_sent is None:
        st.warning("please sent otp first")
    elif int(otp_recieved) == st.session_state.otp_sent:
        with st.spinner("logging in."):
            time.sleep(2)
    else:
        st.warning("wrong otp")


if len(str(otp_recieved)) == 4:
    st.button("check otp", on_click=checker)




