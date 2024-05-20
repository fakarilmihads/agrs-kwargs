import pandas as pd
from pathlib import Path
class Search(object):
    def __init__(self, query, path: str):
        self.query = query
        self.data: str = ""
        self.path: str = path
        

    def search_data(self, *args, **kwargs):
        query = kwargs.get('query', None)
        df = pd.read_csv(self.path)
        if query:
            # Buat filter untuk setiap kolom yang diberikan di args
            filters = [df[col].str.contains(self.query, case=False) for col in args]

            combined_filter = filters[0]
            for filt in filters[1:]:
                combined_filter = combined_filter | filt
            # Terapkan filter dan kembalikan hasil
            results = df[combined_filter]
            return results[list(args)]  # Memilih hanya kolom-kolom yang diberikan di args
        else:
            return None