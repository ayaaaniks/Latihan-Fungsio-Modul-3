def konversi(j=0):
    def menit(m=0):
        def detik(d=0):
            return (((j * 7 * 24 * 60) + (m * 24 * 60) + (d * 60)))
        return detik
    return menit

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

OutputData = []

for data_item in data:
    data_split = data_item.split()
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int(data_split[6])
    
    konvert = konversi(minggu)(hari)(jam)(menit)
    OutputData.append(konvert)

print("OutputData =", OutputData)
