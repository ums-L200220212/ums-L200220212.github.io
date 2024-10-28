from metaflow import FlowSpec, step

class KuliahInformatika():
    @step
    def start(self):
        print("""memuilai process""")
        self.next(self.langkah1)
    @step
    def langkah1(self):
        print("""bayar spp""")
        self.next(self.langkah2)
    @step
    def langkah2(self):
        print("""mengambil krs""")
        self.next(self.langkah3)
    @step
    def langkah3(self):
        print("mengikuti kelas")
        self.next(self.langkah4)
    @step
    def langkah4(self):
        print("mengikuti ujian tengah semester")
        self.next(self.langkah5)
    @step
    def langkah5(self):
        print("mengikuti kelas setelah uts")
        self.next(self.langkah6)
    @step
    def langkah6(self):
        print("membayar spp")
        self.next(self.langkah7)
    @step
    def langkah7(self):
        print("mengikuti ujian akhir semester")
        self.next(self.langkah8)
    @step
    def langkah8(self):
        print("menunggu nilai keluar di star ums")
        self.next(self.end)
    @step
    def end(self):
        print("proses berakhir")
if __name__ == '__main__':
    KuliahInformatika()