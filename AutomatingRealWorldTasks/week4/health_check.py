#!/usr/bin/env python3
import psutil, shutil
import socket
import emails
import os, sys

#Warning if CPU usage is over 80%
def cpu_check():
  cpu_usage = psutil.cpu_percent(1)
  return not cpu_usage > 80

#Report an error if available disk space is lower than 20%
def disk_space_check():
  disk_usage = shutil.disk_usage("/")
  disk_total = disk_usage.total
  disk_free = disk_usage.free
  threshold = disk_free / disk_total * 100
  return not threshold < 20

#Report an error if available memory is less than 500MB
def available_memory_check():
  mem = psutil.virtual_memory().available
  mem_MB = mem / 1024 ** 2 #convert to MB
  return mem_MB > 500

#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def hostname_check():
  local_host_ip = socket.gethostbyname('localhost')
  return local_host_ip == "127.0.0.1"

def email_warning(error):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate(sender, receiver, subject, body)
  emails.send(message)

if __name__ == "__main__":
  if not cpu_check():
    subject = "Error - CPU usage is over 80%"
    print(subject)
    email_warning(subject)

  if not disk_space_check():
    subject = "Error - Available disk space is less than 20%"
    email_warning(subject)

  if not available_memory_check():
    subject = "Error - Available memory is less than 500MB"
    print(subject)
    email_warning(subject)

  if not hostname_check():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    print(subject)
    email_warning(subject)
