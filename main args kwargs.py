import pandas as pd
from pathlib import Path

# Mendefinisikan path file CSV
filepath = Path("D:/MOCK_DATA.csv")  # Pastikan path file CSV sesuai dengan lokasi yang benar

# Membaca data dari file CSV ke dalam DataFrame
df = pd.read_csv(filepath)


def search_data(*args, **kwargs):
    query = kwargs.get('query', None)
    if query:
        # Buat filter untuk setiap kolom yang diberikan di args
        filters = [df[col].str.contains(query, case=False) for col in args]

        combined_filter = filters[0]
        for filt in filters[1:]:
            combined_filter = combined_filter | filt
        # Terapkan filter dan kembalikan hasil
        results = df[combined_filter]
        return results[list(args)]  # Memilih hanya kolom-kolom yang diberikan di args
    else:
        return None


# Contoh penggunaan
search_results = search_data('first_name', 'email', query='eggi')

# Mencetak nama dan email dari hasil pencarian
if search_results is not None and not search_results.empty:
    print(search_results)
else:
    print("Tidak ada hasil pencarian.")



