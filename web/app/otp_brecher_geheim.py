import hashlib
import time
import grpc
from concurrent import futures
import otp_pb2
import otp_pb2_grpc
import os

from dotenv import load_dotenv
load_dotenv()

OTP_SECRET = os.getenv("OTP_SECRET")
if OTP_SECRET is None:
    raise RuntimeError("OTP_SECRET nicht gesetzt")

def get_time_based_secret():
    time_window = int(time.time()) // 300
    derived = hashlib.md5(f"{OTP_SECRET}:{time_window}".encode()).hexdigest()   
    return derived

def generate_otp(username):
    time_step = int(time.time()) // 300
    secret = get_time_based_secret()
    raw = f"{username}:{secret}:{time_step}"
    digest = hashlib.sha256(raw.encode()).hexdigest()
    otp = ''.join(c for c in digest if c.isdigit())[:6]
    return otp.ljust(6, '0')
