from flask import Flask, request
from fbmq import Page

page = Page("EABWHbYnOQhIBAHZCbnzSlmnn7x5KEoeax2ZAI6feG7ZAQs8EClvDD2xI6NZA7op3uQoVWMabbbk0YAbtAZBS1UP62VYnPTdeHlUyOZCmAKupZANPm5rG81TQX83ZCHihrXri5pXRBOLLVLmJTxpJcn2MX9lbLSY0UvnM1pI0n14VKZAReb5fHdZAsoCeIQmKQbauZCJ44zZBcJLNvQZDZD")

@app.route('/webhook', methods=['POST'])
def webhook():
  page.handle_webhook(request.get_data(as_text=True))
  return "ok"

@page.handle_message
def message_handler(event):
  """:type event: fbmq.Event"""
  sender_id = event.sender_id
  message = event.message_text
  
  page.send(sender_id, "thank you! your message is '%s'" % message)

@page.after_send
def after_send(payload, response):
  """:type payload: fbmq.Payload"""
  print("complete")