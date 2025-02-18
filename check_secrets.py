import os

def check_secrets():
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    if aws_access_key_id and aws_secret_access_key:
        print("AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are set.")
    else:
        print("AWS_ACCESS_KEY_ID and/or AWS_SECRET_ACCESS_KEY are not set.")

if __name__ == "__main__":
    check_secrets()