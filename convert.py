from typing import Optional

def str_to_float(user_input: str) -> Optional[float]:
    try:
        return float(user_input)
    except ValueError:
        return None

