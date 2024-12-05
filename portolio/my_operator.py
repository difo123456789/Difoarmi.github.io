from datetime import datetime, timedelta

def calculate_parking_fee(hours):
    rate_per_hour = 2000
    total_fee = hours * rate_per_hour
    return total_fee

def main():
    print("Proyek Parkir Mall")
    
    try:
        # Input waktu masuk dan keluar dalam format HH:MM
        time_in = input("Masukkan waktu masuk (HH:MM): ")
        time_out = input("Masukkan waktu keluar (HH:MM): ")
        
        # Konversi waktu ke format datetime
        time_in = datetime.strptime(time_in, '%H:%M')
        time_out = datetime.strptime(time_out, '%H:%M')
        
        # Jika waktu keluar lebih awal dari waktu masuk, asumsikan waktu keluar adalah hari berikutnya
        if time_out < time_in:
            time_out += timedelta(days=1)
        
        # Hitung selisih waktu dalam jam
        total_hours = (time_out - time_in).seconds // 3600
        
        # Hitung biaya parkir
        total_fee = calculate_parking_fee(total_hours)
        
        print(f"Jumlah jam parkir: {total_hours} jam")
        print(f"Total biaya parkir adalah: Rp {total_fee}")
    except ValueError:
        print("Format waktu tidak valid. Silakan masukkan waktu dalam format HH:MM.")

if __name__ == "__main__":
    main()
