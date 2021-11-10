
from typing import Dict, List

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45,

}

countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '45000',
    },
    {
        'name': 'México',
        'people': '9000000',
    },
    {
        'name': 'Colombia',
        'people': '9999999999999'
        
    },
]

from typing import Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)



from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

#Una variable que es de tipo CoordinatesType 🤯
coordinates: CoordinatesType = [
  {
    'coord1': (1,2),
    'coord2': (3,5),
  },
  {
    'coord1': (0,1),
    'coord2': (2,5),
  },
]