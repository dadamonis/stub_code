import requests

def send_email_notification( ) -> None:
    """
    This function will send an email via MS Flow.
      url - Provided by MSFlow once the flow has been created
      emailaddress - the email account that is SENDING the message
      emaiSubject - the subject for the email that is being sent by the flow
      emailBody - the message that the email will contain
      errors - additional messages that will be included in the email
    
    Parameters
    ==========
    None
        
    Results
    None
    ==========
    """
    url = '<your_msflow_url>'

    headers = {'Content-type': 'application/json'}
    body ={'emailaddress': '<your_email_address>',
           'emailSubject':'<your_email_subject_line',
           'emailBody':'<your_email_message>',
           'errors':'<your_error_messages>'
          }

    r = requests.post(url, 
                      headers=headers,
                      json = body)
