import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Görüntü okunamıyor!")
        break
    
    # Gri Tonlama Filtresi
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Bulanık Görüntü
    blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    
    # Kenar Algılama
    edges = cv2.Canny(frame, 100, 200)
    
    # Toz Pembe ve Mor Filtre
    pink_purple_filter = frame.copy()
    
    # Parlaklık seviyesini kontrol ederek renk değişimi uygulama
    # Aydınlık yerler için toz pembe, karanlık yerler için mor
    for i in range(pink_purple_filter.shape[0]):
        for j in range(pink_purple_filter.shape[1]):
            # Pikselin parlaklığını hesapla (ortalama renk değeri)
            brightness = np.mean(pink_purple_filter[i, j])
            
            if brightness > 128:  # Aydınlık bölgeler
                pink_purple_filter[i, j] = [180, 130, 200]  # Toz pembe tonu (BGR formatında)
            else:  # Karanlık bölgeler
                pink_purple_filter[i, j] = [90, 60, 120]  # Mor tonu (BGR formatında)
    
    # Görüntüleri ekrana yazdır
    cv2.imshow("Orijinal", frame)
    cv2.imshow("Gri Tonlama", gray_frame)
    cv2.imshow("Bulanık Görüntü", blurred_frame)
    cv2.imshow("Kenar Algılama", edges)
    cv2.imshow("Toz Pembe ve Mor Filtre", pink_purple_filter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
