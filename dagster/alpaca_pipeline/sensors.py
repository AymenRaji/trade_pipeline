from dagster import RunFailureSensorContext, run_failure_sensor
import smtplib
from email.message import EmailMessage
import ssl
import os

def message(context: RunFailureSensorContext) -> str:
    error_strings_by_step_key = {
    # includes the stack trace
    event.step_key: event.event_specific_data.error.to_string()
    for event in context.get_step_failure_events()
}
    return (
        f"Job {context.dagster_run.job_name} failed!\n"
        f"Error: {context.failure_event.message}\n {error_strings_by_step_key}\n\n\n {context.get_step_failure_events()}"
    )

@run_failure_sensor(monitor_all_code_locations=True
                    )
def email_on_filure_sensor(context: RunFailureSensorContext):
    email_subject = f"Failure in job: {context.dagster_run.job_name}"
    email_body = message(context)
    context.log.info(message(context))
    email_sender = os.environ["EMAIL_SENDER"]
    email_password = os.environ["EMAIL_PASSWORD"]
    receivers = os.environ["EMAIL_RECEIVERS"]
    email_receiver = [receiver.strip() for receiver in receivers.split(",") ]

    subject = email_subject
    error_strings_by_step_key = {

    event.step_key: event.event_specific_data.error.to_string()
    for event in context.get_step_failure_events()
}
    context.log.info(context.get_step_failure_events())

    body = email_body 


    em = EmailMessage()

    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)


    context_ssl = ssl.create_default_context()


    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context_ssl) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

