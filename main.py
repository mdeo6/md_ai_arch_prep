
### main.py

```python
import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

def main():
    list_s3_buckets()

if __name__ == "__main__":
    main()