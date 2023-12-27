import cv2
import numpy as np

# Baca gambar
demo = cv2.imread(r"d:\materi\skd\p10 rsa\test.png", 0)

# Cek ukuran gambar
r, c = demo.shape

# Buat key acak dengan ukuran yang sama dengan gambar
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)

# Simpan key
cv2.imwrite(r"d:\materi\skd\p10 rsa\key.png", key)

# Enkripsi gambar dengan operasi XOR antara gambar dan key
encryption = cv2.bitwise_xor(demo, key)

# Simpan gambar yang telah dienkripsi
cv2.imwrite(r"d:\materi\skd\p10 rsa\encrypted.png", encryption)

# Dekripsi gambar dengan operasi XOR antara gambar terenkripsi dan key yang sama
decryption = cv2.bitwise_xor(encryption, key)

# Simpan gambar yang telah didekripsi
cv2.imwrite(r"d:\materi\skd\p10 rsa\decrypted.png", decryption)

# Tampilkan gambar asli, gambar terenkripsi, dan gambar yang telah didekripsi
cv2.imshow("Original", demo)
cv2.imshow("Encrypted", encryption)
cv2.imshow("Decrypted", decryption)

cv2.waitKey(0)
cv2.destroyAllWindows()
