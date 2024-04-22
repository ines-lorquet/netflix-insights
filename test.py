import numpy as np
liste_croissante = [1,2,3,4,5,6,7,8,9]
# mon_array = np.array(liste_croissante)
# print (mon_array)
# mon_array[::-1]
# print (mon_array[::-1])

import pandas as pd

# Créer un DataFrame avec des valeurs manquantes
df = pd.DataFrame({'A': [1, 2, None, 4],
                   'B': [None, 5, 6, None]})

# Vérifier les valeurs nulles
print(df.isnull())
