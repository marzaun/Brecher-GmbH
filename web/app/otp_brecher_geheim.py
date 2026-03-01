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
    # Secret rotiert alle 5 Minuten, aber deterministisch aus dem master secret
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

class OTPServiceServicer(otp_pb2_grpc.OTPServiceServicer):
    def GetOTPToken(self, request, context):
        # 1. Username aus dem Request extrahieren
        username = request.username
        
        # 2. Deine generate_otp Funktion aufrufen
        token_string = generate_otp(username)
        
        return otp_pb2.OTPResponse(token=int(token_string))

def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    otp_pb2_grpc.add_OTPServiceServicer_to_server(OTPServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server gestartet auf Port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve_grpc()