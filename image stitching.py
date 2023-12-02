from mpi4py import MPI
import cv2
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def stitch_gambar(direktori):
    if rank == 0:  # Master process
        # Membaca semua nama file dalam direktori
        nama_file = os.listdir(direktori)

        # Memastikan hanya 10 gambar yang akan diproses
        nama_file = nama_file[:4]

        # Membaca semua gambar
        gambar = [cv2.imread(os.path.join(direktori, nf)) for nf in nama_file]

        # Membuat objek stitcher
        stitcher = cv2.Stitcher_create()

        # Melakukan stitching pada gambar
        status, pano = stitcher.stitch(gambar)

        if status == cv2.Stitcher_OK:
            # Menyimpan gambar hasil stitching
            cv2.imwrite('hasil_stitching.jpg', pano)
            print('Stitching berhasil, gambar disimpan sebagai hasil_stitching.jpg')
        else:
            print('Stitching gagal, status:', status)
    else:
        if rank == 1:
            print('')
        elif rank == 2:
            print('')

# Contoh penggunaan:
if __name__ == "__main__":
    stitch_gambar('data_real')
