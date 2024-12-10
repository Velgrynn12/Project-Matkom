import pandas as pd


df = pd.read_csv(r'C:\Users\INDAH HARIYANTI\Downloads\datafikesabiess.csv')  


def prediksi_kelulusan(df, identifier):
    
    if isinstance(identifier, str):  
        mahasiswa = df[df['Nama'].str.lower() == identifier.lower()]
    elif isinstance(identifier, int):  
        mahasiswa = df[df['ID'] == identifier]
    else:
        return "Data tidak ditemukan."

    if mahasiswa.empty:
        return "Mahasiswa tidak ditemukan."
    
    
    rata_rata = mahasiswa[['Nilai Tugas', 'UTS', 'UAS']].mean(axis=1).values[0]
    status = mahasiswa['Status'].values[0]
    
    
    return f"Nama: {mahasiswa['Nama'].values[0]}\nID: {mahasiswa['ID'].values[0]}\nRata-rata Nilai: {rata_rata:.2f}\nStatus: {status}"


print(prediksi_kelulusan(df, 'Wati'))  
print(prediksi_kelulusan(df, 5))        
