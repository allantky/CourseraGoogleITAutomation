#!/usr/bin/env python3
import os, datetime
import reports
import emails


def generate_pdf(path):
  pdf = ""
  files = os.listdir(path)
  for file in files:
    if file.endswith(".txt"):
      with open(path + file, 'r') as f:
        line = f.readlines()
        name = line[0].strip()
        weight = line[1].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf

if __name__ == "__main__":
  path = "supplier-data/descriptions/"
  current_date = datetime.datetime.now().strftime('%Y-%m-%d')

  title = "Process Updated on " + current_date
  pdf_content = generate_pdf(path)
  #print(pdf_content)
  reports.generate_report("/tmp/processed.pdf", title, pdf_content)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"

  #generate email for the online fruit store report and pdf attachment
  message = emails.generate(sender, receiver, subject, body, attachment)
  emails.send(message)
