from twilio.rest import Client

# Twilio credentials from https://console.twilio.com/
account_sid = ''
auth_token = ''
twilio_number = '+16184089675'  # Your Twilio phone number

# The number to call
to_number = '+923138756156'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=to_number,
    from_=twilio_number,
    url='http://demo.twilio.com/docs/voice.xml'  # URL to TwiML instructions
)

print(f"Call initiated: {call.sid}")