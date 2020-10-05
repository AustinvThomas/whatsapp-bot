from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    if 'Hi' in msg or 'hey' in msg:
    	resp = MessagingResponse()
    	resp.message("Send 'yes' for key words")
    	return str(resp)
    if 'yes' in msg or 'Yes' in msg:
    	resp = MessagingResponse()
    	resp.message("1.conduct G-meet 2.transistor configuration with PN junction diode 3.pass in Digital Communication? 4.NODAL ANALYSIS - INSPECTION METHOD 5.CE Anna University Question Paper 6.New movie trailors")
    	return str(resp)
    if 'conduct G-meet' in msg or '1' in msg:
    	resp = MessagingResponse()
    	resp.message("www.youtube.com/watch?v=eGNKYQpdo5o")
    	return str(resp)
    if 'transistor configuration with PN junction diode' in msg or '2' in msg:
    	resp = MessagingResponse()
    	resp.message("https://www.youtube.com/watch?v=jEHcmcfD38c")
    	return str(resp)
    if 'pass in Digital Communication?' in msg or '3' in msg:
    	resp = MessagingResponse()
    	resp.message("https://www.youtube.com/watch?v=ufMAVGup6og")
    	return str(resp)
    if 'NODAL ANALYSIS - INSPECTION METHOD' in msg or '4' in msg:
    	resp = MessagingResponse()
    	resp.message("https://www.youtube.com/watch?v=jhzTlCbKkJU")
    	return str(resp)
    if 'CE Anna University Question Paper' in msg or '5' in msg:
    	resp = MessagingResponse()
    	resp.message("https://www.youtube.com/watch?v=AFAgtNTJQ5w")
    	return str(resp)
    if 'New movie trailors' in msg or '6' in msg:
    	resp = MessagingResponse()
    	resp.message("https://www.youtube.com/results?search_query=new+movie+trailers+2020+official+trailers+")
    	return str(resp)
    if 'Poorvish' in msg or '7' in msg:
    	resp = MessagingResponse()
    	resp.message("Don't ask about that Idiot")
    	return str(resp)
    if 'Austin' in msg or '8' in msg:
    	resp = MessagingResponse()
    	resp.message("The one who gave you this number")
    	return str(resp)
    
if __name__ == "__main__":
    app.run(debug=True)
