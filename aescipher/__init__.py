version = "2.1.1"
keywords = ["aes cipher"]
entry = "test:main"


if not version.endswith(".0"):
    import re
    print(f"version {version} is deployed for automatic commitments only", flush=True)
    print("install version "+re.sub(r"([0-9]+\.[0-9]+\.)[0-9]+", r"\g<1>0", version)+" instead")
    import os
    os._exit(1)


from .aescipher import *

