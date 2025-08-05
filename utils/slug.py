from uuid import uuid4

def gen_slug() -> str:
    return uuid4().hex[:8]