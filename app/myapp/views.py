from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
import time
import subprocess
import platform

def htop_view(request):
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get server time in IST
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 19800))  # IST is UTC+5:30, which is 19800 seconds ahead

    # Use 'tasklist' on Windows and 'top' on Unix/Linux systems
    if platform.system() == "Windows":
        top_output = subprocess.getoutput("tasklist")
    else:
        top_output = subprocess.getoutput("top -bn 1")

    # Create an HTML response
    response_content = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Sajith Salu </p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre><strong>Top Output:</strong><br>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response_content)