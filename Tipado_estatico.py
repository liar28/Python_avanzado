from typing import Dict, List, Tuple

def suma(a: int, b: int) -> int:
    return a + b

print(suma(1,2))



positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    "Argentina": 1,
    "México": 34,
    "Colombia": 45,
}

countries: List[Dict[str, str]] = [
    {"name": "Argentina",
    "people": "450,000",
    }
]

CoordinationOfTypes = List[Dict[str, Tuple[int, int]]]
Coordinates: CoordinationOfTypes = [
    {

    }
]